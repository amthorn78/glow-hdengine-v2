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
workspace_skill_registry_disposition: 'Evidence only. That registry is DRAFT, unapproved, and
  self-classified INVENTORY_EVIDENCE_NOT_APPROVED_EXPECTED_STATE, observed from a checkout absent
  from this environment. It confers no skill lifecycle on this approved registry. Its glow-hde-devops
  row is a dated observation and is preserved unedited; that skill is retired by D16, which is the
  authority for its disposition, and the forbidden literal on all 55 rows below is correct.'
authority_sources:
- type: SELECTED_RELEASE_REGISTER
  release: GCFPE-20260914.1
  url: https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1
- type: SELECTED_CATALOG
  version_family: '091426.1'
  member_count: 55
  url: https://app.notion.com/p/3db4590a05eb81738ef1d846e3c0df8c
  correction: 'Until 2026-09-21 this row named 091426.1 and 55 members but pointed at the
    091326.2 catalog (3da4590a05eb81bcbc5deb2d2cec4f1f), which holds 54 members of a different
    release. The identifiers were right and the URL was wrong. Corrected at promotion (D17) to
    the catalog that actually carries the 55 rows this registry describes; the predecessor
    catalog is archived intact and is historical evidence only.'
- type: COMPLETE_PROMPT_FETCH_MANIFEST
  path: candidate/prompts/manifest.json
  note: 'Pre-merge extraction workspace, 2026-09-17. Historical lineage only: this path does not exist in the repository. Current prompt bodies are authored in Notion and are resolved through the candidate catalog; the evidence_contract byte count and SHA-256 on each row below are the reproducible identity.'
  disposition: HISTORICAL_LINEAGE_NOT_A_RESOLVABLE_PATH
body_extraction_convention:
  in_force: STRIP_BOTH_BOUNDARY_NEWLINES
  definition: 'The exact slice between the fetch result''s <content> and </content> markers, with
    the two boundary newlines dropped: the newline that follows <content> and the one that precedes
    </content>. The markers occupy their own lines, so a literal reading that keeps them yields a
    body two bytes larger on every prompt. This is the convention under which every
    evidence_contract byte count and SHA-256 below was produced, and the only convention under
    which they reproduce.'
  row_wording_disposition: 'All 55 rows carry the dated line "Extraction convention: the exact
    slice between the fetch result''s <content> and </content> markers, with no trailing newline
    added". That wording is incomplete in two ways: it omits the leading newline entirely, and it
    states the trailing treatment as an addition withheld rather than a byte dropped. Read
    literally it describes a different corpus from the one the recorded digests identify. Those 55
    lines are dated evidence statements and are preserved unedited under AUTH-001; this key is the
    authority for the convention in force, and each row''s recorded byte count and SHA-256 remain
    the reproducible identity.'
  evidence:
  - 'Reverse-applied edits reproduce the recorded pre-edit SHA-256 for 21 of 21 repaired bodies
    under strip-both and 0 of 21 under as-extracted, leading-only or trailing-only. Three untouched
    prompts extracted under all four variants reproduce their recorded digests only under
    strip-both: CF-C-10 41dce73a… / 7203 B, MGR-10 5c8aebc6… / 7276 B, PR-40 042255564c… /
    54043 B. Recorded in docs/ephemeral/gcfpe.prompt-body-addendum-schema.repair-report.md and
    docs/prompt_ecosystem_management/pe-succession/pe32-to-pe33.md.'
  evidence_scope: 'The evidence above is reproducible in this repository and covers 24 of the 55
    bodies: 21 repaired bodies by reverse-applied edit, and 3 untouched prompts extracted under all
    four variants. No body corpus exists on disk and prompt_bodies_validated is false, so no
    checked-in artifact exercises the remaining 31. The conclusion does not depend on them: the
    convention in force is established by 0 of 21 reproducing under any other variant, and by three
    untouched prompts reproducing only under strip-both. A claim of complete-corpus coverage is
    NOT made by this key.'
  corroboration_not_reproducible_here: 'A Product Owner-relayed human review dated 2026-09-20
    reports 55 of 55 live bodies matching on both SHA-256 and byte count under strip-both, totalling
    1,060,573 bytes across the 55 evidence_contract rows. That figure reconciles exactly with the
    sum of those rows, which is the only part of it this repository can check. The review itself is
    a relayed narrative: no report, inputs or command is checked in, so it cannot be reproduced and
    it is recorded here as corroboration, never as evidence. It is promoted to evidence only by
    landing the run — per-body digest, byte count and the extraction command — in a repository
    evidence artifact.'
  applies_to: 'The evidence_contract byte count and SHA-256 on each row below, which are the body
    identity for validation. This key does not alter, revive or reinterpret any source_snapshot
    record; those remain the 2026-09-17 pre-merge extraction that authority_sources dispositions as
    HISTORICAL_LINEAGE_NOT_A_RESOLVABLE_PATH.'
  why_it_matters: 'The convention defines the ecosystem''s tamper-evidence. The ambiguity already
    produced one silent two-byte error that no amount of agreement between independent extractions
    would have surfaced, because both extractions were wrong in the same way.'
  body_identity_disposition: 'The `evidence_contract` and `source_snapshot` identities on every row
    describe the bodies before `D23` (2026-09-23) and no longer identify them. They are not
    regenerated, because hashing bodies is prohibited (`prompt-corpus-policy.md`).'
