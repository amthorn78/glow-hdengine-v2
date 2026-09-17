# Project Prompt Contract Registry — GCFPE-20260914.1 / 091426.1

artifact_type: `PROJECT_PROMPT_CONTRACT_REGISTRY`  
status: `APPROVED`  
approved_by: `Nathan / Product Owner`  
approved_at: `2026-09-17`  
release: `GCFPE-20260914.1 / 091426.1 / 55`  
home: `docs/prompt_ecosystem_management/`  
supersedes: `GCFPE-20260914.1-Predecessor-Project-Prompt-Registry.md` (DRAFT, 091326.2 / 54), removed from `docs/ephemeral/` in the same change

```yaml
schema_version: project-prompt-contract-registry/1.0
registry_id: GCFPE-PCR-20260914.1
project_id: glow-hde
status: APPROVED
approved_by: Nathan / Product Owner
approved_at: 2026-09-17
workspace_skill_registry_id: WSR-20260914.1-OBSERVATIONAL
authority_sources:
- type: SELECTED_RELEASE_REGISTER
  release: GCFPE-20260914.1
  url: https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1
- type: SELECTED_CATALOG
  version_family: '091426.1'
  member_count: 55
  url: https://app.notion.com/p/3da4590a05eb81bcbc5deb2d2cec4f1f
- type: COMPLETE_PROMPT_FETCH_MANIFEST
  path: candidate/prompts/manifest.json
  note: 55-prompt candidate extraction, 2026-09-17
- type: COMPLETE_PROMPT_FETCH_MANIFEST
  path: candidate/prompts/manifest.json
- type: COMPLETE_PROMPT_FETCH_MANIFEST
  path: candidate/prompts/manifest.json
- type: COMPLETE_PROMPT_FETCH_MANIFEST
  path: candidate/prompts/manifest.json
observation:
  release: GCFPE-20260914.1
  version_family: '091426.1'
  selected_member_count: 55
  complete_body_count: 54
  mutation_posture: READ_ONLY
lanes:
- lane: GCFPE-MGMT
  title: GCFPE management
  notion_parent_id: 3cc4590a05eb8101b5ded32c12616eb6
  notion_parent_title: Glow HDE Prompt Flow Index
  active: true
- lane: CF-PO
  title: Product Owner change-class selection
  notion_parent_id: 3c74590a05eb811d8433e7022629e213
  notion_parent_title: HDE Change Flow
  active: true
- lane: CF-C
  title: CRD specification
  notion_parent_id: 3c74590a05eb811d8433e7022629e213
  notion_parent_title: HDE Change Flow
  active: true
- lane: CF-E
  title: Epic specification
  notion_parent_id: 3c74590a05eb811d8433e7022629e213
  notion_parent_title: HDE Change Flow
  active: true
- lane: CL-C
  title: CRD closure
  notion_parent_id: 3c74590a05eb811d8433e7022629e213
  notion_parent_title: HDE Change Flow
  active: true
- lane: CL-E
  title: Epic closure and PF09 maintenance
  notion_parent_id: 3c74590a05eb811d8433e7022629e213
  notion_parent_title: HDE Change Flow
  active: true
- lane: CL
  title: Shared closure administration
  notion_parent_id: 3c74590a05eb811d8433e7022629e213
  notion_parent_title: HDE Change Flow
  active: true
- lane: DOC
  title: Repository documentation
  notion_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  notion_parent_title: HDE IA
  active: true
- lane: ESC
  title: Escalation and remediation
  notion_parent_id: 3c74590a05eb8123bc55ca7f99ce176c
  notion_parent_title: Escalation
  active: true
- lane: IA
  title: Whole-change implementation audit and plan
  notion_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  notion_parent_title: HDE IA
  active: true
- lane: MGR
  title: Optional flow coordination
  notion_parent_id: 3c74590a05eb811d8433e7022629e213
  notion_parent_title: HDE Change Flow
  active: true
- lane: OPS
  title: Bounded operations
  notion_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  notion_parent_title: HDE IA
  active: true
- lane: PR
  title: PR work-unit development
  notion_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  notion_parent_title: HDE IA
  active: true
- lane: QA
  title: Whole-change QA
  notion_parent_id: 3c74590a05eb8149905fd694f6d2901a
  notion_parent_title: HDE QA
  active: true
- lane: RS
  title: Bounded rescope
  notion_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  notion_parent_title: HDE IA
  active: true
- lane: UTIL
  title: Exact redline utility
  notion_parent_id: 3c74590a05eb8176baf8cb59f1631f3c
  notion_parent_title: HDE TW
  active: true
prompts:
- prompt_key: CF-C-10
  notion_page_id: 3db4590a05eb8119a5a8e4d083fcf360
  notion_url: https://app.notion.com/p/3db4590a05eb8119a5a8e4d083fcf360
  expected_title: CF-C-10 — Prepare CRD Specification Kickoff Handoff — 091426.1
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
    - KICKOFF_READY
    consumers: &id001
    - CF-C-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 7276 bytes'
  - 'SHA-256 of that extraction: 0e449fe7730e4493e775d407ea38c36b7ac9dec58281f0ba4a030ce134f5105d'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id001
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CF-C-10.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CF-C-10.md
    sha256: 0e449fe7730e4493e775d407ea38c36b7ac9dec58281f0ba4a030ce134f5105d
    bytes: 7276
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CF-C-20
  notion_page_id: 3db4590a05eb8173a73edc73f302a90a
  notion_url: https://app.notion.com/p/3db4590a05eb8173a73edc73f302a90a
  expected_title: CF-C-20 — Create CRD Specification — 091426.1
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
    - SPECIFICATION_PENDING
    consumers: &id002
    - CF-C-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 5973 bytes'
  - 'SHA-256 of that extraction: 6995097d2950f2ddd0425ed088cfe1d4dea9b2850ea94deec232965749cb8f6d'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id002
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CF-C-20.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CF-C-20.md
    sha256: 6995097d2950f2ddd0425ed088cfe1d4dea9b2850ea94deec232965749cb8f6d
    bytes: 5973
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CF-C-30
  notion_page_id: 3db4590a05eb8149a8d2ed42c9c01ffd
  notion_url: https://app.notion.com/p/3db4590a05eb8149a8d2ed42c9c01ffd
  expected_title: CF-C-30 — Review and Approve CRD Specification — 091426.1
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
    - INITIAL_APPROVE
    - INITIAL_DENY
    - DELTA_APPROVE
    - DELTA_DENY
    consumers: &id003
    - IA-10
    - CF-C-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 10121 bytes'
  - 'SHA-256 of that extraction: 4b7b6b739c909f6bdb994985d5ec5b6084d63cacf372712301cdb3c2afd76f24'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id003
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CF-C-30.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CF-C-30.md
    sha256: 4b7b6b739c909f6bdb994985d5ec5b6084d63cacf372712301cdb3c2afd76f24
    bytes: 10121
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CF-C-40
  notion_page_id: 3db4590a05eb81269931cee342ce8a0e
  notion_url: https://app.notion.com/p/3db4590a05eb81269931cee342ce8a0e
  expected_title: CF-C-40 — Revise CRD Specification — 091426.1
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 7597 bytes'
  - 'SHA-256 of that extraction: ccfcbd5d4595d3455f059e90b3a715063d3fc4316f3278b39999e8a331949218'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id004
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CF-C-40.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CF-C-40.md
    sha256: ccfcbd5d4595d3455f059e90b3a715063d3fc4316f3278b39999e8a331949218
    bytes: 7597
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CF-E-10
  notion_page_id: 3db4590a05eb815b84a5c5a5ace85fe1
  notion_url: https://app.notion.com/p/3db4590a05eb815b84a5c5a5ace85fe1
  expected_title: CF-E-10 — Prepare Epic Specification Kickoff Handoff — 091426.1
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
    - KICKOFF_READY
    consumers: &id005
    - CF-E-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 7380 bytes'
  - 'SHA-256 of that extraction: 02eb026dfb7a891b4ff1e778a66676b070419fbce575c25daec6ef0b0c131410'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id005
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CF-E-10.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CF-E-10.md
    sha256: 02eb026dfb7a891b4ff1e778a66676b070419fbce575c25daec6ef0b0c131410
    bytes: 7380
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CF-E-20
  notion_page_id: 3db4590a05eb810eb177f7dced41bc8f
  notion_url: https://app.notion.com/p/3db4590a05eb810eb177f7dced41bc8f
  expected_title: CF-E-20 — Create Epic Specification — 091426.1
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
    - SPECIFICATION_PENDING
    consumers: &id006
    - CF-E-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 5985 bytes'
  - 'SHA-256 of that extraction: a3305b3a9da58e9fbebd8ce7cda8df889aca76cda0342a6826704ddb8fbcfd23'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id006
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CF-E-20.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CF-E-20.md
    sha256: a3305b3a9da58e9fbebd8ce7cda8df889aca76cda0342a6826704ddb8fbcfd23
    bytes: 5985
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CF-E-30
  notion_page_id: 3db4590a05eb81b4be79f405566da9a7
  notion_url: https://app.notion.com/p/3db4590a05eb81b4be79f405566da9a7
  expected_title: CF-E-30 — Review and Approve Epic Specification — 091426.1
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
    - INITIAL_APPROVE
    - INITIAL_DENY
    - DELTA_APPROVE
    - DELTA_DENY
    consumers: &id007
    - IA-10
    - CF-E-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 10129 bytes'
  - 'SHA-256 of that extraction: 00e55e788b4e6662a37bec715cf503ae783dec3d9fb60c74a11467463e58c3a1'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id007
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CF-E-30.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CF-E-30.md
    sha256: 00e55e788b4e6662a37bec715cf503ae783dec3d9fb60c74a11467463e58c3a1
    bytes: 10129
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CF-E-40
  notion_page_id: 3db4590a05eb8101b655ed223b11a85e
  notion_url: https://app.notion.com/p/3db4590a05eb8101b655ed223b11a85e
  expected_title: CF-E-40 — Revise Epic Specification — 091426.1
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 7612 bytes'
  - 'SHA-256 of that extraction: ce8bed7759d9d1b2e6c0f4427da9d45a98514969a6b43bec71d93b453070b73f'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id008
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CF-E-40.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CF-E-40.md
    sha256: ce8bed7759d9d1b2e6c0f4427da9d45a98514969a6b43bec71d93b453070b73f
    bytes: 7612
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CF-PO-10
  notion_page_id: 3db4590a05eb8161b4d7cb6d07f5101c
  notion_url: https://app.notion.com/p/3db4590a05eb8161b4d7cb6d07f5101c
  expected_title: CF-PO-10 — Record Product Owner Change-Class Selection — 091426.1
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
    - CF-E-10
    - CF-C-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 6164 bytes'
  - 'SHA-256 of that extraction: ca3d97a07474b610cdc9f036bac0ec93ccf058502d443724c9fa7ed2dd7adbaa'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id009
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CF-PO-10.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CF-PO-10.md
    sha256: ca3d97a07474b610cdc9f036bac0ec93ccf058502d443724c9fa7ed2dd7adbaa
    bytes: 6164
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CL-20
  notion_page_id: 3db4590a05eb81f4812be61e8877c02c
  notion_url: https://app.notion.com/p/3db4590a05eb81f4812be61e8877c02c
  expected_title: CL-20 — Prepare Post-Closure Drainage and Closure Memo — 091426.1
  lane: CL
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Prepare Post-Closure Drainage and Closure Memo for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, after the positive terminal closure decision.
  creator_role: Isis, after the positive terminal closure decision.
  reviewer_role: NONE
  inputs:
  - CHANGE_CLOSURE_DECISION_ID
  - CLOSE
  outputs:
  - artifact: CLOSURE_MEMO / POST_CLOSURE_DRAINAGE
    states:
    - POST_CLOSURE_PENDING
    consumers: &id010
    - CL-30
    - CL-E-20
    - CL-E-40
    - CL-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 33952 bytes'
  - 'SHA-256 of that extraction: bcf1dd21f0ec6afe4f0c6b363a054decc031a94c67b871d22e8d79316b092b78'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id010
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CL-20.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CL-20.md
    sha256: bcf1dd21f0ec6afe4f0c6b363a054decc031a94c67b871d22e8d79316b092b78
    bytes: 33952
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CL-30
  notion_page_id: 3db4590a05eb8190a444d8818e445c1d
  notion_url: https://app.notion.com/p/3db4590a05eb8190a444d8818e445c1d
  expected_title: CL-30 — Prepare Conditional Post-Change ADR Maintenance — 091426.1
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
    - CL-20
    - CL-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 30792 bytes'
  - 'SHA-256 of that extraction: 60e01caed575653a8c0992dce1001f1668de69f734583427f1c9d2545ddb1dd6'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id011
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CL-30.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CL-30.md
    sha256: 60e01caed575653a8c0992dce1001f1668de69f734583427f1c9d2545ddb1dd6
    bytes: 30792
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CL-40
  notion_page_id: 3db4590a05eb81db9c88cde6027e07bf
  notion_url: https://app.notion.com/p/3db4590a05eb81db9c88cde6027e07bf
  expected_title: CL-40 — Scan for PF09 Gaps and CRD Candidates — 091426.1
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
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 30437 bytes'
  - 'SHA-256 of that extraction: bc8970a7e52ce216ba20311497e023b9cbee106dd1062783e8794166504decee'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id012
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CL-40.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CL-40.md
    sha256: bc8970a7e52ce216ba20311497e023b9cbee106dd1062783e8794166504decee
    bytes: 30437
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CL-C-10
  notion_page_id: 3db4590a05eb81ad8989faa77f441a64
  notion_url: https://app.notion.com/p/3db4590a05eb81ad8989faa77f441a64
  expected_title: CL-C-10 — Perform CRD Retrospective and Decide Closure — 091426.1
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 37121 bytes'
  - 'SHA-256 of that extraction: 5e61b02e8939dea84d517ea6c3e80a9e0a45b060fbdd8c8361e96ce9fb92a511'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id013
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CL-C-10.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CL-C-10.md
    sha256: 5e61b02e8939dea84d517ea6c3e80a9e0a45b060fbdd8c8361e96ce9fb92a511
    bytes: 37121
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CL-E-10
  notion_page_id: 3db4590a05eb811a8578d75885c16cac
  notion_url: https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac
  expected_title: CL-E-10 — Perform Epic Retrospective and Decide Closure — 091426.1
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 37579 bytes'
  - 'SHA-256 of that extraction: 13380a6babd2c71cb8a6bedce6b26f3573cc957187e119fddd2850f35a33841b'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id014
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CL-E-10.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CL-E-10.md
    sha256: 13380a6babd2c71cb8a6bedce6b26f3573cc957187e119fddd2850f35a33841b
    bytes: 37579
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CL-E-20
  notion_page_id: 3db4590a05eb81c2b5d5ff46126f9e45
  notion_url: https://app.notion.com/p/3db4590a05eb81c2b5d5ff46126f9e45
  expected_title: CL-E-20 — Perform Bounded PF09 Epic Revalidation — 091426.1
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
    - COMPLETE
    - PARTIAL
    - BLOCKED
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 15304 bytes'
  - 'SHA-256 of that extraction: 439366e754cba931fe1ef0022ebd516fbe37b7514290703c6bf25f49767b8e70'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id015
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CL-E-20.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CL-E-20.md
    sha256: 439366e754cba931fe1ef0022ebd516fbe37b7514290703c6bf25f49767b8e70
    bytes: 15304
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CL-E-30
  notion_page_id: 3db4590a05eb81b4a649fdcdb1903345
  notion_url: https://app.notion.com/p/3db4590a05eb81b4a649fdcdb1903345
  expected_title: CL-E-30 — Review Bounded PF09 Revalidation — 091426.1
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
    - CL-E-40
    - CL-E-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 14180 bytes'
  - 'SHA-256 of that extraction: 7dfb3c0d6ec737cbcec4fa26b09afa96fc06b91d6742a16f80513f50bf99888d'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id016
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CL-E-30.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CL-E-30.md
    sha256: 7dfb3c0d6ec737cbcec4fa26b09afa96fc06b91d6742a16f80513f50bf99888d
    bytes: 14180
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: CL-E-40
  notion_page_id: 3db4590a05eb81e78e82f83a5f2e4b68
  notion_url: https://app.notion.com/p/3db4590a05eb81e78e82f83a5f2e4b68
  expected_title: CL-E-40 — Prepare Post-Epic PF09 Maintenance — 091426.1
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
    - CL-E-20
    - CL-E-30
    - CL-20
    - CL-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 16002 bytes'
  - 'SHA-256 of that extraction: cccef152db6eb0f9d6cd0c4e7338f51d73ffd4069abe7512c4d3b4e6ba8c3a5c'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id017
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/CL-E-40.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/CL-E-40.md
    sha256: cccef152db6eb0f9d6cd0c4e7338f51d73ffd4069abe7512c4d3b4e6ba8c3a5c
    bytes: 16002
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: DOC-10
  notion_page_id: 3db4590a05eb8193a9a8d7ddd751cd2d
  notion_url: https://app.notion.com/p/3db4590a05eb8193a9a8d7ddd751cd2d
  expected_title: DOC-10 — Create Final Repository Documentation PR Instructions — 091426.1
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
  - REMEDIATION_PLAN_REVIEW_ID
  - BLOCKED
  - PENDING
  - PARTIAL
  - FAILED
  outputs:
  - artifact: PR_INSTRUCTION
    states:
    - INSTRUCTION_READY
    - DRAFT
    - BLOCKED
    consumers: &id018
    - PR-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 20261 bytes'
  - 'SHA-256 of that extraction: dbeb6f96a39b4868e750e72b3f39ba6fafaf8d4790626f122385830af3de502f'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id018
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/DOC-10.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/DOC-10.md
    sha256: dbeb6f96a39b4868e750e72b3f39ba6fafaf8d4790626f122385830af3de502f
    bytes: 20261
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: DOC-20
  notion_page_id: 3db4590a05eb8164ac09e722dc967f25
  notion_url: https://app.notion.com/p/3db4590a05eb8164ac09e722dc967f25
  expected_title: DOC-20 — Verify Final Repository Documentation Completion — 091426.1
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
  - REMEDIATION_PLAN_REVIEW_ID
  outputs:
  - artifact: DOCUMENTATION_COMPLETION
    states:
    - COMPLETE
    - INCOMPLETE
    consumers: &id019
    - QA-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 20784 bytes'
  - 'SHA-256 of that extraction: 967fcdd78641d410e5255579010931146f7711eb4884a0601d6eefb450b5dbc6'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id019
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/DOC-20.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/DOC-20.md
    sha256: 967fcdd78641d410e5255579010931146f7711eb4884a0601d6eefb450b5dbc6
    bytes: 20784
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: ESC-10
  notion_page_id: 3db4590a05eb81d582b8d490e77f9f40
  notion_url: https://app.notion.com/p/3db4590a05eb81d582b8d490e77f9f40
  expected_title: ESC-10 — Create QA Escalation Report — 091426.1
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 17169 bytes'
  - 'SHA-256 of that extraction: 87b310229a85227426392c40e1d928558de07d4fa80efd35657a665aaede3a82'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id020
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/ESC-10.md
  expected_parent_id: 3c74590a05eb8123bc55ca7f99ce176c
  expected_parent_title: Escalation
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/ESC-10.md
    sha256: 87b310229a85227426392c40e1d928558de07d4fa80efd35657a665aaede3a82
    bytes: 17169
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: ESC-25
  notion_page_id: 3db4590a05eb81bf9326e46a1017de38
  notion_url: https://app.notion.com/p/3db4590a05eb81bf9326e46a1017de38
  expected_title: ESC-25 — Execute Bounded Escalation Discovery — 091426.1
  lane: ESC
  sequence: 25
  lifecycle: ACTIVE
  function: Execute Execute Bounded Escalation Discovery for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the explicitly named read-only repository reviewer or authorized environment operator.
  creator_role: the explicitly named read-only repository reviewer or authorized environment operator.
  reviewer_role: NONE
  inputs:
  - REMEDIATION_PLAN_ID
  - DISCOVERY_TASK_ID
  - TRIAGE_RECEIPT_ID
  outputs:
  - artifact: DISCOVERY_RESULT
    states:
    - COMPLETE
    - PARTIAL
    - BLOCKED
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 17817 bytes'
  - 'SHA-256 of that extraction: 1d04bc4b76a28557502a9b499d10ec00b65b1282f405b0cdf8ea2ec6091499cd'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id021
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/ESC-25.md
  expected_parent_id: 3c74590a05eb8123bc55ca7f99ce176c
  expected_parent_title: Escalation
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/ESC-25.md
    sha256: 1d04bc4b76a28557502a9b499d10ec00b65b1282f405b0cdf8ea2ec6091499cd
    bytes: 17817
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: ESC-30
  notion_page_id: 3db4590a05eb813e99b4e416bc7afdae
  notion_url: https://app.notion.com/p/3db4590a05eb813e99b4e416bc7afdae
  expected_title: ESC-30 — Diagnose and Propose Bounded Remediation — 091426.1
  lane: ESC
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Diagnose and Propose Bounded Remediation for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Thoth, the continuing Head of Development and remediation proposal author for this change.
  creator_role: Thoth, the continuing Head of Development and remediation proposal author for this change.
  reviewer_role: NONE
  inputs:
  - ORIGINATING_FINDING_REF
  - QA_ESCALATION_REPORT_ID
  - CHANGE_CLASS
  - CHANGE_ID
  - REMEDIATION_PLAN_ID
  - DISCOVERY_RESULT_IDS
  - REMEDIATION_PLAN_REVIEW_ID
  outputs:
  - artifact: REMEDIATION_PROPOSAL
    states:
    - REMEDIATION_PENDING
    - DISCOVERY_REQUIRED
    - BLOCKED
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 18446 bytes'
  - 'SHA-256 of that extraction: 579c893c9576a25233a7238dffc01333058cedfd8de01d73df8bc669539962c9'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id022
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/ESC-30.md
  expected_parent_id: 3c74590a05eb8123bc55ca7f99ce176c
  expected_parent_title: Escalation
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/ESC-30.md
    sha256: 579c893c9576a25233a7238dffc01333058cedfd8de01d73df8bc669539962c9
    bytes: 18446
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: ESC-40
  notion_page_id: 3db4590a05eb81efb6d4cd8d02ba9756
  notion_url: https://app.notion.com/p/3db4590a05eb81efb6d4cd8d02ba9756
  expected_title: ESC-40 — Review and Return Approved Remediation — 091426.1
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
    - RS-40
    - IA-40
    - IA-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 18896 bytes'
  - 'SHA-256 of that extraction: 8ca0090c6b067e55e744d52eccf5d9f9ba2ff9898e05266dfda0f1033fe2a8c9'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id023
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/ESC-40.md
  expected_parent_id: 3c74590a05eb8123bc55ca7f99ce176c
  expected_parent_title: Escalation
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/ESC-40.md
    sha256: 8ca0090c6b067e55e744d52eccf5d9f9ba2ff9898e05266dfda0f1033fe2a8c9
    bytes: 18896
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: GCFPE-MGMT-10
  notion_page_id: 3db4590a05eb81d1bb64ebcb3ca8eb54
  notion_url: https://app.notion.com/p/3db4590a05eb81d1bb64ebcb3ca8eb54
  expected_title: GCFPE-MGMT-10 — Manage an Ecosystem Change — 091426.1
  lane: GCFPE-MGMT
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Manage an Ecosystem Change for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: Act as the Managing Prompt Engineer for one requested GCFPE change.
  creator_role: Act as the Managing Prompt Engineer for one requested GCFPE change.
  reviewer_role: NONE
  inputs:
  - Use the user's supplied error report, requested change, runtime/environment update or proposed new prompt.
  outputs:
  - artifact: GCFPE_SUCCESSOR_RELEASE / CHANGE_RECORD
    states:
    - COMPLETED_AND_PUBLISHED
    - CANDIDATE_AWAITING_DECISION
    - BLOCKED
    consumers: &id024
    - CF-PO-10
    - CF-E-10
    - CF-C-10
  mutations:
    allowed:
    - Perform only the authorized GCFPE prompt/control publication mutations
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 8065 bytes'
  - 'SHA-256 of that extraction: 85729677e80aa579fb9ca80684eeab1dd0b7c7a5d95561051c4844da570e4e1c'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id024
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/GCFPE-MGMT-10.md
  expected_parent_id: 3cc4590a05eb8101b5ded32c12616eb6
  expected_parent_title: Glow HDE Prompt Flow Index
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/GCFPE-MGMT-10.md
    sha256: 85729677e80aa579fb9ca80684eeab1dd0b7c7a5d95561051c4844da570e4e1c
    bytes: 8065
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: IA-10
  notion_page_id: 3db4590a05eb817aa191f1e822c30480
  notion_url: https://app.notion.com/p/3db4590a05eb817aa191f1e822c30480
  expected_title: IA-10 — Create Whole-Change Implementation Audit and Plan — 091426.1
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
    - PLAN_PENDING
    - BLOCKED
    consumers: &id025
    - IA-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 10287 bytes'
  - 'SHA-256 of that extraction: 2adcc3b6a7f7e9264fc4dde8cd64d8242f8fa4f95ddb875f3be2887c85257c68'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id025
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/IA-10.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/IA-10.md
    sha256: 2adcc3b6a7f7e9264fc4dde8cd64d8242f8fa4f95ddb875f3be2887c85257c68
    bytes: 10287
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: IA-20
  notion_page_id: 3db4590a05eb81c4825df2ad0dec4750
  notion_url: https://app.notion.com/p/3db4590a05eb81c4825df2ad0dec4750
  expected_title: IA-20 — Create Whole-Change Implementation Plan — 091426.1
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
    - PLAN_PENDING
    - BLOCKED
    consumers: &id026
    - IA-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 6332 bytes'
  - 'SHA-256 of that extraction: fccb50a0746843e6d5bbcd401f820a95802d40f1825778e2a7b393b9f558db3f'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id026
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/IA-20.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/IA-20.md
    sha256: fccb50a0746843e6d5bbcd401f820a95802d40f1825778e2a7b393b9f558db3f
    bytes: 6332
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: IA-30
  notion_page_id: 3db4590a05eb81c6bfb5f36f7df8f464
  notion_url: https://app.notion.com/p/3db4590a05eb81c6bfb5f36f7df8f464
  expected_title: IA-30 — Review Whole-Change Implementation Plan — 091426.1
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
    - APPROVE
    - DENY
    consumers: &id027
    - PR-10
    - IA-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 9858 bytes'
  - 'SHA-256 of that extraction: a757109e79b733bc45cb9d05d337f7f361a4d661bcf23586a18d0153681473e7'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id027
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/IA-30.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/IA-30.md
    sha256: a757109e79b733bc45cb9d05d337f7f361a4d661bcf23586a18d0153681473e7
    bytes: 9858
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: IA-40
  notion_page_id: 3db4590a05eb8197bb1bc8f52f896969
  notion_url: https://app.notion.com/p/3db4590a05eb8197bb1bc8f52f896969
  expected_title: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 091426.1
  lane: IA
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Prepare or Revise Whole-Change Implementation Plan for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the same Implementation Agent (IA) who authored the pending preapproval whole-change Plan.
  creator_role: the same Implementation Agent (IA) who authored the pending preapproval whole-change Plan.
  reviewer_role: Isis / Lead Developer
  inputs:
  - Require one complete pending initial Implementation Plan plus the exact IA-30 denial/redline for that version, or an interrupted preapproval
    recovery package with the same author/reviewer lineage.
  outputs:
  - artifact: IMPLEMENTATION_PLAN
    states:
    - PLAN_PENDING_REVISED
    - WRONG_ROUTE_APPROVED_BASE
    consumers: &id028
    - IA-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 5537 bytes'
  - 'SHA-256 of that extraction: 78c209da41eb258c4dd5c667e71150b2585eb3355758020aab02294dc5a71083'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id028
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/IA-40.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/IA-40.md
    sha256: 78c209da41eb258c4dd5c667e71150b2585eb3355758020aab02294dc5a71083
    bytes: 5537
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: IA-50
  notion_page_id: 3db4590a05eb81d78eeae384e93dd697
  notion_url: https://app.notion.com/p/3db4590a05eb81d78eeae384e93dd697
  expected_title: IA-50 — IA Answer Seeder — 091426.1
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
    - SEED_READY
    - SEED_INCOMPLETE
    consumers: &id029
    - IA-10
    - IA-20
    - IA-30
    - IA-40
    - ESC-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 6526 bytes'
  - 'SHA-256 of that extraction: 504f9454328a2230ace76128d1837fbeae404e14d01384226a4a7025daa9492d'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id029
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/IA-50.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/IA-50.md
    sha256: 504f9454328a2230ace76128d1837fbeae404e14d01384226a4a7025daa9492d
    bytes: 6526
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: IA-60
  notion_page_id: 3db4590a05eb8141b5b2c8fbf7b725e2
  notion_url: https://app.notion.com/p/3db4590a05eb8141b5b2c8fbf7b725e2
  expected_title: IA-60 — Thoth Planning Research — 091426.1
  lane: IA
  sequence: 60
  lifecycle: ACTIVE
  function: Execute Thoth Planning Research for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: Act as Thoth for one bounded advanced engineering planning inquiry before Plan approval.
  creator_role: Act as Thoth for one bounded advanced engineering planning inquiry before Plan approval.
  reviewer_role: NONE
  inputs:
  - 'PLANNING_INQUIRY: exact original question/identity; actual files/interfaces and repository evidence; constraints, alternatives, failure modes,
    decision criteria and specific requested finding.'
  outputs:
  - artifact: PLANNING_RESEARCH_FINDING
    states:
    - RESEARCH_COMPLETE
    - PARTIAL
    - BLOCKED
    consumers: &id030
    - IA-50
    - ESC-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 5357 bytes'
  - 'SHA-256 of that extraction: 6a8971c4c2bc1ca9000843b7da2b2df86f08ec6eb8f1b2ffa701a930700c0deb'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id030
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/IA-60.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/IA-60.md
    sha256: 6a8971c4c2bc1ca9000843b7da2b2df86f08ec6eb8f1b2ffa701a930700c0deb
    bytes: 5357
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: MGR-10
  notion_page_id: 3db4590a05eb8108ad2dd4d0e20bd6c4
  notion_url: https://app.notion.com/p/3db4590a05eb8108ad2dd4d0e20bd6c4
  expected_title: MGR-10 — Coordinate the Complete Change Flow within Current Authority — 091426.1
  lane: MGR
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Coordinate the Complete Change Flow within Current Authority for the exact supplied change.
  session_class: ORCHESTRATOR_RUN
  session_role: You are the Change Flow coordinator, without taking over any substantive actor or approval.
  creator_role: the Change Flow coordinator, without taking over any substantive actor or approval.
  reviewer_role: NONE
  inputs:
  - For a request only to prepare Product Owner cycle-entry launch guidance, accept known or unresolved classification and all actual intake without
    inventing change identity.
  outputs:
  - artifact: FLOW_PROGRESS
    states:
    - FLOW_PROGRESS
    - TERMINAL_RETURN
    consumers: &id031
    - CF-PO-10
    - CF-E-10
    - CF-C-10
    - QA-10
    - CL-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 7357 bytes'
  - 'SHA-256 of that extraction: 63b4897d9774eea985f94b78b4d43b83a3443a3be8adb7543283042e2882810b'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id031
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/MGR-10.md
  expected_parent_id: 3c74590a05eb811d8433e7022629e213
  expected_parent_title: HDE Change Flow
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/MGR-10.md
    sha256: 63b4897d9774eea985f94b78b4d43b83a3443a3be8adb7543283042e2882810b
    bytes: 7357
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: OPS-10
  notion_page_id: 3db4590a05eb81db98cce3e30a62bce5
  notion_url: https://app.notion.com/p/3db4590a05eb81db98cce3e30a62bce5
  expected_title: OPS-10 — Create Bounded Ops Task — 091426.1
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
  - REMEDIATION_PLAN_REVIEW_ID
  outputs:
  - artifact: OPS_TASK
    states:
    - READY
    - BLOCKED
    consumers: &id032
    - OPS-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 43576 bytes'
  - 'SHA-256 of that extraction: 47f2e40af709fbfc1486d7fca67a2114527aa2a2fd2be8bb3f03e268f236d25d'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id032
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/OPS-10.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/OPS-10.md
    sha256: 47f2e40af709fbfc1486d7fca67a2114527aa2a2fd2be8bb3f03e268f236d25d
    bytes: 43576
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: OPS-20
  notion_page_id: 3db4590a05eb81858a9dd361d3689ce8
  notion_url: https://app.notion.com/p/3db4590a05eb81858a9dd361d3689ce8
  expected_title: OPS-20 — Execute Bounded Ops Task — 091426.1
  lane: OPS
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Execute Bounded Ops Task for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the authorized DevOps or target-environment operator for the exact bounded operation supplied in OPS_TASK_ID.
  creator_role: the authorized DevOps or target-environment operator for the exact bounded operation supplied in OPS_TASK_ID.
  reviewer_role: NONE
  inputs:
  - OPS_TASK_ID
  outputs:
  - artifact: OPS_EXECUTION_RESULT
    states:
    - COMPLETE
    - PARTIAL
    - BLOCKED
    - FAILED
    - NOT_EXECUTED
    - NOT_PRODUCED
    consumers: &id033
    - OPS-30
  mutations:
    allowed:
    - Execute only the bounded OPS_TASK mutations
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 37499 bytes'
  - 'SHA-256 of that extraction: 066ace58820320724fab5e22b269f33fa13db92c646a46e9b7462b6b273b4a0f'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id033
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/OPS-20.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/OPS-20.md
    sha256: 066ace58820320724fab5e22b269f33fa13db92c646a46e9b7462b6b273b4a0f
    bytes: 37499
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: OPS-30
  notion_page_id: 3db4590a05eb816f91c9c394f9c9fa57
  notion_url: https://app.notion.com/p/3db4590a05eb816f91c9c394f9c9fa57
  expected_title: OPS-30 — Review Ops Execution Receipt — 091426.1
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
    consumers: &id034
    - OPS-10
    - OPS-20
    - ESC-30
    - RS-10
    - RS-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 58399 bytes'
  - 'SHA-256 of that extraction: 6a90191f32d8c9a8698bb39abb6fd5043dcb1afd8a27f28317e3b0e649f0381e'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id034
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/OPS-30.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/OPS-30.md
    sha256: 6a90191f32d8c9a8698bb39abb6fd5043dcb1afd8a27f28317e3b0e649f0381e
    bytes: 58399
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: PR-10
  notion_page_id: 3db4590a05eb818e8359de1994e97a7d
  notion_url: https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d
  expected_title: PR-10 — Create PR Work-Unit Instructions — 091426.1
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
  - REMEDIATION_PLAN_REVIEW_ID
  outputs:
  - artifact: PR_INSTRUCTION
    states:
    - INSTRUCTION_READY
    - DRAFT
    - BLOCKED
    consumers: &id035
    - PR-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 50295 bytes'
  - 'SHA-256 of that extraction: a731f158057d5ff896a13e1ada3d323bbd20d827de577ed005ddf01e334913e4'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id035
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/PR-10.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/PR-10.md
    sha256: a731f158057d5ff896a13e1ada3d323bbd20d827de577ed005ddf01e334913e4
    bytes: 50295
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: PR-20
  notion_page_id: 3db4590a05eb8174abf8c04318ab04be
  notion_url: https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be
  expected_title: PR-20 — Create Detailed PR Implementation Plan — 091426.1
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
  outputs:
  - artifact: PR_IMPLEMENTATION_PLAN
    states:
    - AWAITING_PO_PROCEED
    - DRAFT
    - BLOCKED
    consumers: &id036
    - PR-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 52673 bytes'
  - 'SHA-256 of that extraction: 3d0b5c6dec34ce39e04d2229a6e5a3cf5c0919552a40c5e0e4426516a08c3c2f'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id036
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/PR-20.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/PR-20.md
    sha256: 3d0b5c6dec34ce39e04d2229a6e5a3cf5c0919552a40c5e0e4426516a08c3c2f
    bytes: 52673
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: PR-30
  notion_page_id: 3db4590a05eb8123afb8caeeaa83a294
  notion_url: https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294
  expected_title: PR-30 — PR Implementation Proceed — 091426.1
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
    - MERGE_PENDING
    - RESCOPE_PENDING
    - RECOVERY_PENDING
    - PRODUCT_OWNER_DECISION_REQUIRED
    consumers: &id037
    - PR-40
    - RS-20
  mutations:
    allowed:
    - Implement, test, commit, publish, and review-correct the exact proceeded PR work unit
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 40571 bytes'
  - 'SHA-256 of that extraction: c666d6560a8aac597612944b4ef3755ec29351229ad128d86b9142cc89a546fe'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id037
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/PR-30.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/PR-30.md
    sha256: c666d6560a8aac597612944b4ef3755ec29351229ad128d86b9142cc89a546fe
    bytes: 40571
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: PR-35
  notion_page_id: 3db4590a05eb8120b443ed2cb08b723c
  notion_url: https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c
  expected_title: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1
  lane: PR
  sequence: 35
  lifecycle: ACTIVE
  function: Execute the review-resolution and merge-readiness phase for one proceeded PR work unit.
  session_class: SAME_SESSION_CONTINUATION
  session_role: You are the same dedicated PR-development session that produced or recovered the exact PR_CANDIDATE_PUBLISHED result for one proceeded work unit.
  creator_role: The same dedicated PR-development session; PR-30 and PR-35 are two phases of one native PR execution work unit.
  reviewer_role: NONE
  inputs:
  - WORK_UNIT_ID and exact change/Epic identity
  - selected PR-35 prompt identity and direct Notion URL
  - same dedicated PR session reference with session_disposition RETAIN_EXISTING
  - original Product Owner Proceed for the exact detailed PR Plan
  - complete IA-issued PR instruction
  - immutable approved Specification and whole-change Implementation Plan with review and approved overlay lineage
  outputs:
  - artifact: PR_IMPLEMENTATION_RESULT
    states:
    - MERGE_PENDING
    - RESCOPE_PENDING
    - RECOVERY_PENDING
    - REMOTE_EVIDENCE_PENDING
    consumers:
    - RS-20
    - PR-35
  mutations:
    allowed:
    - Resolve review findings on the existing pull request for the proceeded work unit
    - Record remote actions in the durable remote-action ledger and checkpoints
    - Produce the versioned same-lineage PR_IMPLEMENTATION_RESULT phase record
    forbidden:
    - Merge a pull request or enable automatic merge
    - Edit PF10 directly
    - Add an R1 row, actor, approval, Proceed, work unit or session
    - Produce a PF10_BUILD_NOTES_ADDENDUM
  source_snapshot:
    path: candidate/prompts/PR-35.md
    sha256: 39d72456ae6080d47488508005a038e88e4555a20efa5a9c394f03726b675e51
    bytes: 17934
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: NEXT_PROMPT_HANDOFF
      rule_id: CTR-002
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 17934 bytes'
  - 'SHA-256 of that extraction: 39d72456ae6080d47488508005a038e88e4555a20efa5a9c394f03726b675e51'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - RS-20
  - PR-35
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/PR-35.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  registry_note: Added 2026-09-17. Present in the 091426.1 candidate and absent from the 091326.2 predecessor; this entry was derived from the candidate body, not carried over.
- prompt_key: PR-40
  notion_page_id: 3db4590a05eb818786c5cb6051b4d634
  notion_url: https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634
  expected_title: PR-40 — Review PR Work-Unit Lineage — 091426.1
  lane: PR
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Review PR Work-Unit Lineage for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the designated PR reviewer for the complete work unit, operating read-only.
  creator_role: the designated PR reviewer for the complete work unit, operating read-only.
  reviewer_role: NONE
  inputs:
  - 'The sole substantive review input is the complete native package containing:

    - PR_INSTRUCTION_ID and complete PR_INSTRUCTION.'
  outputs:
  - artifact: PR_WORK_UNIT_LINEAGE_REVIEW
    states:
    - ACCEPT
    - REJECT
    - PENDING
    consumers: &id038
    - DOC-20
    - QA-10
    - PR-30
    - PR-10
    - RS-10
    - RS-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 54974 bytes'
  - 'SHA-256 of that extraction: 9350d497844631345b0ab851f457554a97e4a308aad522b644995a7ea99de3f5'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id038
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/PR-40.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/PR-40.md
    sha256: 9350d497844631345b0ab851f457554a97e4a308aad522b644995a7ea99de3f5
    bytes: 54974
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: PR-50
  notion_page_id: 3db4590a05eb8138ac99c13cf6f2f282
  notion_url: https://app.notion.com/p/3db4590a05eb8138ac99c13cf6f2f282
  expected_title: PR-50 — Abort PR and Escalate — 091426.1
  lane: PR
  sequence: 50
  lifecycle: ACTIVE
  function: Execute Abort PR and Escalate for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are acting only on Nathan / Product Owner's direct manual invocation.
  creator_role: acting only on Nathan / Product Owner's direct manual invocation.
  reviewer_role: NONE
  inputs:
  - Require Nathan's direct manual invocation, exact change/work unit, PR/session/workspace/worktree/branch/head, original Proceed, immutable
    base and applicable overlays, failure/recovery evidence, completed work, reviews/CI, artifacts, constraints and the reason continuation is
    unrecoverable.
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 7257 bytes'
  - 'SHA-256 of that extraction: 4c08399c9300b7bf85e007f0512954895a523db9d61a348e333e98241c7b2d8d'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id039
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/PR-50.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/PR-50.md
    sha256: 4c08399c9300b7bf85e007f0512954895a523db9d61a348e333e98241c7b2d8d
    bytes: 7257
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-10
  notion_page_id: 3db4590a05eb818bad2fcb4bc2610b29
  notion_url: https://app.notion.com/p/3db4590a05eb818bad2fcb4bc2610b29
  expected_title: QA-10 — Audit Implementation and Establish QA Readiness — 091426.1
  lane: QA
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Audit Implementation and Establish QA Readiness for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are Isis, the continuing Lead Developer and whole-change readiness decision owner for the exact supplied change.
  creator_role: Isis, the continuing Lead Developer and whole-change readiness decision owner for the exact supplied change.
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
  - REMEDIATION_PLAN_ID
  - REMEDIATION_PLAN_REVIEW_ID
  - ORIGINATING_FINDING_REF
  outputs:
  - artifact: REALITY_AUDIT / CHANGE_AUDIT_TRIAGE / QA_READINESS
    states:
    - READY_FOR_QA
    - NOT_READY
    - ASSESSMENT_INCOMPLETE
    consumers: &id040
    - QA-20
    - ESC-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 83229 bytes'
  - 'SHA-256 of that extraction: af8f7fa69427a843bd1a8c3c303cf0b2f1a3ceba890d4338d4687b91c4250ca7'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id040
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-10.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-10.md
    sha256: af8f7fa69427a843bd1a8c3c303cf0b2f1a3ceba890d4338d4687b91c4250ca7
    bytes: 83229
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-100
  notion_page_id: 3db4590a05eb811a8d13c0bbbf77a848
  notion_url: https://app.notion.com/p/3db4590a05eb811a8d13c0bbbf77a848
  expected_title: QA-100 — Execute Bounded QA Task — 091426.1
  lane: QA
  sequence: 100
  lifecycle: ACTIVE
  function: Execute Execute Bounded QA Task for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the authorized environment or DevOps operator, not Kronos acting as the executor.
  creator_role: the authorized environment or DevOps operator, not Kronos acting as the executor.
  reviewer_role: NONE
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
    - COMPLETE
    - PARTIAL
    - BLOCKED
    - FAILED
    - NOT_EXECUTED
    consumers: &id041
    - QA-110
    - QA-90
    - QA-80
    - QA-70
  mutations:
    allowed:
    - Execute only the bounded QA_TASK actions
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 13449 bytes'
  - 'SHA-256 of that extraction: baaa8505fc4f0ba58f97c554d948ce11cf8e35204d95dbc200f7637b69fc77ba'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id041
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-100.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-100.md
    sha256: baaa8505fc4f0ba58f97c554d948ce11cf8e35204d95dbc200f7637b69fc77ba
    bytes: 13449
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-110
  notion_page_id: 3db4590a05eb816984d1d34da0e08f40
  notion_url: https://app.notion.com/p/3db4590a05eb816984d1d34da0e08f40
  expected_title: QA-110 — Review QA Evidence and Route the Next Action — 091426.1
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
    - QA-120
    - QA-90
    - QA-100
    - ESC-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 14371 bytes'
  - 'SHA-256 of that extraction: 92afcc89e220af90c5f26bcf556771741468de84b8cfa707705bf4a26189d197'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id042
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-110.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-110.md
    sha256: 92afcc89e220af90c5f26bcf556771741468de84b8cfa707705bf4a26189d197
    bytes: 14371
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-120
  notion_page_id: 3db4590a05eb81589d21e798cf38e8ba
  notion_url: https://app.notion.com/p/3db4590a05eb81589d21e798cf38e8ba
  expected_title: QA-120 — Create Final QA Report and RCA — 091426.1
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
  - QA_GUIDE_ID
  - QA_AUDIT_ID
  - REALITY_AUDIT_ID
  - CHANGE_AUDIT_TRIAGE_ID
  - QA_READINESS_ID
  outputs:
  - artifact: QA_REPORT / QA_RCA / QA_INTERIM_STATUS
    states:
    - PASS
    - FAIL
    - INTERIM
    consumers: &id043
    - CL-C-10
    - QA-110
    - QA-90
    - ESC-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 13751 bytes'
  - 'SHA-256 of that extraction: 58d9bf66480b7fc07cd057bdef2881dcd031b1cfab8287ea78441226a92ccc48'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id043
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-120.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-120.md
    sha256: 58d9bf66480b7fc07cd057bdef2881dcd031b1cfab8287ea78441226a92ccc48
    bytes: 13751
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-20
  notion_page_id: 3db4590a05eb816daa3adff37283482b
  notion_url: https://app.notion.com/p/3db4590a05eb816daa3adff37283482b
  expected_title: QA-20 — Create Live QA Guide — 091426.1
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
    - GUIDE_READY
    - BLOCKED
    consumers: &id044
    - QA-50
    - QA-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 13460 bytes'
  - 'SHA-256 of that extraction: 8935c48a7be1331c3bf726afffdaa7923bd01b3ea544f14769deaf3af77db4ec'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id044
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-20.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-20.md
    sha256: 8935c48a7be1331c3bf726afffdaa7923bd01b3ea544f14769deaf3af77db4ec
    bytes: 13460
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-50
  notion_page_id: 3db4590a05eb81a3ac91f602bad8cfa2
  notion_url: https://app.notion.com/p/3db4590a05eb81a3ac91f602bad8cfa2
  expected_title: QA-50 — Create Whole-Change QA Audit and Plan — 091426.1
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
    - PLAN_PENDING
    - BLOCKED
    consumers: &id045
    - QA-70
    - QA-80
    - QA-60
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 16482 bytes'
  - 'SHA-256 of that extraction: 438a56d57746acfe41c39a0a6354fcc8db2a1ea521ad05ac4ec13890682e5014'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id045
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-50.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-50.md
    sha256: 438a56d57746acfe41c39a0a6354fcc8db2a1ea521ad05ac4ec13890682e5014
    bytes: 16482
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-60
  notion_page_id: 3db4590a05eb810b8aa3e1692830d4b8
  notion_url: https://app.notion.com/p/3db4590a05eb810b8aa3e1692830d4b8
  expected_title: QA-60 — Create Whole-Change QA Plan — 091426.1
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
    - PLAN_PENDING
    - BLOCKED
    consumers: &id046
    - QA-70
    - QA-80
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 14201 bytes'
  - 'SHA-256 of that extraction: 7b783e2638b7cc8818a8b2f2fa465360f2e9bc9ec2aefb361f148eb126bcd12d'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id046
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-60.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-60.md
    sha256: 7b783e2638b7cc8818a8b2f2fa465360f2e9bc9ec2aefb361f148eb126bcd12d
    bytes: 14201
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-70
  notion_page_id: 3db4590a05eb8143bf26d1459fbbcad7
  notion_url: https://app.notion.com/p/3db4590a05eb8143bf26d1459fbbcad7
  expected_title: QA-70 — Review Whole-Change QA Plan — 091426.1
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
    - QA-90
    - QA-80
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 14302 bytes'
  - 'SHA-256 of that extraction: 338b991180b96858170988db5043d297163d7353f526b0091e3036964d8cd6cc'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id047
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-70.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-70.md
    sha256: 338b991180b96858170988db5043d297163d7353f526b0091e3036964d8cd6cc
    bytes: 14302
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-80
  notion_page_id: 3db4590a05eb813ba9a9dbd9a641d36c
  notion_url: https://app.notion.com/p/3db4590a05eb813ba9a9dbd9a641d36c
  expected_title: QA-80 — Revise Whole-Change QA Plan — 091426.1
  lane: QA
  sequence: 80
  lifecycle: ACTIVE
  function: Execute Revise Whole-Change QA Plan for the exact supplied change.
  session_class: ROLE_CONTINUING
  session_role: You are the same Kronos who authored the Plan.
  creator_role: the same Kronos who authored the Plan.
  reviewer_role: Isis / Lead Developer
  inputs:
  - Require one complete pending initial QA Plan plus the exact QA-70 denial/redline for that version, or an interrupted preapproval recovery
    package with the same Kronos author and Isis reviewer.
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 10205 bytes'
  - 'SHA-256 of that extraction: 7fea018710fd4eabf260a90faf5693153f16696122d4e7cde2cedf35fa3d8178'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id048
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-80.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-80.md
    sha256: 7fea018710fd4eabf260a90faf5693153f16696122d4e7cde2cedf35fa3d8178
    bytes: 10205
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: QA-90
  notion_page_id: 3db4590a05eb811e8582cf30238c5b9c
  notion_url: https://app.notion.com/p/3db4590a05eb811e8582cf30238c5b9c
  expected_title: QA-90 — Create Bounded QA Execution Task — 091426.1
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
    - TASK_READY
    - ESCALATION_REQUIRED
    - NOT_EXECUTED
    consumers: &id049
    - QA-100
    - QA-110
    - QA-80
    - QA-70
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 13982 bytes'
  - 'SHA-256 of that extraction: 83cdc85066147308327b9c57adceb11d1b6de5405fadd5a5de488f91f15ad517'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id049
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/QA-90.md
  expected_parent_id: 3c74590a05eb8149905fd694f6d2901a
  expected_parent_title: HDE QA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/QA-90.md
    sha256: 83cdc85066147308327b9c57adceb11d1b6de5405fadd5a5de488f91f15ad517
    bytes: 13982
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: RS-10
  notion_page_id: 3db4590a05eb811ca0cdc66e0d508ac4
  notion_url: https://app.notion.com/p/3db4590a05eb811ca0cdc66e0d508ac4
  expected_title: RS-10 — Create Bounded Work-Unit Rescope Proposal — 091426.1
  lane: RS
  sequence: 10
  lifecycle: ACTIVE
  function: Execute Create Bounded Work-Unit Rescope Proposal for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are Sekhmet or the explicitly assigned finding author, with no approval authority.
  creator_role: Sekhmet or the explicitly assigned finding author, with no approval authority.
  reviewer_role: Whole-change Implementation Agent
  inputs:
  - Supply the exact CHANGE_CLASS, CHANGE_ID and work-unit/finding identity; approved Specification and immutable approved Plan/review; current
    PF10 Markdown and applicable addenda; actual originating stage, owner/session, suspended boundary and read-only finding evidence; existing
    draft/result and any prior proposal/review.
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 12819 bytes'
  - 'SHA-256 of that extraction: ef6b73601ce867e02d291358877abbe2446bfccf6136916bd65bdb0a0bd13e33'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id050
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/RS-10.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/RS-10.md
    sha256: ef6b73601ce867e02d291358877abbe2446bfccf6136916bd65bdb0a0bd13e33
    bytes: 12819
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: RS-20
  notion_page_id: 3db4590a05eb81c183aac2ecb40b1497
  notion_url: https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497
  expected_title: RS-20 — Review Bounded Work-Unit Rescope — 091426.1
  lane: RS
  sequence: 20
  lifecycle: ACTIVE
  function: Execute Review Bounded Work-Unit Rescope for the exact supplied change.
  session_class: CHANGE_LIFETIME
  session_role: You are the continuing whole-change Implementation Agent (IA).
  creator_role: the continuing whole-change Implementation Agent (IA).
  reviewer_role: NONE
  inputs:
  - 'Supply exactly one complete read-back rescope artifact: a RESCOPE_REQUEST produced by PR-30 or revised by RS-30, or a RESCOPE_PROPOSAL produced
    by RS-10 or revised by RS-30.'
  outputs:
  - artifact: RESCOPE_REVIEW
    states:
    - APPROVE
    - REJECT
    - REVISION_REQUIRED
    - SPECIFICATION_CHANGE_REQUIRED
    - IN_SCOPE_REPAIR
    consumers: &id051
    - RS-40
    - PR-30
    - RS-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-17: 15709 bytes'
  - 'SHA-256 of that extraction: 4736d703b0b34e4767572b61ff50ae67bd2f8660b23b53fb2b93bce84f10f251'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id051
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/RS-20.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/RS-20.md
    sha256: 4736d703b0b34e4767572b61ff50ae67bd2f8660b23b53fb2b93bce84f10f251
    bytes: 15709
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: RS-30
  notion_page_id: 3db4590a05eb81ed9fd3d2ef439ceaaf
  notion_url: https://app.notion.com/p/3db4590a05eb81ed9fd3d2ef439ceaaf
  expected_title: RS-30 — Revise Bounded Work-Unit Rescope Proposal — 091426.1
  lane: RS
  sequence: 30
  lifecycle: ACTIVE
  function: Execute Revise Bounded Work-Unit Rescope Proposal for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the same Sekhmet or explicitly assigned rescope-artifact author.
  creator_role: the same Sekhmet or explicitly assigned rescope-artifact author.
  reviewer_role: Whole-change Implementation Agent
  inputs:
  - 'Supply exactly one RESCOPE_REQUEST_ID or RESCOPE_PROPOSAL_ID and the actual correction authority: either its RS-20 REVISION_REQUIRED review
    or Nathan''s exact Product Owner correction.'
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 12001 bytes'
  - 'SHA-256 of that extraction: 347ee4e749843fe50420bcecce47fc1049c303178a45a8e114886beddfa4961f'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id052
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/RS-30.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/RS-30.md
    sha256: 347ee4e749843fe50420bcecce47fc1049c303178a45a8e114886beddfa4961f
    bytes: 12001
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: RS-40
  notion_page_id: 3db4590a05eb8183b5ffdf4270133226
  notion_url: https://app.notion.com/p/3db4590a05eb8183b5ffdf4270133226
  expected_title: RS-40 — Approved Rescope — Resume PR Implementation — 091426.1
  lane: RS
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Approved Rescope — Resume PR Implementation for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: You are the same dedicated PR engineering session for the exact suspended work unit.
  creator_role: the same dedicated PR engineering session for the exact suspended work unit.
  reviewer_role: NONE
  inputs:
  - RESCOPE_REVIEW
  outputs:
  - artifact: PR_IMPLEMENTATION_RESULT
    states:
    - MERGE_PENDING
    - RESCOPE_PENDING
    - RECOVERY_PENDING
    - PRODUCT_OWNER_DECISION_REQUIRED
    consumers: &id053
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 8858 bytes'
  - 'SHA-256 of that extraction: 1bbcfadf8193f22fc11ffb3cb501f49ebdc5669879dd826893927add52d37a11'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id053
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/RS-40.md
  expected_parent_id: 3c74590a05eb81f2953de712f2adb6fa
  expected_parent_title: HDE IA
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/RS-40.md
    sha256: 1bbcfadf8193f22fc11ffb3cb501f49ebdc5669879dd826893927add52d37a11
    bytes: 8858
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
- prompt_key: UTIL-10
  notion_page_id: 3db4590a05eb81b89fbaf4b31a3ed2a9
  notion_url: https://app.notion.com/p/3db4590a05eb81b89fbaf4b31a3ed2a9
  expected_title: UTIL-10 — Apply Exact Redline to a Complete Artifact — 091426.1
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
  - 'Complete prompt body extracted from Notion 2026-09-17: 6653 bytes'
  - 'SHA-256 of that extraction: 9be2271229c5988b58f15f817b019147c73f834326aa021118d384f4ef6bf382'
  - 'Extraction, not a canonical publication receipt; the Notion page is authority'
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: *id054
  controlling_sources:
  - GCFPE-20260914.1
  - '091426.1'
  - candidate/prompts/UTIL-10.md
  expected_parent_id: 3c74590a05eb8176baf8cb59f1631f3c
  expected_parent_title: HDE TW
  supersedes: []
  superseded_by: null
  source_snapshot:
    path: candidate/prompts/UTIL-10.md
    sha256: 9be2271229c5988b58f15f817b019147c73f834326aa021118d384f4ef6bf382
    bytes: 6653
    completeness: COMPLETE
    extracted_as_of: '2026-09-17'
    representation: NOTION_BODY_EXTRACTION_NOT_A_PUBLICATION_RECEIPT
  audit_assertions:
    required_literals:
    - value: 'Prompt Version: 091426.1'
      rule_id: SRC-001
    - value: 'Ecosystem release: GCFPE-20260914.1'
      rule_id: INV-003
    - value: select only the controlled Markdown lane
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex: []
    forbidden_regex: []
global_literals:
  approval_request: ASK OK?
  approved: ASK OK.
audit_contracts:
  selected_binding:
    release: GCFPE-20260914.1
    version_family: '091426.1'
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
