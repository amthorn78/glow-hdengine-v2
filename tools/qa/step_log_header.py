#!/usr/bin/env python3
"""
Compatibility step-log headers with explicit claim rules from PF27.

This helper preserves the existing reduced header interface; it does not produce
the full current v2 QA schema or prove that a check ran or a token predicate passed.

Supported fields and outcomes:
- Hard required fields: check_id, status, command, captured_env
- Defaultable fields: pf_refs, intended_tokens, claimed_tokens (default to [])
- Status vocabulary: PASS, FAIL_BEHAVIOR, FAIL_TOOLING, TOOLING_BLOCKED, PARKED
- Claims are explicit PASS-only data, contained in intended_tokens
- Omitted claims are empty, including on updates to a previously claimed outcome
- The caller explains PASS intended/claimed differences in the log body

Usage:
    from tools.qa.step_log_header import create_header, write_header
    
    header = create_header(
        check_id="D13_human_index",
        command="python3 (embedded) validate INDEX.json",
        pf_refs=["PF12 §8.5"],  # optional, defaults to []
        status="PARKED",  # caller records the actual outcome after its check
    )
    
    write_header(output_path, header)
    # ... write validation output after header
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

# Supported compatibility status vocabulary
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


def _validate_claims(
    status: str,
    intended_tokens: Optional[List[str]],
    claimed_tokens: Optional[List[str]],
) -> List[str]:
    """Validate a proposed outcome without mutating caller data or issuing claims."""
    if status not in ALLOWED_STATUS:
        # Retain the existing invalid-status diagnostic for compatibility.
        raise ValueError(
            f"Invalid status '{status}'. Per PF10 §2.34, must be one of: {', '.join(sorted(ALLOWED_STATUS))}"
        )
    claims = claimed_tokens if claimed_tokens is not None else []
    if claims and status != "PASS":
        raise ValueError("Nonempty claimed_tokens require PASS status")
    if any(token not in (intended_tokens or []) for token in claims):
        raise ValueError("Every claimed token must appear in intended_tokens")
    return claims


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
    Create a compatibility header with a truthful caller-selected outcome.
    
    Supported compatibility fields:
    - Hard required fields: check_id, status, command, captured_env
    - Defaultable fields (non-gating): pf_refs, intended_tokens, claimed_tokens
    - Missing defaultable fields are treated as empty lists
    
    Args:
        check_id: Unique identifier for the check (e.g., "D13_human_index") [REQUIRED]
        command: Command description (e.g., "python3 (embedded) validate INDEX.json") [REQUIRED]
        status: Actual check status (default: "PASS", retained for compatibility)
        pf_refs: PF-Canon references (defaultable, defaults to [])
        intended_tokens: Tokens this check intends to validate (defaultable, defaults to [])
        claimed_tokens: Explicit PASS claims within intended_tokens; None means []
        captured_env: Environment pins (default: auto-captured from current env) [REQUIRED]
    
    Returns:
        Dictionary with 4 hard required fields + 3 defaultable fields.
        
    Raises:
        ValueError: If the status or explicit claim combination is invalid.

    The caller must justify its outcome and claims. Intended-list alignment is
    neither registry validation nor predicate proof. Explain any PASS difference
    between intended and claimed tokens in the log body.
    """
    claims = _validate_claims(status, intended_tokens, claimed_tokens)
    
    # Preserve the four required and three defaultable compatibility fields.
    return {
        "captured_env": captured_env if captured_env is not None else capture_env(),
        "check_id": check_id,
        "status": status,
        "command": command,
        "pf_refs": pf_refs or [],  # defaultable (non-gating)
        "intended_tokens": intended_tokens or [],  # defaultable (non-gating)
        "claimed_tokens": claims,
    }


