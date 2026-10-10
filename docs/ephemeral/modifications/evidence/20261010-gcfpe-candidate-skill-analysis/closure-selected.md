# Selected graph dependency closure

Generated from current repository `closure.py` for each of 55 IDs at baseline 1ea6a262032c3c4de19c38c549d737d72b03ec2f. Command: `PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/closure.py <ID> --parts <selected prompt-parts directory> --json`. All 55 commands exit 0. These are declared one-hop relationships and state sharers, not rebuilt-graph validation, runtime traces, skill closure or a tier calculation.

### CF-C-10

```json
{
  "prompt": "CF-C-10",
  "upstream": [
    "CF-C-20",
    "CF-E-10",
    "CF-PO-10",
    "MGR-10"
  ],
  "downstream": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-PO-10"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "KICKOFF_READY"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CF-PO-10",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "MGR-10",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ]
}
```

### CF-C-20

```json
{
  "prompt": "CF-C-20",
  "upstream": [
    "CF-C-10"
  ],
  "downstream": [
    "CF-C-10",
    "CF-C-30"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-40",
    "CF-E-10",
    "CF-E-20",
    "CF-E-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "SPECIFICATION_PENDING"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-30",
    "CF-C-40",
    "CF-E-10",
    "CF-E-20",
    "CF-E-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ]
}
```

### CF-C-30

```json
{
  "prompt": "CF-C-30",
  "upstream": [
    "CF-C-20",
    "CF-C-40"
  ],
  "downstream": [
    "CF-C-40",
    "IA-10"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-E-30",
    "IA-30"
  ],
  "states": [
    "CORRECTION_REDLINE",
    "DELTA_APPROVE",
    "DELTA_DENY",
    "INITIAL_APPROVE",
    "INITIAL_DENY"
  ],
  "radius": [
    "CF-C-20",
    "CF-C-40",
    "CF-E-30",
    "IA-10",
    "IA-30"
  ]
}
```

### CF-C-40

```json
{
  "prompt": "CF-C-40",
  "upstream": [
    "CF-C-30"
  ],
  "downstream": [
    "CF-C-30"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-C-20",
    "CF-E-20",
    "CF-E-40"
  ],
  "states": [
    "SPECIFICATION_PENDING"
  ],
  "radius": [
    "CF-C-20",
    "CF-C-30",
    "CF-E-20",
    "CF-E-40"
  ]
}
```

### CF-E-10

```json
{
  "prompt": "CF-E-10",
  "upstream": [
    "CF-C-10",
    "CF-E-20",
    "CF-PO-10",
    "MGR-10"
  ],
  "downstream": [
    "CF-C-10",
    "CF-E-10",
    "CF-E-20",
    "CF-PO-10"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "KICKOFF_READY"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CF-PO-10",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "MGR-10",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ]
}
```

### CF-E-20

```json
{
  "prompt": "CF-E-20",
  "upstream": [
    "CF-E-10"
  ],
  "downstream": [
    "CF-E-10",
    "CF-E-30"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-C-40",
    "CF-E-10",
    "CF-E-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "SPECIFICATION_PENDING"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-C-40",
    "CF-E-10",
    "CF-E-30",
    "CF-E-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ]
}
```

### CF-E-30

```json
{
  "prompt": "CF-E-30",
  "upstream": [
    "CF-E-20",
    "CF-E-40"
  ],
  "downstream": [
    "CF-E-40",
    "IA-10"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-C-30",
    "IA-30"
  ],
  "states": [
    "CORRECTION_REDLINE",
    "DELTA_APPROVE",
    "DELTA_DENY",
    "INITIAL_APPROVE",
    "INITIAL_DENY"
  ],
  "radius": [
    "CF-C-30",
    "CF-E-20",
    "CF-E-40",
    "IA-10",
    "IA-30"
  ]
}
```

### CF-E-40

```json
{
  "prompt": "CF-E-40",
  "upstream": [
    "CF-E-30"
  ],
  "downstream": [
    "CF-E-30"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-C-20",
    "CF-C-40",
    "CF-E-20"
  ],
  "states": [
    "SPECIFICATION_PENDING"
  ],
  "radius": [
    "CF-C-20",
    "CF-C-40",
    "CF-E-20",
    "CF-E-30"
  ]
}
```

### CF-PO-10