observation:
  release: GCFPE-20260914.1
  version_family: '091426.1'
  selected_member_count: 55
  complete_body_count: 55
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
    - BLOCKED
    - KICKOFF_READY
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 7203 bytes'
  - 'SHA-256 of that extraction: 41dce73a62735927d291bd8f7342654d314d38de47070fe37f8a6c9318fd1702'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-C-20
  - CF-E-10
  - CF-PO-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    - BLOCKED
    - SPECIFICATION_PENDING
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 5888 bytes'
  - 'SHA-256 of that extraction: 4570e718530316c018b18dcb15848f061e938e268ae4ec163630b310c14c67c7'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-C-10
  - CF-C-30
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    - CORRECTION_REDLINE
    - DELTA_APPROVE
    - DELTA_DENY
    - INITIAL_APPROVE
    - INITIAL_DENY
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 9420 bytes'
  - 'SHA-256 of that extraction: b56d218a4f5d2a08f4f12af99fe097b001925dd1a1a445c2375edf4d3cd894e7'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-C-40
  - IA-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
    - CF-C-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 7518 bytes'
  - 'SHA-256 of that extraction: 9b62004b93aa3a1e93fb5cf325bb6e78ea460ed78f49c523a654be6fd5a0c95f'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-C-30
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    - BLOCKED
    - KICKOFF_READY
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 7307 bytes'
  - 'SHA-256 of that extraction: 5cdfce4d502c5b5b564b562b18e108cc38b1ffa85b3b655edd6706d0e76e80fe'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-C-10
  - CF-E-20
  - CF-PO-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    - BLOCKED
    - SPECIFICATION_PENDING
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 5900 bytes'
  - 'SHA-256 of that extraction: 5add38939d7e920b90c4031846e51f0fdb29b1bf50ec3574dcb72eaddc134108'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-E-10
  - CF-E-30
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    - CORRECTION_REDLINE
    - DELTA_APPROVE
    - DELTA_DENY
    - INITIAL_APPROVE
    - INITIAL_DENY
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 9428 bytes'
  - 'SHA-256 of that extraction: 6e92232ba58cc4e8c53004af7176ae2422863f2e1bcf1c6e209dc3a257066e76'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-E-40
  - IA-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
    - CF-E-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 7533 bytes'
  - 'SHA-256 of that extraction: e5e297ebcf0585c4114d30311535089ea16bad4ea679120a8e0e8d08050987ce'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-E-30
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 6091 bytes'
  - 'SHA-256 of that extraction: ba98c011ec3607c25618d2dfe8409c4a1f6232dbf0323812b80f551a8a277b79'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-C-10
  - CF-E-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
