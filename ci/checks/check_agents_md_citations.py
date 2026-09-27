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
# The reverse order: "section 2.29 of PF10".
_PF10_REVERSE = re.compile(
    r"(?:[§¶]\s*|\baddend(?:um|a)\s+|\b(?:sub)?sections?\s+|\bparagraphs?\s+)\d+(?:\.\d+)*[^\n.;]{0,40}?\b(?:of|in|from)\s+(?:the\s+)?(?:PF10|HDE[ -]Build[ -]Notes)\b",
    re.IGNORECASE,
)
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


def pf_names(pfcanon: Path) -> tuple[list[str], list[str]]:
    """Exact PF file names (without .md) and single-word PF titles."""
    stems: list[str] = []
    single: list[str] = []
    for path in sorted(pfcanon.glob("*.md")):
        if path.stem.startswith("PF10"):
            continue
        stems.append(path.stem)
        match = _TITLE_FROM_FILE.match(path.stem)
        raw = (match.group(1) if match else path.stem).strip(" -")
        words = raw.replace("-", " ").split()
        if len(words) == 1:
            single.append(words[0])
    return stems, single


def scan_names(text: str, stems: list[str], single: list[str]) -> list[str]:
    violations: list[str] = []
    for number, line in enumerate(text.splitlines(), 1):
        lowered = line.lower()
        for stem in stems:
            if stem.lower() in lowered:
                violations.append(f"AGENTS.md:{number}:pf_filename:{stem}")
        for word in single:
            if re.search(rf"\bthe\s+{re.escape(word)}\s+(?:document|doc|file|guide)\b", line, re.IGNORECASE):
                violations.append(f"AGENTS.md:{number}:pf_title:{word}")
    return violations


def _wrapped_pairs(text: str) -> list[tuple[int, str, int]]:
    """Adjacent prose lines joined as Markdown renders them: (line number, joined text, boundary)."""
    lines = [raw.replace("*", "").replace("`", "") for raw in text.splitlines()]
    pairs: list[tuple[int, str, int]] = []
    for index in range(len(lines) - 1):
        first, second = lines[index].rstrip(), lines[index + 1].strip()
        if not first.strip() or not second or second.startswith(("#", "-", "|", ">")) or re.match(r"\d+[.)]\s", second):
            continue
        pairs.append((index + 1, f"{first} {second}", len(first)))
    return pairs


def scan(text: str, titles: list[str]) -> list[str]:
    violations = _scan_lines(text, titles)
    # A citation split across a soft line break is still one citation.
    patterns = [
        ("pf_document_named", _PF_NUMBER),
        ("pf10_locator", _PF10_LOCATOR),
        ("pf10_version", _PF10_VERSION),
        ("pf10_heading", _PF10_HEADING),
        ("pf10_locator", _PF10_REVERSE),
        ("addendum_number", _ADDENDUM_NUMBER),
    ] + [("pf_title", re.compile(re.escape(title).replace(r"\ ", r"[\s_-]+"), re.IGNORECASE)) for title in titles]
    for number, joined, boundary in _wrapped_pairs(text):
        for label, pattern in patterns:
            for match in pattern.finditer(joined):
                if match.start() < boundary < match.end():
                    if label == "pf_document_named" and match.group(1) == "10":
                        continue
                    violations.append(f"AGENTS.md:{number}:{label}:{' '.join(match.group(0).split())}")
    return violations


def _scan_lines(text: str, titles: list[str]) -> list[str]:
    violations: list[str] = []
    for number, raw_line in enumerate(text.splitlines(), 1):
        # Emphasis and code markers must not hide a citation.
        line = raw_line.replace("*", "").replace("`", "")
        for match in _PF_NUMBER.finditer(line):
            if match.group(1) != "10":
                violations.append(f"AGENTS.md:{number}:pf_document_named:{match.group(0)}")
        for match in _PF10_LOCATOR.finditer(line):
            violations.append(f"AGENTS.md:{number}:pf10_locator:{match.group(0).strip()}")
        if not _PF10_LOCATOR.search(line):
            for match in _PF10_VERSION.finditer(line):
                violations.append(f"AGENTS.md:{number}:pf10_version:{match.group(0).strip()}")
        if not _ADDENDUM_NUMBER.search(line):
            for match in _PF10_REVERSE.finditer(line):
                violations.append(f"AGENTS.md:{number}:pf10_locator:{match.group(0).strip()}")
        for match in _PF10_HEADING.finditer(line):
            violations.append(f"AGENTS.md:{number}:pf10_heading:{match.group(0).strip()}")
        for match in _ADDENDUM_NUMBER.finditer(line):
            violations.append(f"AGENTS.md:{number}:addendum_number:{match.group(0)}")
        for match in _PFCANON_FILE.finditer(line):
            violations.append(f"AGENTS.md:{number}:pf_filename:{match.group(0)}")
        # Hyphens and spaces are equivalent separators in PF titles ("HDE-Governance").
        lowered = re.sub(r"[\s_-]+", " ", line.lower())
        for title in titles:
            if title.lower() in lowered:
                violations.append(f"AGENTS.md:{number}:pf_title:{title}")
    return violations


def main(root: Path = ROOT) -> int:
    agents = root / "AGENTS.md"
    if not agents.is_file():
        print("AGENTS_MD_CITATIONS_MISSING_FILE", file=sys.stderr)
        return 2
    text = agents.read_text(encoding="utf-8")
    pfcanon = root / "docs" / "pfcanon"
    violations = scan(text, pf_titles(pfcanon)) + scan_names(text, *pf_names(pfcanon))
    if violations:
        for row in violations:
            print(row, file=sys.stderr)
        print(f"AGENTS_MD_CITATIONS_FAIL:{len(violations)}", file=sys.stderr)
        return 1
    print("AGENTS_MD_CITATIONS_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