```json
{
  "prompt": "CF-PO-10",
  "upstream": [
    "CF-C-10",
    "CF-E-10",
    "MGR-10"
  ],
  "downstream": [
    "CF-C-10",
    "CF-E-10"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [],
  "states": [
    "CLASS_SELECTED"
  ],
  "radius": [
    "CF-C-10",
    "CF-E-10",
    "MGR-10"
  ]
}
```

### CL-20

```json
{
  "prompt": "CL-20",
  "upstream": [
    "CL-C-10",
    "CL-E-10"
  ],
  "downstream": [
    "CL-30",
    "CL-40",
    "CL-E-20",
    "CL-E-30",
    "CL-E-40"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [],
  "states": [
    "POST_CLOSURE_PENDING"
  ],
  "radius": [
    "CL-30",
    "CL-40",
    "CL-C-10",
    "CL-E-10",
    "CL-E-20",
    "CL-E-30",
    "CL-E-40"
  ]
}
```

### CL-30

```json
{
  "prompt": "CL-30",
  "upstream": [
    "CL-20"
  ],
  "downstream": [
    "CL-40"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [],
  "states": [
    "ADR_CANDIDATE",
    "NO_ADR_NEEDED"
  ],
  "radius": [
    "CL-20",
    "CL-40"
  ]
}
```

### CL-40

```json
{
  "prompt": "CL-40",
  "upstream": [
    "CL-20",
    "CL-30",
    "CL-E-40",
    "MGR-10"
  ],
  "downstream": [
    "CL-40"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CL-E-20",
    "DOC-20",
    "ESC-25",
    "OPS-20",
    "QA-100",
    "QA-110",
    "UTIL-10"
  ],
  "states": [
    "COMPLETE",
    "INCOMPLETE"
  ],
  "radius": [
    "CL-20",
    "CL-30",
    "CL-40",
    "CL-E-20",
    "CL-E-40",
    "DOC-20",
    "ESC-25",
    "MGR-10",
    "OPS-20",
    "QA-100",
    "QA-110",
    "UTIL-10"
  ]
}
```

### CL-C-10

```json
{
  "prompt": "CL-C-10",
  "upstream": [
    "QA-120"
  ],
  "downstream": [
    "CL-20",
    "ESC-30"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CL-E-10"
  ],
  "states": [
    "CHANGE_CLOSED",
    "DO_NOT_CLOSE"
  ],
  "radius": [
    "CL-20",
    "CL-E-10",
    "ESC-30",
    "QA-120"
  ]
}
```

### CL-E-10

```json
{
  "prompt": "CL-E-10",
  "upstream": [
    "QA-120"
  ],
  "downstream": [
    "CL-20",
    "CL-E-20",
    "ESC-30"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CL-C-10"
  ],
  "states": [
    "CHANGE_CLOSED",
    "DO_NOT_CLOSE"
  ],
  "radius": [
    "CL-20",
    "CL-C-10",
    "CL-E-20",
    "ESC-30",
    "QA-120"
  ]
}
```

### CL-E-20

```json
{
  "prompt": "CL-E-20",
  "upstream": [
    "CL-20",
    "CL-E-10",
    "CL-E-30",
    "CL-E-40"
  ],
  "downstream": [
    "CL-E-20",
    "CL-E-30"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-40",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "UTIL-10"
  ],
  "states": [
    "BLOCKED",
    "COMPLETE",
    "PARTIAL"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-20",
    "CL-40",
    "CL-E-10",
    "CL-E-20",
    "CL-E-30",
    "CL-E-40",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "UTIL-10"
  ]
}
```

### CL-E-30

```json
{
  "prompt": "CL-E-30",
  "upstream": [
    "CL-20",
    "CL-E-20"
  ],
  "downstream": [
    "CL-E-20",
    "CL-E-40"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "ESC-40",
    "OPS-30",
    "PR-40",
    "QA-110",
    "QA-70"
  ],
  "states": [
    "ACCEPT",
    "DENY"
  ],
  "radius": [
    "CL-20",
    "CL-E-20",
    "CL-E-40",
    "ESC-40",
    "OPS-30",
    "PR-40",
    "QA-110",
    "QA-70"
  ]
}
```

### CL-E-40

