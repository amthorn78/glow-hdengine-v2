# Candidate flow review

These diagrams describe the reviewed candidate's declared behavior and current rulings. They are analysis aids, not replacement graph parts, release selection, observed execution or permission to launch sessions. Known disagreements are identified below. Nathan starts top-level sessions by pasting handoffs; task workers may assist within them.

## Delivery and plan-driven progression

```mermaid
flowchart TD
    S["Approved Specification"] --> I["IA: approved whole-change Plan"]
    I --> U{"Next dependency-ready unit"}
    U --> PI["PR-10: instructions"]
    PI --> P["PR-20: plan"]
    P --> A["Nathan: Proceed for this plan"]
    A --> B["PR-30: implement and publish"]
    B --> R["PR-35: review and correct"]
    R --> M["Nathan: merge"]
    M --> V["PR-40: verify landed work"]
    V -->|"ACCEPT: resolve actual Plan"| U
    V -->|"REJECT: implementation defect"| P
    V -->|"REJECT: instruction defect"| PI
    U --> O["OPS-10 task; OPS-20 execution"]
    O --> OR["OPS-30: review evidence"]
    OR --> U
    U --> D["DOC-10: final documentation instructions"]
    D --> P
    V -->|"Accepted documentation unit"| DR["DOC-20: verify completion"]
    DR --> U
    U -->|"All delivery and documentation complete"| Q["QA-10: whole-change readiness"]
    U -->|"No executable next stage"| H["Preserve accepted work; name actual owner"]
```

PR-40 never invents another unit or another Proceed. Its five named ACCEPT receivers are PR-10, OPS-10, DOC-10, DOC-20 and QA-10; an unresolved dependency preserves ACCEPT. An instruction defect returns to PR-10; an implementation defect returns to PR-20. A merge observation and the fallback merge assertion are alternative entries to one PR-40 invocation, never two.

## PR rescope and phase-specific return

```mermaid
flowchart TD
    F["Material boundary in the PR work unit"] --> A["PR author: bounded request or revision"]
    A --> I["RS-20: independent whole-change IA review"]
    I -->|"REVISION_REQUIRED"| R["RS-30: same author revises"]
    R --> A
    I -->|"APPROVE"| P{"Originating phase"}
    P -->|"Before Proceed"| PP["PR-20: planning continues"]
    P -->|"PR-30 before publication"| PI["PR-30: direct continuation"]
    P -->|"Actual open PR"| RS["RS-40: resume PR-30 or PR-35"]
    I -->|"REJECT or IN_SCOPE_REPAIR"| N["Existing repair owner"]
    I -->|"Specification boundary"| PO["Nathan: native product decision"]
```

RS-10 is optional author support. The PR author prepares the proposal; IA reviews it; Isis is not inserted into rescope. Only an actual open-PR phase uses RS-40. The original work unit, plan, Proceed, PR and evidence lineage remain bound; role/name and artifacts let the receiving side recover its session. Two dedicated PR-30 and PR-35 phase sessions and reviewer independence remain required. A non-PR finding with no lawful PR author returns to its actual owner or Nathan instead of inventing one.

The pre-Proceed arrow follows RS-20's current native instruction. Its candidate graph still has no matching PR-20 return: the dynamic branch is restricted to a non-PR origin. F09 records this disagreement; the diagram does not claim the graph already implements that arrow.

The general Specification/Plan delta lane is distinct from PR rescope. CF-C-30, CF-E-30 and IA-30 currently call qualifying approval terminal, while their candidate graph parts declare one native continuation. That disagreement is a finding, not a new terminal route adopted by these diagrams.

## QA, evidence return and closure

```mermaid
flowchart TD
    R["QA-10: READY_FOR_QA"] --> G["QA-20: Live QA Guide"]
    G --> P["QA-50: Kronos audit and Plan"]
    P --> A["QA-70: Isis reviews Plan"]
    A -->|"Preapproval revision"| V["QA-80: Kronos revises"]
    V --> A
    A -->|"Approved steps selected"| T["QA-90: Kronos authors tasks"]
    T --> E["QA-100: PO-chosen execution; store and index evidence"]
    E -->|"Every result state"| C["QA-110: review exact returned evidence"]
    C -->|"Authorized task or bounded rerun needed"| T
    C -->|"Ready existing task or missing execution evidence"| E
    C -->|"Missing registration only"| O["Evidence owner: index existing valid results"]
    O --> C
    C -->|"Escalation needed"| X["Native escalation and remediation"]
    C -->|"Complete required run"| F["QA-120: report and RCA"]
    F --> L["CL-C-10 or CL-E-10: Isis closure decision"]
    L -->|"Closed"| M["CL-20 memo and applicable post-closure work"]
```

QA task authoring is not execution; execution is not acceptance. All five QA-100 outcomes return to QA-110, including failures and not-run results. Indexing is part of the task and evidence return; missing registration alone does not authorize rerunning valid checks. The historical AF-024 contrary observation remains withdrawn. QA-50's surviving requirement for a named, different executor conflicts with its own new latitude clause and needs reconciliation. Conditional DELTA modes keep their own native routes and are not the preapproval revision arrow shown here.

## Skill responsibilities and boundaries

| Surface | Actual role in this analysis |
|---|---|
| `change-flow` | Complete workflow specialization; must agree with native role, result and recovery contracts. |
| `glow-hde-pr-development` | PR-30/PR-35 primary execution support; eligible RS-40 continues the originating phase. |
| `glow-merged-change-attribution-lock` | Temporary supplemental merged attribution in PR-40; SHADOW_VALIDATION does not replace native review or select a progression route. |
| `flowmaster-primary` | Generic embedded orchestration core. Actual-target safety is distinct from a forbidden persistent-session dependency. |
| `flowmaster-propagate` | Maintenance copy operation after an approved core change; never propagates domain-specialization repairs by itself. |
| `flowmaster-validate` | Structural, interface and fixture checks; a green historical or zero-body run does not validate this candidate. |
| `typesafe-scoring` | Supplied Glow app model/effort decision aid. It is not yet a demonstrated GCFPE relay-safety interface or permission to add a model gate. |

The missing `glow-graph-contract` source owns the shipped graph builder/derivation. It is a tooling dependency, not another runtime actor. The Ops lane needs no DevOps skill (D16).
