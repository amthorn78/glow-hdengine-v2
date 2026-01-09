#!/usr/bin/env python3
"""
Standard step-log header template for QA checks (PF10 §2.34 compliant).

This module provides a canonical way to generate primary.log headers that satisfy
PF10 §2.34 step-log header requirements with proper defaultable field handling.

Per PF10 §2.34:
- Hard required fields: check_id, status, command, captured_env
- Defaultable fields: pf_refs, intended_tokens, claimed_tokens (default to [])
- Status vocabulary: PASS, FAIL_BEHAVIOR, FAIL_TOOLING, TOOLING_BLOCKED, PARKED
- Token claims are never inferred from text

Usage:
    from tools.qa.step_log_header import create_header, write_header
    
    header = create_header(
        check_id="D13_human_index",
        command="python3 (embedded) validate INDEX.json",
        pf_refs=["PF12 §8.5"],  # optional, defaults to []
        intended_tokens=["SOME_TOKEN"]  # optional, defaults to []
    )
    
    write_header(output_path, header)
    # ... write validation output after header
"""

import datetime as _dt
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

# PF10 §2.34 allowed status vocabulary (gating)
ALLOWED_STATUS = {"PASS", "FAIL_BEHAVIOR", "FAIL_TOOLING", "TOOLING_BLOCKED", "PARKED"}

# Required environment pins for closed-rails execution
REQUIRED_ENV_PINS = ["SAFE_MODE", "ALLOW_NETWORK", "APP_ENV", "LC_ALL", "LANG", "TZ"]


def capture_env() -> Dict[str, Optional[str]]:
    """
    Capture required environment pins for closed-rails execution.
    
    Returns:
        Dictionary mapping env var names to their values (or None if unset).
    """
    return {key: os.getenv(key) for key in REQUIRED_ENV_PINS}


def create_header(
    check_id: str,
    command: str,
    status: str = "PASS",
    pf_refs: Optional[List[str]] = None,
    intended_tokens: Optional[List[str]] = None,
    claimed_tokens: Optional[List[str]] = None,
    captured_env: Optional[Dict[str, Optional[str]]] = None,
) -> Dict[str, Any]:
    """
    Create a PF10 §2.34 compliant step-log header.
    
    Per PF10 §2.34:
    - Hard required fields: check_id, status, command, captured_env
    - Defaultable fields (non-gating): pf_refs, intended_tokens, claimed_tokens
    - Missing defaultable fields are treated as empty lists
    
    Args:
        check_id: Unique identifier for the check (e.g., "D13_human_index") [REQUIRED]
        command: Command description (e.g., "python3 (embedded) validate INDEX.json") [REQUIRED]
        status: Check status from PF10 §2.34 vocabulary (default: "PASS") [REQUIRED]
        pf_refs: PF-Canon references (defaultable, defaults to [])
        intended_tokens: Tokens this check intends to validate (defaultable, defaults to [])
        claimed_tokens: Tokens this check claims on success (defaultable, defaults to [])
        captured_env: Environment pins (default: auto-captured from current env) [REQUIRED]
    
    Returns:
        Dictionary with 4 hard required fields + 3 defaultable fields.
        
    Raises:
        ValueError: If status is not in ALLOWED_STATUS vocabulary (gating per PF10 §2.34).
    """
    if status not in ALLOWED_STATUS:
        raise ValueError(
            f"Invalid status '{status}'. Per PF10 §2.34, must be one of: {', '.join(sorted(ALLOWED_STATUS))}"
        )
    
    # Per PF10 §2.34: 4 hard required fields + 3 defaultable fields
    return {
        "captured_env": captured_env if captured_env is not None else capture_env(),
        "check_id": check_id,
        "status": status,
        "command": command,
        "pf_refs": pf_refs or [],  # defaultable (non-gating)
        "intended_tokens": intended_tokens or [],  # defaultable (non-gating)
        "claimed_tokens": claimed_tokens or [],  # defaultable (non-gating)
    }


