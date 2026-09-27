#!/usr/bin/env python3
"""PostToolUse hook: review artifacts must carry a non-empty "Canon relied on" block.

Fires after Write/Edit/MultiEdit. For a file under docs/ephemeral/ that is a review, approval, readiness,
disposition, decision, verdict, acceptance, triage or audit artifact (by name or
front-matter artifact_type), it checks for a heading or label "Canon relied on"
followed by at least one non-empty line before the next heading. A missing or
empty block returns decision "block", which feeds the reason back to the agent.
It checks presence only: it cannot verify that the listed sections were read.
Standard library only; reads the one file; never writes.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

_REVIEW_NAME = re.compile(r"(review|approv|readiness|disposition|decision|verdict|acceptance|triage|audit)", re.IGNORECASE)
_REVIEW_TYPE = re.compile(r"^artifact_type:\s*\S*(REVIEW|APPROV|READINESS|DISPOSITION|DECISION|VERDICT|ACCEPTANCE|TRIAGE|AUDIT)", re.IGNORECASE | re.MULTILINE)
_LABEL = re.compile(r"^\s*(#{1,6}\s*|\*\*|[-*]\s*)?canon relied on\s*(\*\*)?\s*(:|$)", re.IGNORECASE)
_HEADING = re.compile(r"^\s*#{1,6}\s")


def has_block(text: str) -> bool:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not _LABEL.match(line):
            continue
        after = line.split(":", 1)[1].strip(" *") if ":" in line else ""
        if after:
            return True
        for follow in lines[index + 1 :]:
            if _HEADING.match(follow):
                break
            if follow.strip(" -*|\t"):
                return True
    return False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    path = str((payload.get("tool_input") or {}).get("file_path") or "")
    if "docs/ephemeral/" not in path or not path.endswith(".md"):
        return 0
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return 0
    if not (_REVIEW_NAME.search(Path(path).name) or _REVIEW_TYPE.search(text[:4000])):
        return 0
    if has_block(text):
        return 0
    print(json.dumps({
        "decision": "block",
        "reason": (
            f"{Path(path).name} is a review or approval artifact with no non-empty "
            "'Canon relied on' block. Add one listing the PF titles and sections, and the "
            "in-flight documents, actually read for this review (AGENTS.md canon-first rule). "
            "Search canon first if you have not."
        ),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