- prompt_key: CL-20
  notion_page_id: 3db4590a05eb81f4812be61e8877c02c
  notion_url: https://app.notion.com/p/3db4590a05eb81f4812be61e8877c02c
  expected_title: CL-20 — Prepare Closure Memo and Post-Closure Record — 091426.1
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 32573 bytes'
  - 'SHA-256 of that extraction: 6c7860c0b23210e7a4f58938b134c0f80ba1f2ec69d4c4bfe567d2b83608660e'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CL-30
  - CL-40
  - CL-E-20
  - CL-E-30
  - CL-E-40
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
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
    - CL-40
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-19: 29622 bytes'
  - 'SHA-256 of that extraction: dc0a967032467707c738c465069b0cc3c042b1b1cbcdadb3389356e1d7b7d2c1'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CL-40
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
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers: []
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-19: 29401 bytes'
  - 'SHA-256 of that extraction: a3fd6cd79929c91829672faee9c5129e3f0ca80b9eef38360a6c1f80dc898e06'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: []
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 35878 bytes'
  - 'SHA-256 of that extraction: 794b9bf3bed9278386379f898039bfde22e1831a92bdf40942fe74ca4d7b1b91'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CL-20
  - ESC-30
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 36353 bytes'
  - 'SHA-256 of that extraction: 0c2b669d5833dcfb4c60d11fe5afe3851343c2f866251bffeb8f1af952b00753'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CL-20
  - CL-E-20
  - ESC-30
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
    - CL-E-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-19: 14832 bytes'
  - 'SHA-256 of that extraction: 10698a09852b296886f36d4df4ae0250285f8b13741c122ba9fcb90f54659689'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CL-E-30
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
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 13629 bytes'
  - 'SHA-256 of that extraction: 7e1524159e9f6b00f5b4ffb8d33a90b3cd78e4115b526313322d7a0f5f8b99ae'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CL-E-20
  - CL-E-40
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
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 15457 bytes'
  - 'SHA-256 of that extraction: 582b6476d38e45bc9733c5d5d3e599281178a1a9f0cadb99aaf451dcbddd3b8c'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CL-40
  - CL-E-20
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
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 19787 bytes'
  - 'SHA-256 of that extraction: c858901a70cf0532395fda643841b9de2ea55b236b48f12bb24cac77661218ac'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - PR-20
  - RS-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - REMEDIATION_REVIEW_ID
  outputs:
  - artifact: DOCUMENTATION_COMPLETION
    states:
    - BLOCKED
    - COMPLETE
    - INCOMPLETE
    - PENDING
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 20217 bytes'
  - 'SHA-256 of that extraction: e37624c24c349aff20324721fd2c9ae3d9b23e33b7261d6e49884805fafd4194'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - DOC-10
  - PR-40
  - QA-10
  - RS-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
    - ESC-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-19: 16683 bytes'
  - 'SHA-256 of that extraction: 93b05f42c6c18c4a1bc67bac767efc36c8d84f075a90292384a7be64e7e6e75c'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-30
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - REMEDIATION_PROPOSAL_ID
  - DISCOVERY_TASK_ID
  - TRIAGE_RECEIPT_ID
  outputs:
  - artifact: DISCOVERY_RESULT
    states:
    - COMPLETE
    - PARTIAL
    - BLOCKED
    consumers:
    - ESC-30
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-19: 17279 bytes'
  - 'SHA-256 of that extraction: 7766e52f3da17ee56e3ff4b60edb2a264215503e53fa7ed286a097769c6c09e2'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-30
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - REMEDIATION_PROPOSAL_ID
  - DISCOVERY_RESULT_IDS
  - REMEDIATION_REVIEW_ID
  outputs:
  - artifact: REMEDIATION_PROPOSAL
    states:
    - REMEDIATION_PENDING
    - DISCOVERY_REQUIRED
    - BLOCKED
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 17751 bytes'
  - 'SHA-256 of that extraction: 459ed2988a3fe000e70079a02967a1f47a8644498f54fc6199586c16a428ac6a'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-25
  - ESC-40
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 17786 bytes'
  - 'SHA-256 of that extraction: 9159ec0d9b52a52a58b1cf654547f31089381c331f5d10d133c1f619cea2bd08'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-30
  - PR-30
  - PR-35
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    - ECOSYSTEM_CHANGE_COMPLETE
    - IMPLEMENTATION_BLOCKED
    - PROMOTION_CHECKPOINT_REQUIRED
    - READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION
    consumers:
    - PR-10
  mutations:
    allowed:
    - Perform only the authorized GCFPE prompt/control publication mutations
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 8015 bytes'
  - 'SHA-256 of that extraction: e5b77f9c5c9939b2234146b106360b06fe73101b6ec50459ada16b18f6d25b12'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - PR-10
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
    required_literals: null
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 10301 bytes'
  - 'SHA-256 of that extraction: 5b7980fe30e9fced15b3c88133f834236d0309dc1f8966db9d0a9430b4fe8659'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - IA-20
  - IA-30
  - IA-50
  - IA-60
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 6411 bytes'
  - 'SHA-256 of that extraction: 802ccd490feb83f6c4df3c73c325342e0202a02935579ffbf33c74feb35451be'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - IA-30
  - IA-50
  - IA-60
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    - CHANGE_NOT_SUBSTANTIATED
    - DELTA_APPROVE
    - DELTA_DENY
    - INITIAL_APPROVE
    - INITIAL_DENY
    - PLAN_DELTA_REDLINE
    - PRODUCT_OWNER_DECISION_REQUIRED
    - WRONG_NATIVE_LANE
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 9729 bytes'
  - 'SHA-256 of that extraction: a07e8933a00a4979298fabb703a0c2226aaf96eb870f1109a2c71b1252d14ebc'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - IA-40
  - PR-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - Require one complete pending initial Implementation Plan plus the exact IA-30 denial/redline for that version, or an interrupted preapproval recovery package with the same author/reviewer lineage.
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 5712 bytes'
  - 'SHA-256 of that extraction: 8c9bb2273f3e54ba8b1422a6f8d1c3bd1132497faa0ffd561038342a0c268326'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - IA-30
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 6668 bytes'
  - 'SHA-256 of that extraction: 42ce029be426cd3d745b3e9f7099439a091d3ee915c1f4c0dcd660cf5cf0afef'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - IA-10
  - IA-20
  - IA-30
  - IA-40
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - 'PLANNING_INQUIRY: exact original question/identity; actual files/interfaces and repository evidence; constraints, alternatives, failure modes, decision criteria and specific requested finding.'
  outputs:
  - artifact: PLANNING_RESEARCH_FINDING
    states:
    - RESEARCH_COMPLETE
    - PARTIAL
    - BLOCKED
    consumers:
    - IA-50
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 5633 bytes'
  - 'SHA-256 of that extraction: 5addd33093e4c794e609829bba434275f06e798d313eda8ed29d63ffdba3e8c6'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - IA-50
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - For a request only to prepare Product Owner cycle-entry launch guidance, accept known or unresolved classification and all actual intake without inventing change identity.
  outputs:
  - artifact: FLOW_PROGRESS
    states:
    - FLOW_PROGRESS
    - TERMINAL_RETURN
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 7276 bytes'
  - 'SHA-256 of that extraction: 5c8aebc68f7f7f6aa708851e0464e5793b27df158af1e37537ab450efbd86f6a'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CF-C-10
  - CF-E-10
  - CF-PO-10
  - CL-40
  - QA-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - REMEDIATION_REVIEW_ID
  outputs:
  - artifact: OPS_TASK
    states:
    - READY
    - BLOCKED
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 42826 bytes'
  - 'SHA-256 of that extraction: 4a30d7342f4a71e314b7962c2f7eb2ab6b313d9323044a1fcc8e6cbc6bc41563'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-25
  - OPS-20
  - RS-10
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
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 36912 bytes'
  - 'SHA-256 of that extraction: 429c6ccca8c1602b3457433b85f3c91f96d7c21bb4891ee921dd56decd8b2c0c'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-25
  - OPS-30
  - RS-10
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
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 57532 bytes'
  - 'SHA-256 of that extraction: 321e626fc72fb71dddf865860193b9d66fb36eae30b6a43c7d713e27443ff45f'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-25
  - OPS-10
  - RS-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - REMEDIATION_REVIEW_ID
  outputs:
  - artifact: PR_INSTRUCTION
    states:
    - INSTRUCTION_READY
    - DRAFT
    - BLOCKED
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 49351 bytes'
  - 'SHA-256 of that extraction: d1e2458c39037c9aa1dfbc3f97641e2e6b2c1dd2143447f40c142dacb6a8b623'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - PR-20
  - RS-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - PR_WORK_UNIT_LINEAGE_REVIEW with REJECT (reject_replan) and its in-scope finding, for a re-plan of the same WORK_UNIT_ID in a new dedicated session Nathan seeds
  outputs:
  - artifact: PR_IMPLEMENTATION_PLAN
    states:
    - AWAITING_PO_PROCEED
    - DRAFT
    - BLOCKED
    consumers:
    - RS-10
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 51725 bytes'
  - 'SHA-256 of that extraction: d64997b20867063089a23b42d44f6744a6537f158844e0a13f84670fd5f41110'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - RS-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    - value: 'accepts\s+a\s+`?PR_WORK_UNIT_LINEAGE_REVIEW`?\s+whose\s+result\s+is\s+`?REJECT'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    - PRODUCT_OWNER_DECISION_REQUIRED
    - PR_CANDIDATE_PUBLISHED
    - RECOVERY_PENDING
    - RESCOPE_PENDING
    consumers:
    - PR-35
    - RS-20
  mutations:
    allowed:
    - Implement, test, commit and publish the exact proceeded PR work unit; review findings and CI fixes on the published PR belong to PR-35
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-19: 39791 bytes'
  - 'SHA-256 of that extraction: 482ca2a7657058154147acf3768334dfb956246c45a400a80e6c6f0138004a9d'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - PR-35
  - RS-20
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'An\s+\*?In-flight decisions\*?\s+section'
      rule_id: CTR-002
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'they do not share a session'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
- prompt_key: PR-35
  notion_page_id: 3db4590a05eb8120b443ed2cb08b723c
  notion_url: https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c
  expected_title: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1
  lane: PR
  sequence: 35
  lifecycle: ACTIVE
  function: Execute the review-resolution and merge-readiness phase for one proceeded PR work unit.
  session_class: DEDICATED_PR_REVIEW_SESSION
  session_role: You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.
  creator_role: The dedicated PR-35 session; PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions.
  reviewer_role: NONE
  inputs:
  - WORK_UNIT_ID and exact change/Epic identity
  - selected PR-35 prompt identity and direct Notion URL
  - 'session_disposition: NEW_DEDICATED — the dedicated PR-35 session for this WORK_UNIT_ID'
  - original Product Owner Proceed for the exact detailed PR Plan
  - complete IA-issued PR instruction
  - immutable approved Specification and whole-change Implementation Plan with review and approved overlay lineage
  outputs:
  - artifact: PR_IMPLEMENTATION_RESULT
    states:
    - MERGE_OBSERVED
    - MERGE_PENDING
    - PRODUCT_OWNER_DECISION_REQUIRED
    - RECOVERY_PENDING
    - REMOTE_EVIDENCE_PENDING
    - RESCOPE_PENDING
    consumers:
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
    - Add an R1 row, actor, approval, Proceed or work unit, or any session beyond its own dedicated PR-35 session
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
    - value: NEXT_PROMPT_HANDOFF
      rule_id: CTR-002
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'An\s+\*?In-flight decisions\*?\s+section'
      rule_id: CTR-002
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'they do not share a session'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    - value: '[Ss]ubscribe to the pull request'
      rule_id: CTR-002
    - value: 'stay subscribed and do not poll'
      rule_id: CTR-002
    - value: 'The observed merge event is the fact PR-40 is entered on'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
    - value: 'launched as a new session'
      rule_id: CTR-001
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-19: 17908 bytes'
  - 'SHA-256 of that extraction: 51e8a5e85ca3b66ce755e979d0a1ac61540c7f06e58237f516f3a28148570e79'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - PR-40
  - RS-20
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
  - PR_INSTRUCTION_ID and complete PR_INSTRUCTION
  - PR_IMPLEMENTATION_PLAN_ID and complete PR_IMPLEMENTATION_PLAN
  - The complete PR-30 result with PR_CANDIDATE_PUBLISHED
  - 'The complete PR-35 result: MERGE_OBSERVED with the observed merge event, or, only where no MERGE_OBSERVED result was returned for this merge, the earlier MERGE_PENDING, which is historical pre-merge evidence.'
  - The complete ordered PR_REFS for this work unit, with each actual PR reference, commit identity, order, review/check state and merge evidence
  - CHANGE_CLASS, CHANGE_ID, WORK_UNIT_ID, approved Specification, Implementation Audit, Plan, Plan review, dependency and acceptance/evidence lineage
  - Existing PR reviewer/session lineage for a rereview, the PR-30 and PR-35 session identities, the whole-change IA context and exact return owner
  - CANON_CONFLICT_REGISTER, recovery state, truthful pending, NOT PRODUCED and NOT EXECUTED values, and all actual access limitations
  - PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it.
  outputs:
  - artifact: PR_WORK_UNIT_LINEAGE_REVIEW
    states:
    - ACCEPT
    - REJECT
    - PENDING
    consumers:
    - PR-10
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 54043 bytes'
  - 'SHA-256 of that extraction: 042255564c9916c4a933f0986ad8f98e36a495bdf1e35a956cdc0704a87991dc'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - PR-10
  - PR-20
  - RS-10
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    - value: 'PR-40 is entered on the observed merge event'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
    - value: 'original Proceed and a suitable actual authorized implementation vehicle'
      rule_id: CTR-001
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
  - Require Nathan's direct manual invocation, exact change/work unit, PR/session/workspace/worktree/branch/head, original Proceed, immutable base and applicable overlays, failure/recovery evidence, completed work, reviews/CI, artifacts, constraints and the reason continuation is unrecoverable.
  outputs:
  - artifact: PR_ABORT_ESCALATION_RECORD
    states:
    - PR_ABORTED_ESCALATED
    consumers: []
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 6887 bytes'
  - 'SHA-256 of that extraction: ac910fe9e1374a4206179c58b8fba187b6c0e62e66e9c0cc1ffab85de93a91c8'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: []
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
    - value: controlled Markdown
      rule_id: CTR-002
    - value: PF10
      rule_id: CTR-002
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - REMEDIATION_PROPOSAL_ID
  - REMEDIATION_REVIEW_ID
  - ORIGINATING_FINDING_REF
  outputs:
  - artifact: REALITY_AUDIT / CHANGE_AUDIT_TRIAGE / QA_READINESS
    states:
    - READY_FOR_QA
    - NOT_READY
    - ASSESSMENT_INCOMPLETE
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 82485 bytes'
  - 'SHA-256 of that extraction: 9aeaeff42ad12f44f0e6036e922cb14c9da16457128a07159a8ee4331b152b99'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-30
  - QA-20
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'Notion and repository persistence'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
    - QA-110
  mutations:
    allowed:
    - Execute only the bounded QA_TASK actions
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-19: 13317 bytes'
  - 'SHA-256 of that extraction: 373907a43557e87e46892fb35c683228a779765fb388cfff9dc98389d0c3fb7c'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - QA-110
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 14305 bytes'
  - 'SHA-256 of that extraction: 698c44f0c57d7294eed8a9a34049ee729b4a334eda81d6da0da8ad2dfb287718'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-10
  - QA-100
  - QA-120
  - QA-90
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - LIVE_QA_GUIDE_ID
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 13731 bytes'
  - 'SHA-256 of that extraction: 94d6abb95dc8c637f91e2cb16d5a68323addc416bb961cef32c27477fb6a53d4'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - CL-C-10
  - CL-E-10
  - ESC-10
  - QA-110
  - QA-90
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 13217 bytes'
  - 'SHA-256 of that extraction: 927b57745409bb99c4a83013a84f86ba7a375f2811b03d5a8beb46dcaba453a2'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - QA-10
  - QA-50
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 16351 bytes'
  - 'SHA-256 of that extraction: 6fee14353c20e21d8ae1d38df31d3be2fc93a73161606fc17a7e45bd385881ff'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - QA-60
  - QA-70
  - QA-80
  - QA-90
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 14012 bytes'
  - 'SHA-256 of that extraction: f523e6354696e5ba637181f1ad7f1b60b54f11bb421ea39ac55cf7b9ede965a3'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - QA-70
  - QA-80
  - QA-90
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: '`ASK OK\?` is the line immediately before the block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\bends? `ASK OK\?`'
      rule_id: CTR-002
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 14014 bytes'
  - 'SHA-256 of that extraction: ed4ee3adca15bf2a3e91525eca413d6aba0d2ef1819ce81640f9b4cbd2505881'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - QA-80
  - QA-90
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: never a gate on later work
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - Require one complete pending initial QA Plan plus the exact QA-70 denial/redline for that version, or an interrupted preapproval recovery package with the same Kronos author and Isis reviewer.
  outputs:
  - artifact: QA_PLAN
    states:
    - PLAN_PENDING_REVISED
    - WRONG_ROUTE_APPROVED_BASE
    consumers:
    - QA-70
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 10163 bytes'
  - 'SHA-256 of that extraction: 3c0080857a39aa14cf8e8e93f80674858e906a5e30e58d44dfdc944abfa8a02d'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - QA-70
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: '`ASK OK\?` is the line immediately before the block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\bends? `ASK OK\?`'
      rule_id: CTR-002
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-18: 13892 bytes'
  - 'SHA-256 of that extraction: b77124fc789087f297fb668547617c3d6d82f3b0e4c8fcaff93686684c62d097'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - ESC-10
  - QA-100
  - QA-110
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - Supply the exact CHANGE_CLASS, CHANGE_ID and work-unit/finding identity; approved Specification and immutable approved Plan/review; current PF10 Markdown and applicable addenda; actual originating stage, owner/session, suspended boundary and read-only finding evidence; existing draft/result and any prior proposal/review.
  outputs:
  - artifact: RESCOPE_PROPOSAL
    states:
    - RESCOPE_PROPOSAL_PENDING_REVIEW
    consumers:
    - RS-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 12732 bytes'
  - 'SHA-256 of that extraction: 93905c67c008c31d829ad1cf3b3b621ff699a84228df61cb2268a6d0cbfc83c1'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - RS-20
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: '`ASK OK\?` is the line immediately before the block\.'
      rule_id: TOP-001
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\bends? `ASK OK\?`'
      rule_id: CTR-002
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - 'Supply exactly one complete read-back rescope artifact: a RESCOPE_REQUEST produced by PR-30 or revised by RS-30, or a RESCOPE_PROPOSAL produced by RS-10 or revised by RS-30.'
  outputs:
  - artifact: RESCOPE_REVIEW
    states:
    - APPROVE
    - REJECT
    - REVISION_REQUIRED
    - SPECIFICATION_CHANGE_REQUIRED
    - IN_SCOPE_REPAIR
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 14818 bytes'
  - 'SHA-256 of that extraction: e6ccd013f8b390fc39069bbd3f87508cf630d3c1d267fda5feada00184ec5659'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - PR-30
  - PR-35
  - RS-30
  - RS-40
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
  - 'Supply exactly one RESCOPE_REQUEST_ID or RESCOPE_PROPOSAL_ID and the actual correction authority: either its RS-20 REVISION_REQUIRED review or Nathan''s exact Product Owner correction.'
  outputs:
  - artifact: RESCOPE_REQUEST / RESCOPE_PROPOSAL
    states:
    - RESCOPE_PROPOSAL_PENDING_REVIEW
    consumers:
    - RS-20
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 12113 bytes'
  - 'SHA-256 of that extraction: 4c5f96f002762200a18fc8eff864d85157ef5d12487e6b044adc51e3fef5641a'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - RS-20
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: '`ASK OK\?` is the line immediately before the block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\bends? `ASK OK\?`'
      rule_id: CTR-002
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
- prompt_key: RS-40
  notion_page_id: 3db4590a05eb8183b5ffdf4270133226
  notion_url: https://app.notion.com/p/3db4590a05eb8183b5ffdf4270133226
  expected_title: RS-40 — Approved Rescope — Resume PR Implementation — 091426.1
  lane: RS
  sequence: 40
  lifecycle: ACTIVE
  function: Execute Approved Rescope — Resume PR Implementation for the exact supplied change.
  session_class: DEDICATED_ONE_OFF
  session_role: 'You resume the recorded phase in its own dedicated session: PR-30''s session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35.'
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
    consumers:
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
  - 'Complete prompt body extracted from Notion 2026-09-19: 8233 bytes'
  - 'SHA-256 of that extraction: ddef768be169c6eb41660433ff7557d72b3ebc5dd3ba8f617bdeb113b4732630'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces:
  - PR-30
  - PR-35
  - PR-40
  - RS-20
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: never a gate on later work
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'An\s+\*?In-flight decisions\*?\s+section'
      rule_id: CTR-002
    - value: 'they do not share a session'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    - value: '[Ss]ubscribe to the pull request'
      rule_id: CTR-002
    - value: 'stay subscribed and do not poll'
      rule_id: CTR-002
    - value: 'The observed merge event is the fact PR-40 is entered on'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
    - value: 'launched as a new session'
      rule_id: CTR-001
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
    - ALREADY_APPLIED
    - COMPLETE
    - INCOMPLETE
    consumers: []
  mutations:
    allowed:
    - Produce and save the prompt-defined governed result artifact(s)
    forbidden:
    - Edit PF10 directly
    - Merge a pull request or enable automatic merge
    - Automatically invoke PR-50
  evidence_contract:
  - 'Complete prompt body extracted from Notion 2026-09-18: 6934 bytes'
  - 'SHA-256 of that extraction: 9234ff70454e2cd12f2d98e40a9ce103f9a27c87d51e7ded78aae5352cd96de4'
  - 'Extraction convention: the exact slice between the fetch result''s <content> and </content> markers, with no trailing newline added'
  - Extraction, not a canonical publication receipt; the Notion page is authority
  failure_contract:
  - Return truthful blocked/incomplete state to the exact source, authority, or recovery owner; do not invent missing evidence.
  required_interfaces: []
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
    - value: PF10
      rule_id: CTR-002
    - value: NEXT_PROMPT_HANDOFF
      rule_id: TOP-001
    forbidden_literals: []
    required_regex:
    - value: docs/pfcanon/
      rule_id: CTR-002
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
    forbidden_regex:
    - value: 'addendum_id[\s\S]{0,400}?artifact_version'
      rule_id: CTR-001
    - value: Glow / Core Docs / PFCanon
      rule_id: CTR-001
    - value: Glow / Ephemeral Planning Files
      rule_id: CTR-001
    - value: drive\.google\.com
      rule_id: CTR-001
    - value: EPHEMERAL_DRIVE
      rule_id: CTR-001
    - value: off-repositor
      rule_id: SRC-001
    - value: state the mismatch
      rule_id: CTR-002
    - value: '[Cc]ompare the current PF10'
      rule_id: CTR-002
    - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS
      rule_id: INV-003
    - value: (?<![.\w/-])glow-hde-devops(?![\w-])
      rule_id: SRC-001
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
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
