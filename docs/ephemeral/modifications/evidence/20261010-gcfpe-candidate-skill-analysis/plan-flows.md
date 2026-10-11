# Planned repair flows — 2026-10-11

These diagrams describe the proposed repairs and their remaining gates. They do not claim execution or replace the approved graph. The original analysis diagrams remain historical evidence.

## Repair and review boundary

```mermaid
flowchart TD
  A["PLAN authorized"] --> B{"Required sources and commands available?"}
  B -->|No: current state| C["Record stopped PLAN; request sources"]
  B -->|Yes| D["Dated successor and normal-path dry run"]
  D --> E["Bounded independent PLAN review"]
  E --> F{"Nathan approves EXECUTE?"}
  F -->|No| G["Keep repair freeze"]
  F -->|Yes| H["Native and contract repairs"]
  H --> I{"Checks and package review pass?"}
  I -->|Yes| J["Nathan merge and install; verify identities"]
  I -->|Failure after external write| K["Failure record and read-only sweep"]
  K --> L["Keep freeze; Nathan restores page history"]
```

All three packages share one delivery cycle across PART-01/02. Success here does not promote the candidate; full qualification still has F01/F06/F08 and source dependencies.

## Standalone Plan delta and qualifying continuation

```mermaid
flowchart TD
  A["Approved Plan and factual finding"] --> B["IA-30 assessment"]
  B -->|Justified bounded correction| C["IA-40 standalone delta"]
  B -->|Unsupported or unresolved choice| D["Native terminal return"]
  C --> E["IA-30 delta review"]
  E -->|DELTA_DENY| C
  E -->|DELTA_APPROVE| F["Save decision and one numbered addendum"]
  F --> G{"Exact receiver and intake resolved?"}
  G -->|Yes| H["One human-pasted native handoff"]
  G -->|No| I["Source or authority stop to Nathan"]
  H --> J["Receiver reads current PF10 and continues"]
```

The approved Plan remains unchanged throughout. CF-C-30/CF-E-30 qualifying approvals use the same final continuation rule, with their own native Specification review. The producer never runs the receiver or verifies Nathan's PF10 paste. QA-80 is not inferred to share IA-40's delta-authoring mode.

## RS-20 return by actual lifecycle stage

```mermaid
flowchart TD
  A["Independent IA decision at RS-20"] --> B{"Decision"}
  B -->|APPROVE| C["One qualifying numbered addendum"]
  B -->|REJECT or IN_SCOPE_REPAIR| D["No addendum; unchanged authority"]
  C --> E{"Recorded origin"}
  D --> E
  E -->|PR-20 before Proceed| F["PR-20 planning return; no future vehicle fields"]
  E -->|PR-30 or PR-35| G["Preserve existing execution-phase routes"]
  E -->|Lawful non-PR origin| H["Actual native owner return"]
  B -->|REVISION_REQUIRED| I["RS-30 to same proposal author"]
  B -->|SPECIFICATION_CHANGE_REQUIRED| J["Terminal Product Owner decision"]
```

For APPROVE, proceeded PR-30 prepublication returns directly to PR-30; actual open-PR PR-30/PR-35 phases use RS-40. REJECT/IN_SCOPE_REPAIR preserve their direct existing-owner routes. The three execution-phase enum values stay unchanged. This diagram does not invent a PR owner for a non-PR finding.
