#!/usr/bin/env python3
"""Fail when AGENTS.md cites project documents instead of stating its rules.

Product Owner rule (2026-09-27): AGENTS.md states governing rules directly. It
names no PF document except PF10, and names PF10 only by title: never by
version, addendum number, section, heading or filename. PF document titles are
derived from the files in docs/pfcanon/, so the check follows canon as it
changes. Standard library only; reads AGENTS.md and the docs/pfcanon listing.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

_PF_NUMBER = re.compile(r"\bPF(\d{1,2}(?:\.\d+)?)(?![\d.]*\d)")
_PF10_LOCATOR = re.compile(
    r"\b(?:PF10|HDE[ -]Build[ -]Notes)(?:-[A-Za-z]|\s*v\d|[^\n.;]{0,40}?(?:§\s*\d|¶\s*\d|\baddend(?:um|a)\s+\d|\b(?:sub)?sections?\s+\d|\bparagraphs?\s+\d))",
    re.IGNORECASE,
)
_PF10_VERSION = re.compile(r"\b(?:PF10|HDE[ -]Build[ -]Notes)\b[^\n.;]{0,60}?(?:\bv\d+(?:\.\d+)+|\bversion\s+\d)", re.IGNORECASE)
# PF10 followed by a dash and a title other than its own ("HDE Build Notes") cites a heading.
_PF10_HEADING = re.compile(r"\b(?:PF10|HDE[ -]Build[ -]Notes)\s*[—–:-]\s*(?!HDE[ -]Build[ -]Notes\b|PF10\b)[A-Za-z\"\'`*]")
_ADDENDUM_NUMBER = re.compile(r"\baddend(?:um|a)\s+\d+\.\d+", re.IGNORECASE)
_PFCANON_FILE = re.compile(r"docs/pfcanon/[^\s`)*]+\.md")
_TITLE_FROM_FILE = re.compile(r"^PF[\d.]*[- ]*(?:(?:Canon|Reference)-)?(.*?)(?:[- ]v\d[\w.]*)?$")


def pf_titles(pfcanon: Path) -> list[str]:
    """Distinctive titles of PF documents other than PF10."""
    titles: set[str] = set()
    for path in sorted(pfcanon.glob("*.md")):
        stem = path.stem
        if stem.startswith("PF10"):
            continue
        match = _TITLE_FROM_FILE.match(stem)
        raw = (match.group(1) if match else stem).strip(" -")
        if not raw:
            continue
        spaced = re.sub(r"\s+", " ", raw.replace("-", " ")).strip()
        # Only multi-word titles are distinctive enough to match in prose.
        if len(spaced.split()) >= 2:
            titles.add(spaced)
    return sorted(titles)


def scan(text: str, titles: list[str]) -> list[str]:
    violations: list[str] = []
    for number, line in enumerate(text.splitlines(), 1):
        for match in _PF_NUMBER.finditer(line):
            if match.group(1) != "10":
                violations.append(f"AGENTS.md:{number}:pf_document_named:{match.group(0)}")
        for match in _PF10_LOCATOR.finditer(line):
            violations.append(f"AGENTS.md:{number}:pf10_locator:{match.group(0).strip()}")
        if not _PF10_LOCATOR.search(line):
            for match in _PF10_VERSION.finditer(line):
                violations.append(f"AGENTS.md:{number}:pf10_version:{match.group(0).strip()}")
        for match in _PF10_HEADING.finditer(line):
            violations.append(f"AGENTS.md:{number}:pf10_heading:{match.group(0).strip()}")
        for match in _ADDENDUM_NUMBER.finditer(line):
            violations.append(f"AGENTS.md:{number}:addendum_number:{match.group(0)}")
        for match in _PFCANON_FILE.finditer(line):
            violations.append(f"AGENTS.md:{number}:pf_filename:{match.group(0)}")
        lowered = line.lower()
        for title in titles:
            if title.lower() in lowered:
                violations.append(f"AGENTS.md:{number}:pf_title:{title}")
    return violations


def main(root: Path = ROOT) -> int:
    agents = root / "AGENTS.md"
    if not agents.is_file():
        print("AGENTS_MD_CITATIONS_MISSING_FILE", file=sys.stderr)
        return 2
    violations = scan(agents.read_text(encoding="utf-8"), pf_titles(root / "docs" / "pfcanon"))
    if violations:
        for row in violations:
            print(row, file=sys.stderr)
        print(f"AGENTS_MD_CITATIONS_FAIL:{len(violations)}", file=sys.stderr)
        return 1
    print("AGENTS_MD_CITATIONS_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
