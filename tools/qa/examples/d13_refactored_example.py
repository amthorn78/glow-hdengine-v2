#!/usr/bin/env python3
"""
Example: D13 Human Index check using standard r7-compliant header template.

This demonstrates how to use tools.qa.step_log_header to eliminate header
compliance issues during initial check execution.

Before: Manually construct headers, often forgetting required fields
After: Use create_header() with all r7 requirements baked in
"""

import json
import sys
from pathlib import Path

# Add tools to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from tools.qa.step_log_header import (
    create_header,
    write_header,
    append_output,
    update_header_status,
)

# Configuration
CHECK_ID = "D13_human_index"
INDEX_PATH = Path("docs/evidence/INDEX.json")
INDEX_PROOF = Path("docs/evidence/INDEX.json.path_proof.txt")
OUTPUT_PATH = Path("audit/qa/hde-epic023/checks/D13_human_index/primary.log")

REQUIRED_PATHS = {
    "docs/acceptance_map_epic023.json",
    "audit/qa/hde-epic023/token_evidence_matrix.md",
    "audit/qa/hde-epic023/acceptance_map_viability.log",
    "audit/qa/hde-epic023/qa_step_logs_manifest.json",
    "audit/EPIC-023_close_report.md",
}


def main():
    # Create r7-compliant header with all required fields
    header = create_header(
        check_id=CHECK_ID,
        command="python3 (embedded) validate docs/evidence/INDEX.json contains EPIC023 entries (+ path proof)",
        status="PASS",  # Start optimistic, will update on failure
        pf_refs=[],  # D13 is a simple containment check, no specific PF refs
        intended_tokens=[],  # D13 doesn't claim tokens, just validates content
        claimed_tokens=[],
    )

    try:
        # Validation logic
        if not INDEX_PATH.exists():
            raise FileNotFoundError(f"TOOLING_BLOCKED: missing {INDEX_PATH}")
        
        if not INDEX_PROOF.exists():
            raise FileNotFoundError(f"TOOLING_BLOCKED: missing {INDEX_PROOF}")
        
        # Load and check INDEX.json
        with INDEX_PATH.open("r", encoding="utf-8") as f:
            index_data = json.load(f)
        
        index_str = json.dumps(index_data)
        
        # Check for required path strings
        missing = []
        for path in REQUIRED_PATHS:
            if path not in index_str:
                missing.append(path)
        
        if missing:
            raise ValueError(
                f"FAIL_BEHAVIOR: INDEX.json missing required paths: {sorted(missing)}"
            )
        
        # Success
        result = "PASS: INDEX.json references all required EPIC023 artifact paths (string containment)."
        update_header_status(header, "PASS")
        
    except FileNotFoundError as e:
        result = str(e)
        update_header_status(header, "TOOLING_BLOCKED", claimed_tokens=[])
        
    except ValueError as e:
        result = str(e)
        update_header_status(header, "FAIL_BEHAVIOR", claimed_tokens=[])
        
    except Exception as e:
        result = f"FAIL_TOOLING: Unexpected error: {e}"
        update_header_status(header, "FAIL_TOOLING", claimed_tokens=[])
    
    # Write final output
    write_header(OUTPUT_PATH, header)
    append_output(OUTPUT_PATH, result)
    
    # Exit with appropriate code
    if header["status"] == "PASS":
        return 0
    elif header["status"] == "TOOLING_BLOCKED":
        return 13
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