```json
{
  "prompt": "CL-E-40",
  "upstream": [
    "CL-20",
    "CL-E-30"
  ],
  "downstream": [
    "CL-40",
    "CL-E-20"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [],
  "states": [
    "MAINTENANCE_PENDING"
  ],
  "radius": [
    "CL-20",
    "CL-40",
    "CL-E-20",
    "CL-E-30"
  ]
}
```

### DOC-10

```json
{
  "prompt": "DOC-10",
  "upstream": [
    "DOC-20"
  ],
  "downstream": [
    "DOC-10",
    "PR-20",
    "RS-10"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "PR-40",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "DRAFT",
    "INSTRUCTION_READY",
    "PENDING"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "PR-40",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "RS-10"
  ]
}
```

### DOC-20

```json
{
  "prompt": "DOC-20",
  "upstream": [],
  "downstream": [
    "DOC-10",
    "PR-40",
    "QA-10",
    "RS-10"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-40",
    "CL-E-20",
    "DOC-10",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "PR-40",
    "QA-100",
    "QA-110",
    "QA-20",
    "QA-50",
    "QA-60",
    "UTIL-10"
  ],
  "states": [
    "BLOCKED",
    "COMPLETE",
    "INCOMPLETE",
    "PENDING"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-40",
    "CL-E-20",
    "DOC-10",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "PR-40",
    "QA-10",
    "QA-100",
    "QA-110",
    "QA-20",
    "QA-50",
    "QA-60",
    "RS-10",
    "UTIL-10"
  ]
}
```

### ESC-10

```json
{
  "prompt": "ESC-10",
  "upstream": [
    "QA-110",
    "QA-120",
    "QA-90"
  ],
  "downstream": [
    "ESC-30"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [],
  "states": [
    "AWAITING_THOTH_REMEDIATION"
  ],
  "radius": [
    "ESC-30",
    "QA-110",
    "QA-120",
    "QA-90"
  ]
}
```

### ESC-25

```json
{
  "prompt": "ESC-25",
  "upstream": [
    "ESC-30",
    "OPS-10",
    "OPS-20",
    "OPS-30"
  ],
  "downstream": [
    "ESC-30"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "UTIL-10"
  ],
  "states": [
    "BLOCKED",
    "COMPLETE",
    "PARTIAL"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "OPS-30",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "UTIL-10"
  ]
}
```

### ESC-30

```json
{
  "prompt": "ESC-30",
  "upstream": [
    "CL-C-10",
    "CL-E-10",
    "ESC-10",
    "ESC-25",
    "ESC-40",
    "QA-10"
  ],
  "downstream": [
    "ESC-25",
    "ESC-40"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "DISCOVERY_REQUIRED",
    "REMEDIATION_PENDING"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-C-10",
    "CL-E-10",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-10",
    "ESC-25",
    "ESC-40",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-10",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ]
}
```

### ESC-40

```json
{
  "prompt": "ESC-40",
  "upstream": [
    "ESC-30"
  ],
  "downstream": [
    "ESC-30",
    "PR-30",
    "PR-35"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CL-E-30",
    "QA-70",
    "RS-20"
  ],
  "states": [
    "APPROVE",
    "APPROVE_AS_CHANGED",
    "DENY"
  ],
  "radius": [
    "CL-E-30",
    "ESC-30",
    "PR-30",
    "PR-35",
    "QA-70",
    "RS-20"
  ]
}
```

### GCFPE-MGMT-10

```json
{
  "prompt": "GCFPE-MGMT-10",
  "upstream": [],
  "downstream": [
    "PR-10"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [],
  "states": [
    "ECOSYSTEM_CHANGE_COMPLETE",
    "IMPLEMENTATION_BLOCKED",
    "PROMOTION_CHECKPOINT_REQUIRED",
    "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION"
  ],
  "radius": [
    "PR-10"
  ]
}
```

### IA-10

```json
{
  "prompt": "IA-10",
  "upstream": [
    "CF-C-30",
    "CF-E-30",
    "IA-50"
  ],
  "downstream": [
    "IA-10",
    "IA-20",
    "IA-30",
    "IA-50",
    "IA-60"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "AUDIT_COMPLETE",
    "BLOCKED",
    "PLAN_PENDING"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-C-30",
    "CF-E-10",
    "CF-E-20",
    "CF-E-30",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-30",
    "IA-50",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ]
}
```

### IA-20