def update_header_status(
    header: Dict[str, Any],
    status: str,
    claimed_tokens: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Update header status and optionally set claimed tokens.
    
    Per PF10 §2.34:
    - Status must be from allowed vocabulary (gating)
    - Token claims are never inferred from text
    - Auto-claim intended_tokens on PASS if claimed_tokens not explicitly provided
    
    Use this at the end of a check to set final status and record claimed tokens.
    
    Args:
        header: Header dict to update (modified in-place and returned)
        status: New status from PF10 §2.34 vocabulary
        claimed_tokens: Tokens to claim (if None, header's intended_tokens are claimed on PASS)
    
    Returns:
        Updated header dict (same object as input).
        
    Raises:
        ValueError: If status is not in ALLOWED_STATUS vocabulary (gating per PF10 §2.34).
    """
    if status not in ALLOWED_STATUS:
        raise ValueError(
            f"Invalid status '{status}'. Per PF10 §2.34, must be one of: {', '.join(sorted(ALLOWED_STATUS))}"
        )
    
    header["status"] = status
    
    # Auto-claim intended tokens on PASS if claimed_tokens not explicitly provided
    # Per PF10 §2.34: Token claims are never inferred from text
    if status == "PASS":
        if claimed_tokens is not None:
            header["claimed_tokens"] = claimed_tokens
        elif header.get("intended_tokens"):
            header["claimed_tokens"] = header["intended_tokens"][:]
    
    return header


def normalize_header(header: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize header by ensuring all defaultable fields exist (PF10 §2.34).
    
    Per PF10 §2.34 Rule 2: Missing defaultable fields are interpreted as empty lists.
    This is an evidence-format repair that does not require re-running the step.
    
    Args:
        header: Header dict to normalize (modified in-place and returned)
    
    Returns:
        Normalized header dict (same object as input).
    """
    # Ensure defaultable fields exist (non-gating per PF10 §2.34)
    header.setdefault("pf_refs", [])
    header.setdefault("intended_tokens", [])
    header.setdefault("claimed_tokens", [])
    return header


def serialize_header(header: Dict[str, Any]) -> str:
    """
    Serialize header to canonical JSON format (compact, sorted keys, trailing newline).
    
    Args:
        header: Header dict to serialize
    
    Returns:
        JSON string with compact separators, sorted keys, and trailing newline.
    """
    return json.dumps(header, sort_keys=True, separators=(",", ":")) + "\n"


def write_header(path: Path, header: Dict[str, Any]) -> None:
    """
    Write PF10 §2.34 compliant header as first line of primary.log file.
    
    Automatically normalizes header to ensure defaultable fields exist.
    
    Args:
        path: Output path for primary.log
        header: Header dict to write
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    normalize_header(header)  # Ensure defaultable fields exist
    with path.open("w", encoding="utf-8") as f:
        f.write(serialize_header(header))


def append_output(path: Path, content: str) -> None:
    """
    Append validation output after header line.
    
    Args:
        path: Path to primary.log
        content: Validation output to append
    """
    with path.open("a", encoding="utf-8") as f:
        if not content.endswith("\n"):
            content += "\n"
        f.write(content)


# Example usage template for embedded scripts (PF10 §2.34 compliant)
EXAMPLE_TEMPLATE = '''
# Import the header utilities
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from tools.qa.step_log_header import create_header, write_header, append_output, update_header_status

# Create header - only check_id, command, status, captured_env are hard required
# pf_refs, intended_tokens, claimed_tokens are defaultable (optional)
header = create_header(
    check_id="D13_human_index",
    command="python3 (embedded) validate docs/evidence/INDEX.json contains EPIC023 entries",
    status="PASS",  # Must be from PF10 §2.34 vocabulary (gating)
    pf_refs=["PF12 §8.5", "PF10 §2.16"],  # optional, defaults to []
    intended_tokens=["EVIDENCE_INDEX_VALIDATED"],  # optional, defaults to []
)

output_path = Path("audit/qa/hde-epic023/checks/D13_human_index/primary.log")

# Perform validation
try:
    # ... validation logic ...
    result = "PASS: INDEX.json contains all required EPIC023 paths."
    
    # Update to PASS and claim tokens (if not already PASS)
    update_header_status(header, "PASS")  # Auto-claims intended_tokens on PASS
    
except Exception as e:
    result = f"FAIL_BEHAVIOR: {e}"
    update_header_status(header, "FAIL_BEHAVIOR", claimed_tokens=[])

# Write final header and output (auto-normalizes defaultable fields)
write_header(output_path, header)
append_output(output_path, result)
'''


if __name__ == "__main__":
    # Self-test: generate example headers demonstrating PF10 §2.34 compliance
    print("=== PF10 §2.34 Compliant Headers ===\n")
    
    # Example 1: Minimal (only hard required fields + empty defaults)
    h1 = create_header(
        check_id="D13_human_index",
        command="python3 (embedded) validate INDEX.json"
    )
    normalize_header(h1)
    print("Example 1 (minimal - defaultable fields empty):")
    print(serialize_header(h1))
    
    # Example 2: With PF refs and tokens (full)
    h2 = create_header(
        check_id="D15_machine_mirror",
        command="python3 (embedded) validate evidence_index.jsonl",
        pf_refs=["PF12 §8.5", "PF10 §2.16"],
        intended_tokens=["EVIDENCE_INDEX_MIRROR_OK"]
    )
    normalize_header(h2)
    print("Example 2 (with PF refs and intended tokens):")
    print(serialize_header(h2))
    
    # Example 3: PASS with auto-claimed tokens
    h3 = create_header(
        check_id="D15_machine_mirror",
        command="python3 (embedded) validate evidence_index.jsonl",
        pf_refs=["PF12 §8.5"],
        intended_tokens=["EVIDENCE_INDEX_MIRROR_OK"]
    )
    update_header_status(h3, "PASS")  # Auto-claims intended_tokens
    normalize_header(h3)
    print("Example 3 (PASS with auto-claimed tokens):")
    print(serialize_header(h3))
    
    # Example 4: FAIL_BEHAVIOR with no claims
    h4 = create_header(
        check_id="D11_close_report",
        command="python3 (embedded) validate close_report.md",
        intended_tokens=["CLOSE_REPORT_VALIDATED"]
    )
    update_header_status(h4, "FAIL_BEHAVIOR", claimed_tokens=[])
    normalize_header(h4)
    print("Example 4 (FAIL_BEHAVIOR - no token claims per PF10 §2.34):")
    print(serialize_header(h4))
    
    print("\nPer PF10 §2.34:")
    print("- Hard required: check_id, status, command, captured_env")
    print("- Defaultable (non-gating): pf_refs, intended_tokens, claimed_tokens")
    print("- Missing defaultable fields default to []")
    print("- Token claims never inferred from text")
    print("- Status vocabulary (gating): PASS, FAIL_BEHAVIOR, FAIL_TOOLING, TOOLING_BLOCKED, PARKED")
