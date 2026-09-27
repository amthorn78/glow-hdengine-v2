#!/usr/bin/env python3
"""PostToolUse hook: review artifacts must carry a non-empty "Canon relied on" block.

Fires after Write/Edit/MultiEdit, and after Bash for the uncommitted docs/ephemeral files whose content changed since the hook last looked. For a file under docs/ephemeral/ that is a review, approval, readiness,
disposition, decision, verdict, acceptance, triage or audit artifact (by name or
front-matter artifact_type), it checks for a heading or label "Canon relied on"
followed by at least one non-empty line before the next heading. A missing or
empty block returns decision "block", which feeds the reason back to the agent.
It checks presence only: it cannot verify that the listed sections were read.
Standard library only. It never writes to the repository; it keeps a small hash record inside .git/.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import re
import sys
from pathlib import Path

_REVIEW_NAME = re.compile(r"(review|approv|readiness|disposition|decision|verdict|acceptance|triage|audit)", re.IGNORECASE)
_REVIEW_TYPE = re.compile(r"^artifact_type:\s*\S*(REVIEW|APPROV|READINESS|DISPOSITION|DECISION|VERDICT|ACCEPTANCE|TRIAGE|AUDIT)", re.IGNORECASE | re.MULTILINE)
_LABEL = re.compile(r"^\s*(#{1,6}\s*|\*\*|[-*]\s*)?canon relied on\s*(\*\*)?\s*(:|$)", re.IGNORECASE)
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
        # Shell writes: compare the working tree's changed docs/ephemeral Markdown files
        # with the state last seen, so only files whose content this command changed are judged.
        paths = _changed_by_shell()
    else:
        paths = [str(tool_input.get("file_path") or "")]
    for path in dict.fromkeys(paths):
        if _check(path):
            return 0
    return 0


def _changed_by_shell() -> list[str]:
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or ".")
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain", "-z", "--untracked-files=all", "--", "docs/ephemeral"],
            capture_output=True, check=True, timeout=5,
        ).stdout.decode("utf-8", "replace")
        state_file = Path(subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--git-path", "canon_relied_on_hook.json"],
            capture_output=True, check=True, timeout=5,
        ).stdout.decode().strip())
    except (OSError, subprocess.SubprocessError):
        return []
    if not state_file.is_absolute():
        state_file = root / state_file
    try:
        seen = json.loads(state_file.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        seen = {}
    current: dict[str, str] = {}
    changed: list[str] = []
    for entry in out.split("\0"):
        rel = entry[3:]
        if len(entry) < 4 or entry[:2].strip() == "D" or not rel.endswith(".md"):
            continue
        path = root / rel
        try:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError:
            continue
        current[rel] = digest
        if seen.get(rel) != digest:
            changed.append(str(path))
    try:
        state_file.write_text(json.dumps(current, sort_keys=True), encoding="utf-8")
    except OSError:
        pass
    return changed


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