```json
{
  "prompt": "IA-20",
  "upstream": [
    "IA-10",
    "IA-50"
  ],
  "downstream": [
    "IA-20",
    "IA-30",
    "IA-50",
    "IA-60"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "PLAN_PENDING"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-30",
    "IA-50",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ]
}
```

### IA-30

```json
{
  "prompt": "IA-30",
  "upstream": [
    "IA-10",
    "IA-20",
    "IA-40",
    "IA-50"
  ],
  "downstream": [
    "IA-40",
    "PR-10"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-C-30",
    "CF-E-30",
    "IA-40",
    "PR-30",
    "PR-35",
    "RS-40"
  ],
  "states": [
    "CHANGE_NOT_SUBSTANTIATED",
    "DELTA_APPROVE",
    "DELTA_DENY",
    "INITIAL_APPROVE",
    "INITIAL_DENY",
    "PLAN_DELTA_REDLINE",
    "PRODUCT_OWNER_DECISION_REQUIRED",
    "WRONG_NATIVE_LANE"
  ],
  "radius": [
    "CF-C-30",
    "CF-E-30",
    "IA-10",
    "IA-20",
    "IA-40",
    "IA-50",
    "PR-10",
    "PR-30",
    "PR-35",
    "RS-40"
  ]
}
```

### IA-40

```json
{
  "prompt": "IA-40",
  "upstream": [
    "IA-30",
    "IA-50"
  ],
  "downstream": [
    "IA-30"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "IA-30",
    "QA-80"
  ],
  "states": [
    "PLAN_DELTA_PENDING",
    "PLAN_PENDING_REVISED",
    "REDLINE_INCOMPLETE",
    "WRONG_NATIVE_LANE"
  ],
  "radius": [
    "IA-30",
    "IA-50",
    "QA-80"
  ]
}
```

### IA-50

```json
{
  "prompt": "IA-50",
  "upstream": [
    "IA-10",
    "IA-20",
    "IA-60"
  ],
  "downstream": [
    "IA-10",
    "IA-20",
    "IA-30",
    "IA-40"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [],
  "states": [
    "SEED_INCOMPLETE",
    "SEED_READY"
  ],
  "radius": [
    "IA-10",
    "IA-20",
    "IA-30",
    "IA-40",
    "IA-60"
  ]
}
```

### IA-60

```json
{
  "prompt": "IA-60",
  "upstream": [
    "IA-10",
    "IA-20"
  ],
  "downstream": [
    "IA-50"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "PARTIAL",
    "RESEARCH_COMPLETE"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-50",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ]
}
```

### MGR-10

```json
{
  "prompt": "MGR-10",
  "upstream": [],
  "downstream": [
    "CF-C-10",
    "CF-E-10",
    "CF-PO-10",
    "CL-40",
    "QA-10"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [],
  "states": [
    "FLOW_PROGRESS",
    "TERMINAL_RETURN"
  ],
  "radius": [
    "CF-C-10",
    "CF-E-10",
    "CF-PO-10",
    "CL-40",
    "QA-10"
  ]
}
```

### OPS-10

```json
{
  "prompt": "OPS-10",
  "upstream": [
    "OPS-30"
  ],
  "downstream": [
    "ESC-25",
    "OPS-20",
    "RS-10"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "READY"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-20",
    "OPS-30",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "RS-10"
  ]
}
```

### OPS-20

```json
{
  "prompt": "OPS-20",
  "upstream": [
    "OPS-10"
  ],
  "downstream": [
    "ESC-25",
    "OPS-30",
    "RS-10"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "QA-90",
    "UTIL-10"
  ],
  "states": [
    "BLOCKED",
    "COMPLETE",
    "FAILED",
    "NOT_EXECUTED",
    "NOT_PRODUCED",
    "PARTIAL"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-30",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "QA-90",
    "RS-10",
    "UTIL-10"
  ]
}
```

### OPS-30

```json
{
  "prompt": "OPS-30",
  "upstream": [
    "OPS-20"
  ],
  "downstream": [
    "ESC-25",
    "OPS-10",
    "RS-10"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CL-E-30",
    "PR-40",
    "QA-110",
    "RS-20"
  ],
  "states": [
    "ACCEPT",
    "REJECT"
  ],
  "radius": [
    "CL-E-30",
    "ESC-25",
    "OPS-10",
    "OPS-20",
    "PR-40",
    "QA-110",
    "RS-10",
    "RS-20"
  ]
}
```

