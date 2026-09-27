#!/usr/bin/env python3
"""PostToolUse hook: review artifacts must carry a non-empty "Canon relied on" block.

Fires after Write/Edit/MultiEdit, and after Bash for the docs/ephemeral files a command names and just modified. For a file under docs/ephemeral/ that is a review, approval, readiness,
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
import time
from pathlib import Path

_REVIEW_NAME = re.compile(r"(review|approv|readiness|disposition|decision|verdict|acceptance|triage|audit)", re.IGNORECASE)
_REVIEW_TYPE = re.compile(r"^artifact_type:\s*\S*(REVIEW|APPROV|READINESS|DISPOSITION|DECISION|VERDICT|ACCEPTANCE|TRIAGE|AUDIT)", re.IGNORECASE | re.MULTILINE)
_LABEL = re.compile(r"^\s*(#{1,6}\s*|\*\*|[-*]\s*)?canon relied on\s*(\*\*)?\s*(:|$)", re.IGNORECASE)
_BASH_PATH = re.compile(r"[^\s'\"<>|;&]*docs/ephemeral/[^\s'\"<>|;&]+\.md")
_HEADING = re.compile(r"^\s*#{1,6}\s")


_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def has_block(text: str) -> bool:
    # HTML comments (template placeholders) are not attribution.
    lines = _COMMENT.sub("", text).splitlines()
    for index, line in enumerate(lines):
        if not _LABEL.match(line):
            continue
        after = line.split(":", 1)[1].strip(" *") if ":" in line else ""
        if after:
            return True
        for follow in lines[index + 1 :]:
            if _HEADING.match(follow):
                break
            if follow.strip(" -*|\t`~>_"):
                return True
    return False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool_input = payload.get("tool_input") or {}
    if payload.get("tool_name") == "Bash":
        # Shell writes: check every docs/ephemeral Markdown file the command names.
        # Only files the command just changed: a read-only command must not re-judge old records.
        cutoff = time.time() - 30
        paths = [
            p for p in _BASH_PATH.findall(str(tool_input.get("command") or ""))
            if Path(p).is_file() and Path(p).stat().st_mtime >= cutoff
        ]
    else:
        paths = [str(tool_input.get("file_path") or "")]
    for path in dict.fromkeys(paths):
        if _check(path):
            return 0
    return 0


def _check(path: str) -> bool:
    """Print a block decision for one file; return True when it did."""
    if "docs/ephemeral/" not in path or not path.endswith(".md"):
        return False
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return False
    if not (_REVIEW_NAME.search(Path(path).name) or _REVIEW_TYPE.search(text[:4000])):
        return False
    if has_block(text):
        return False
    print(json.dumps({
        "decision": "block",
        "reason": (
            f"{Path(path).name} is a review or approval artifact with no non-empty "
            "'Canon relied on' block. Add one listing the PF titles and sections, and the "
            "in-flight documents, actually read for this review (AGENTS.md canon-first rule). "
            "Search canon first if you have not."
        ),
    }))
    return True


if __name__ == "__main__":
    raise SystemExit(main())
