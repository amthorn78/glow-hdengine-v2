#!/usr/bin/env python3
"""PostToolUse hook: decision artifacts must carry a non-empty "Canon relied on" block.

Contract. A decision artifact is a Markdown file under docs/ephemeral/ whose file
name, or front-matter artifact_type, names a review, approval, readiness,
disposition, decision, verdict, acceptance, triage or audit. It passes when it
has a "Canon relied on" heading or label followed, before the next heading, by
content: a line with at least one letter or digit, outside HTML comments.
Lines made only of Markdown markers (fences, rules, underlines) are not content. A failing artifact produces a
"block" decision that returns the reason to the agent.

When it runs:
* at session start: records HEAD as the baseline for the first shell command;
* after Write, Edit or MultiEdit: on the file written;
* after Bash: on every docs/ephemeral Markdown file that is uncommitted and
  changed since the hook last looked, or changed by commits made since then.
  Failing files stay pending and are reported after each later Bash call until
  they pass. State is kept in .git/, never in the working tree.

Known limits, by design:
* It is advisory. It runs after the write, so it cannot prevent one, and an
  agent can ignore it. It is not a merge gate.
* It runs only in Claude Code sessions that carry this settings file.
* It checks that the block exists, not that the sections listed were read.
* A file changed by something other than this session's tool calls is judged
  at the next Bash call, not when it changes.
Binding enforcement belongs in the prompts that produce these artifacts.
Standard library and git only.
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
        after = line.split(":", 1)[1] if ":" in line else ""
        if _is_content(after):
            return True
        for follow in lines[index + 1 :]:
            if _HEADING.match(follow):
                break
            if _is_content(follow):
                return True
    return False


def _is_content(line: str) -> bool:
    # Content has at least one letter or digit; lines made only of Markdown markers do not count.
    return bool(re.search(r"[^\W_]", line))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool_input = payload.get("tool_input") or {}
    if payload.get("hook_event_name") == "SessionStart":
        _baseline(Path(os.environ.get("CLAUDE_PROJECT_DIR") or "."))
    elif payload.get("tool_name") == "Bash":
        _shell_check(Path(os.environ.get("CLAUDE_PROJECT_DIR") or "."))
    else:
        failing = [p for p in [str(tool_input.get("file_path") or "")] if _fails(p)]
        _report(failing)
    return 0


def _git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, check=True, timeout=5
    ).stdout.decode("utf-8", "replace")


def _state_file(root: Path) -> Path:
    path = Path(_git(root, "rev-parse", "--git-path", "canon_relied_on_hook.json").strip())
    return path if path.is_absolute() else root / path


def _baseline(root: Path) -> None:
    """At session start, record HEAD so the first shell command has a "before" state."""
    try:
        head = _git(root, "rev-parse", "--verify", "-q", "HEAD").strip()
        state_file = _state_file(root)
    except (OSError, subprocess.SubprocessError):
        return
    try:
        state = json.loads(state_file.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        state = {}
    state["head"] = head
    try:
        state_file.write_text(json.dumps(state, sort_keys=True), encoding="utf-8")
    except OSError:
        pass


def _shell_check(root: Path) -> None:
    """Judge docs/ephemeral Markdown files a shell command changed or committed.

    State kept under .git/ records HEAD and the hash of each uncommitted file already
    judged. A file is judged when its content differs from that record, or when it was
    changed by commits made since the recorded HEAD. Only files that pass are recorded,
    so a failing file is judged again after the next shell command.
    """
    try:
        status = _git(root, "status", "--porcelain", "-z", "--untracked-files=all", "--", "docs/ephemeral")
        head = _git(root, "rev-parse", "--verify", "-q", "HEAD").strip()
        state_file = _state_file(root)
    except (OSError, subprocess.SubprocessError):
        return
    try:
        state = json.loads(state_file.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        state = {}
    seen = state.get("files", {}) if isinstance(state.get("files"), dict) else {}
    candidates: dict[str, str | None] = {}
    for entry in status.split("\0"):
        rel = entry[3:]
        if len(entry) < 4 or "D" in entry[:2] or not rel.endswith(".md"):
            continue
        try:
            candidates[rel] = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        except OSError:
            continue
    # Committed files that failed earlier stay pending until they pass.
    for rel in state.get("pending", []) if isinstance(state.get("pending"), list) else []:
        candidates.setdefault(rel, None)
    old_head = state.get("head")
    if old_head and head and old_head != head:
        try:
            committed = _git(root, "diff", "--name-only", "-z", "--diff-filter=AM", old_head, head, "--", "docs/ephemeral")
        except (OSError, subprocess.SubprocessError):
            committed = ""
        for rel in committed.split("\0"):
            if rel.endswith(".md"):
                candidates.setdefault(rel, None)
    recorded: dict[str, str] = {}
    failing: list[str] = []
    pending: list[str] = []
    for rel, digest in candidates.items():
        if digest is not None and seen.get(rel) == digest:
            recorded[rel] = digest
            continue
        if _fails(str(root / rel)):
            failing.append(str(root / rel))
            if digest is None:
                pending.append(rel)
        elif digest is not None:
            recorded[rel] = digest
    try:
        state_file.write_text(json.dumps({"head": head, "files": recorded, "pending": pending}, sort_keys=True), encoding="utf-8")
    except OSError:
        pass
    _report(failing)


def _fails(path: str) -> bool:
    """True for a decision artifact under docs/ephemeral/ without a non-empty block."""
    if "docs/ephemeral/" not in path or not path.endswith(".md"):
        return False
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return False
    if not (_REVIEW_NAME.search(Path(path).name) or _REVIEW_TYPE.search(text[:4000])):
        return False
    return not has_block(text)


def _report(failing: list[str]) -> None:
    if not failing:
        return
    names = ", ".join(Path(p).name for p in failing)
    print(json.dumps({
        "decision": "block",
        "reason": (
            f"{names}: review or approval artifact with no non-empty "
            "'Canon relied on' block. Add one listing the PF titles and sections, and the "
            "in-flight documents, actually read for this review (AGENTS.md canon-first rule). "
            "Search canon first if you have not."
        ),
    }))


if __name__ == "__main__":
    raise SystemExit(main())