### PR-10

```json
{
  "prompt": "PR-10",
  "upstream": [
    "GCFPE-MGMT-10",
    "IA-30",
    "PR-40"
  ],
  "downstream": [
    "PR-10",
    "PR-20",
    "RS-10"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "DRAFT",
    "INSTRUCTION_READY"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "GCFPE-MGMT-10",
    "IA-10",
    "IA-20",
    "IA-30",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "PR-40",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "RS-10"
  ]
}
```

### PR-20

```json
{
  "prompt": "PR-20",
  "upstream": [
    "DOC-10",
    "PR-10",
    "PR-40"
  ],
  "downstream": [
    "PR-20",
    "RS-10"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "NATHAN_PROCEED",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "AWAITING_PO_PROCEED",
    "BLOCKED",
    "DRAFT"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "PR-40",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-60",
    "RS-10"
  ]
}
```

### PR-30

```json
{
  "prompt": "PR-30",
  "upstream": [
    "ESC-40",
    "RS-20",
    "RS-40"
  ],
  "downstream": [
    "PR-30",
    "PR-35",
    "RS-20"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "IA-30",
    "PR-35",
    "RS-40"
  ],
  "states": [
    "PRODUCT_OWNER_DECISION_REQUIRED",
    "PR_CANDIDATE_PUBLISHED",
    "RECOVERY_PENDING",
    "RESCOPE_PENDING"
  ],
  "radius": [
    "ESC-40",
    "IA-30",
    "PR-30",
    "PR-35",
    "RS-20",
    "RS-40"
  ]
}
```

### PR-35

```json
{
  "prompt": "PR-35",
  "upstream": [
    "ESC-40",
    "PR-30",
    "RS-20",
    "RS-40"
  ],
  "downstream": [
    "PR-35",
    "PR-40",
    "RS-20"
  ],
  "boundaries": [
    "NATHAN_MANUAL_MERGE_ASSERTION",
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "IA-30",
    "PR-30",
    "RS-40"
  ],
  "states": [
    "MERGE_OBSERVED",
    "MERGE_PENDING",
    "PRODUCT_OWNER_DECISION_REQUIRED",
    "RECOVERY_PENDING",
    "REMOTE_EVIDENCE_PENDING",
    "RESCOPE_PENDING"
  ],
  "radius": [
    "ESC-40",
    "IA-30",
    "PR-30",
    "PR-35",
    "PR-40",
    "RS-20",
    "RS-40"
  ]
}
```

### PR-40

```json
{
  "prompt": "PR-40",
  "upstream": [
    "DOC-20",
    "PR-35",
    "RS-40"
  ],
  "downstream": [
    "PR-10",
    "PR-20",
    "RS-10"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CL-E-30",
    "DOC-10",
    "DOC-20",
    "OPS-30",
    "QA-110",
    "RS-20"
  ],
  "states": [
    "ACCEPT",
    "PENDING",
    "REJECT"
  ],
  "radius": [
    "CL-E-30",
    "DOC-10",
    "DOC-20",
    "OPS-30",
    "PR-10",
    "PR-20",
    "PR-35",
    "QA-110",
    "RS-10",
    "RS-20",
    "RS-40"
  ]
}
```

### PR-50

```json
{
  "prompt": "PR-50",
  "upstream": [],
  "downstream": [],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [],
  "states": [
    "PR_ABORTED_ESCALATED"
  ],
  "radius": []
}
```

### QA-10

```json
{
  "prompt": "QA-10",
  "upstream": [
    "DOC-20",
    "MGR-10",
    "QA-20"
  ],
  "downstream": [
    "ESC-30",
    "QA-20"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [],
  "states": [
    "ASSESSMENT_INCOMPLETE",
    "NOT_READY",
    "READY_FOR_QA"
  ],
  "radius": [
    "DOC-20",
    "ESC-30",
    "MGR-10",
    "QA-20"
  ]
}
```

### QA-100

```json
{
  "prompt": "QA-100",
  "upstream": [
    "QA-110",
    "QA-90"
  ],
  "downstream": [
    "QA-110"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-20",
    "QA-50",
    "QA-60",
    "QA-90",
    "UTIL-10"
  ],
  "states": [
    "BLOCKED",
    "COMPLETE",
    "FAILED",
    "NOT_EXECUTED",
    "PARTIAL"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-40",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-110",
    "QA-20",
    "QA-50",
    "QA-60",
    "QA-90",
    "UTIL-10"
  ]
}
```