def update_header_status(
    header: Dict[str, Any],
    status: str,
    claimed_tokens: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Record a new outcome, replacing both status and claims after validation.

    Omitted/None or empty claims clear all earlier claims, even on PASS-to-PASS.
    Non-PASS outcomes cannot carry claims. Invalid input leaves the entire earlier
    header untouched; it does not record the rejected attempt as a new outcome.
    
    Args:
        header: Header dict to update (modified in-place and returned)
        status: New status from the supported vocabulary
        claimed_tokens: Explicit PASS claims within intentions; None means []
    
    Returns:
        Updated header dict (same object as input).
        
    Raises:
        ValueError: If the status or explicit claim combination is invalid.
    """
    claims = _validate_claims(status, header.get("intended_tokens"), claimed_tokens)
    header["status"] = status
    header["claimed_tokens"] = claims
    return header


def normalize_header(header: Dict[str, Any]) -> Dict[str, Any]:
    """
    Supply missing compatibility arrays without changing retained historical data.

    This is formatting only, not re-execution, claim validation or new acceptance.
    Existing statuses, claims and caller-added fields remain unchanged.
    
    Args:
        header: Header dict to normalize (modified in-place and returned)
    
    Returns:
        Normalized header dict (same object as input).
    """
    # Formatting must not infer or remove retained claims.
    header.setdefault("pf_refs", [])
    header.setdefault("intended_tokens", [])
    header.setdefault("claimed_tokens", [])
    return header


def serialize_header(header: Dict[str, Any]) -> str:
    """
    Serialize header to canonical JSON format (compact, sorted keys, trailing newline).

    Formatting retained history does not validate a new outcome; write_header
    separately guards current publication.
    
    Args:
        header: Header dict to serialize
    
    Returns:
        JSON string with compact separators, sorted keys, and trailing newline.
    """
    return json.dumps(header, sort_keys=True, separators=(",", ":")) + "\n"


def write_header(path: Path, header: Dict[str, Any]) -> None:
    """
    Validate and serialize a compatibility header before replacing its log.

    Rejected input leaves the header, existing file and absent directories intact.
    Successful writes supply supported defaults in place and retain extra fields.
    I/O errors propagate; this is not a crash-recovery or header/body transaction.
    
    Args:
        path: Output path for primary.log
        header: Header dict to write
    """
    candidate = normalize_header(dict(header))
    candidate["claimed_tokens"] = _validate_claims(
        candidate["status"], candidate["intended_tokens"], candidate["claimed_tokens"]
    )
    serialized = serialize_header(candidate)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(serialized)
    header.update(candidate)


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


# Illustrative compatibility usage; run from a source root with tools importable.
EXAMPLE_TEMPLATE = '''
from pathlib import Path
from tempfile import TemporaryDirectory
from tools.qa.step_log_header import create_header, write_header, append_output, update_header_status

# Demonstration data only: this is not a real QA check or a token predicate proof.
header = create_header(
    check_id="illustrative-check",
    command="illustration only; no real QA executed",
    status="PARKED",
    intended_tokens=["DEMO_REFERENCE"],
)
update_header_status(header, "PASS")  # Illustrates caller-selected tokenless PASS.

# Keep the demonstration away from tracked evidence and clean it up afterward.
with TemporaryDirectory(prefix="step-log-example-") as directory:
    output_path = Path(directory) / "primary.log"
    write_header(output_path, header)
    append_output(
        output_path,
        "Illustrative PASS only. DEMO_REFERENCE is not claimed because its "
        "predicate was not evaluated. No real QA or acceptance is asserted.",
    )
    print(output_path.read_text(encoding="utf-8"), end="")
'''


if __name__ == "__main__":
    print("Illustrative compatibility headers only; no real QA executed.\n")
    h1 = create_header("illustrative-tokenless", "illustration only", status="PARKED")
    update_header_status(h1, "PASS")
    print("Tokenless PASS supplied for illustration:")
    print(serialize_header(h1), end="")

    h2 = create_header(
        "illustrative-explicit", "illustration only", status="PASS",
        intended_tokens=["DEMO_REFERENCE"], claimed_tokens=["DEMO_REFERENCE"],
    )
    print("Explicit aligned caller data; no registry or predicate proof:")
    print(serialize_header(h2), end="")

    update_header_status(h2, "PASS")
    print("New PASS with omitted claims clears the earlier illustrative claim:")
    print(serialize_header(h2), end="")
    print("DEMO_REFERENCE is not claimed: no predicate was evaluated for this outcome.")

    update_header_status(h2, "FAIL_BEHAVIOR")
    print("Illustrative non-PASS outcome remains claim-free:")
    print(serialize_header(h2), end="")