### QA-110

```json
{
  "prompt": "QA-110",
  "upstream": [
    "QA-100",
    "QA-120",
    "QA-90"
  ],
  "downstream": [
    "ESC-10",
    "QA-100",
    "QA-120",
    "QA-90"
  ],
  "boundaries": [
    "ACTUAL_OWNER_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CL-40",
    "CL-E-30",
    "DOC-20",
    "OPS-30",
    "PR-40",
    "QA-90",
    "UTIL-10"
  ],
  "states": [
    "ACCEPT",
    "BOUNDED_RERUN_REQUIRED",
    "ESCALATION_REQUIRED",
    "INCOMPLETE"
  ],
  "radius": [
    "CL-40",
    "CL-E-30",
    "DOC-20",
    "ESC-10",
    "OPS-30",
    "PR-40",
    "QA-100",
    "QA-120",
    "QA-90",
    "UTIL-10"
  ]
}
```

### QA-120

```json
{
  "prompt": "QA-120",
  "upstream": [
    "QA-110"
  ],
  "downstream": [
    "CL-C-10",
    "CL-E-10",
    "ESC-10",
    "QA-110",
    "QA-90"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [],
  "states": [
    "FAIL",
    "INTERIM",
    "PASS"
  ],
  "radius": [
    "CL-C-10",
    "CL-E-10",
    "ESC-10",
    "QA-110",
    "QA-90"
  ]
}
```

### QA-20

```json
{
  "prompt": "QA-20",
  "upstream": [
    "QA-10"
  ],
  "downstream": [
    "QA-10",
    "QA-50"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-50",
    "QA-60"
  ],
  "states": [
    "BLOCKED",
    "GUIDE_READY"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-10",
    "QA-100",
    "QA-50",
    "QA-60"
  ]
}
```

### QA-50

```json
{
  "prompt": "QA-50",
  "upstream": [
    "QA-20"
  ],
  "downstream": [
    "QA-60",
    "QA-70",
    "QA-80",
    "QA-90"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-60"
  ],
  "states": [
    "AUDIT_COMPLETE",
    "BLOCKED",
    "PLAN_PENDING"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-60",
    "QA-70",
    "QA-80",
    "QA-90"
  ]
}
```

### QA-60

```json
{
  "prompt": "QA-60",
  "upstream": [
    "QA-50"
  ],
  "downstream": [
    "QA-70",
    "QA-80",
    "QA-90"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50"
  ],
  "states": [
    "BLOCKED",
    "PLAN_PENDING"
  ],
  "radius": [
    "CF-C-10",
    "CF-C-20",
    "CF-E-10",
    "CF-E-20",
    "CL-E-20",
    "DOC-10",
    "DOC-20",
    "ESC-25",
    "ESC-30",
    "IA-10",
    "IA-20",
    "IA-60",
    "OPS-10",
    "OPS-20",
    "PR-10",
    "PR-20",
    "QA-100",
    "QA-20",
    "QA-50",
    "QA-70",
    "QA-80",
    "QA-90"
  ]
}
```

### QA-70

```json
{
  "prompt": "QA-70",
  "upstream": [
    "QA-50",
    "QA-60",
    "QA-80"
  ],
  "downstream": [
    "QA-80",
    "QA-90"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CL-E-30",
    "ESC-40",
    "RS-20"
  ],
  "states": [
    "APPROVE",
    "DENY"
  ],
  "radius": [
    "CL-E-30",
    "ESC-40",
    "QA-50",
    "QA-60",
    "QA-80",
    "QA-90",
    "RS-20"
  ]
}
```

### QA-80

```json
{
  "prompt": "QA-80",
  "upstream": [
    "QA-50",
    "QA-60",
    "QA-70"
  ],
  "downstream": [
    "QA-70"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "IA-40"
  ],
  "states": [
    "PLAN_PENDING_REVISED",
    "WRONG_ROUTE_APPROVED_BASE"
  ],
  "radius": [
    "IA-40",
    "QA-50",
    "QA-60",
    "QA-70"
  ]
}
```

### QA-90

```json
{
  "prompt": "QA-90",
  "upstream": [
    "QA-110",
    "QA-120",
    "QA-50",
    "QA-60",
    "QA-70"
  ],
  "downstream": [
    "ESC-10",
    "QA-100",
    "QA-110"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "OPS-20",
    "QA-100",
    "QA-110"
  ],
  "states": [
    "ESCALATION_REQUIRED",
    "NOT_EXECUTED",
    "TASK_READY"
  ],
  "radius": [
    "ESC-10",
    "OPS-20",
    "QA-100",
    "QA-110",
    "QA-120",
    "QA-50",
    "QA-60",
    "QA-70"
  ]
}
```

### RS-10

```json
{
  "prompt": "RS-10",
  "upstream": [
    "DOC-10",
    "DOC-20",
    "OPS-10",
    "OPS-20",
    "OPS-30",
    "PR-10",
    "PR-20",
    "PR-40"
  ],
  "downstream": [
    "RS-20"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "RS-30"
  ],
  "states": [
    "RESCOPE_PROPOSAL_PENDING_REVIEW"
  ],
  "radius": [
    "DOC-10",
    "DOC-20",
    "OPS-10",
    "OPS-20",
    "OPS-30",
    "PR-10",
    "PR-20",
    "PR-40",
    "RS-20",
    "RS-30"
  ]
}
```

### RS-20

```json
{
  "prompt": "RS-20",
  "upstream": [
    "PR-30",
    "PR-35",
    "RS-10",
    "RS-30",
    "RS-40"
  ],
  "downstream": [
    "PR-30",
    "PR-35",
    "RS-30",
    "RS-40"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "ESC-40",
    "OPS-30",
    "PR-40",
    "QA-70"
  ],
  "states": [
    "APPROVE",
    "IN_SCOPE_REPAIR",
    "REJECT",
    "REVISION_REQUIRED",
    "SPECIFICATION_CHANGE_REQUIRED"
  ],
  "radius": [
    "ESC-40",
    "OPS-30",
    "PR-30",
    "PR-35",
    "PR-40",
    "QA-70",
    "RS-10",
    "RS-30",
    "RS-40"
  ]
}
```

### RS-30

```json
{
  "prompt": "RS-30",
  "upstream": [
    "RS-20"
  ],
  "downstream": [
    "RS-20"
  ],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "RS-10"
  ],
  "states": [
    "RESCOPE_PROPOSAL_PENDING_REVIEW"
  ],
  "radius": [
    "RS-10",
    "RS-20"
  ]
}
```

### RS-40

```json
{
  "prompt": "RS-40",
  "upstream": [
    "RS-20"
  ],
  "downstream": [
    "PR-30",
    "PR-35",
    "PR-40",
    "RS-20"
  ],
  "boundaries": [
    "NATHAN_MANUAL_MERGE_ASSERTION",
    "NATHAN_TERMINAL_RETURN"
  ],
  "state_sharers": [
    "IA-30",
    "PR-30",
    "PR-35"
  ],
  "states": [
    "MERGE_OBSERVED",
    "MERGE_PENDING",
    "PRODUCT_OWNER_DECISION_REQUIRED",
    "PR_CANDIDATE_PUBLISHED",
    "RECOVERY_PENDING",
    "REMOTE_EVIDENCE_PENDING",
    "RESCOPE_PENDING",
    "SOURCE_RESOLUTION_ERROR"
  ],
  "radius": [
    "IA-30",
    "PR-30",
    "PR-35",
    "PR-40",
    "RS-20"
  ]
}
```

### UTIL-10

```json
{
  "prompt": "UTIL-10",
  "upstream": [],
  "downstream": [],
  "boundaries": [
    "NATHAN_TERMINAL_RETURN",
    "ORIGINAL_NATIVE_STAGE"
  ],
  "state_sharers": [
    "CL-40",
    "CL-E-20",
    "DOC-20",
    "ESC-25",
    "OPS-20",
    "QA-100",
    "QA-110"
  ],
  "states": [
    "ALREADY_APPLIED",
    "COMPLETE",
    "INCOMPLETE"
  ],
  "radius": [
    "CL-40",
    "CL-E-20",
    "DOC-20",
    "ESC-25",
    "OPS-20",
    "QA-100",
    "QA-110"
  ]
}
```
