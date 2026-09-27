#!/usr/bin/env python3
"""Fail when AGENTS.md cites project documents instead of stating its rules.

Product Owner rule (2026-09-27): AGENTS.md states governing rules directly. It
names no PF document except PF10, and names PF10 only by title: never by
version, addendum number, section, heading or filename.

Contract. The text is first rendered the way a reader sees it: Markdown emphasis
and code markers are removed, lines are joined into paragraphs following
CommonMark (headings and table rows stand alone; list items continue onto unindented
lines; consecutive quote lines form one paragraph), and paragraphs are split into sentences. Then, anywhere in AGENTS.md:

* a PF document number other than 10 ("PF04", "PF-19", "PF 09.5") fails;
* an addendum number, in either order ("addendum 2.29", "the 2.29 addendum"), fails;
* a docs/pfcanon file name, or the exact name of a PF file, fails;
* a PF title derived from the docs/pfcanon file names fails, with spaces,
  hyphens and underscores treated alike;
* a sentence that names PF10 (or "HDE Build Notes") and also carries a locator
  fails, whatever the order: a section, paragraph or pilcrow mark, a
  "section/subsection/paragraph N", a version ("v13.4", "version 13"), or a
  hyphenated identifier ("PF10-CANON-001");
* PF10 followed by a dash or colon and a title other than its own fails.

Known limits: this is a lexical check. It cannot catch a citation phrased with
no locator token (for example "the twenty-ninth addendum"), and it judges only
AGENTS.md. Standard library only; reads AGENTS.md and the docs/pfcanon listing.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

_PF10_NAME = r"(?:PF10|HDE Build Notes)"
_PF_NUMBER = re.compile(r"\bPF(\d{1,2}(?:\.\d+)?)(?![\d.]*\d)")
_LOCATOR = re.compile(
    r"[§¶]\s*\d|\b(?:sub)?sections?\s+\d|\bparagraphs?\s+\d|\bv\d+(?:\.\d+)+|\bversion\s+\d|\bPF10-[A-Za-z]",
    re.IGNORECASE,
)
_NAME = re.compile(rf"\b{_PF10_NAME}\b", re.IGNORECASE)
_HEADING = re.compile(rf"\b{_PF10_NAME}\s*[—–:-]\s*(?!{_PF10_NAME}\b)[A-Za-z\"']", re.IGNORECASE)
_ADDENDUM_NUMBER = re.compile(r"\baddend(?:um|a)\s+\d+\.\d+|\b\d+\.\d+\s+addend(?:um|a)\b", re.IGNORECASE)
_PFCANON_FILE = re.compile(r"docs/pfcanon/[^\s)]+\.md")
_SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\"'])")
_SINGLE_LINE_BLOCK = re.compile(r"^(?:#|\|)")
_BLOCK_START = re.compile(r"^(?:#|[-+*]\s|\||>|\d+[.)]\s)")
_TITLE_FROM_FILE = re.compile(r"^PF[\d.]*[- ]*(?:(?:Canon|Reference)-)?(.*?)(?:[- ]v\d[\w.]*)?$")


def _title_words(stem: str) -> list[str]:
    match = _TITLE_FROM_FILE.match(stem)
    return (match.group(1) if match else stem).replace("-", " ").split()


def pf_titles(pfcanon: Path) -> list[str]:
    """Multi-word titles of PF documents other than PF10."""
    titles = {" ".join(_title_words(p.stem)) for p in pfcanon.glob("*.md") if not p.stem.startswith("PF10")}
    return sorted(t for t in titles if len(t.split()) >= 2)


def pf_names(pfcanon: Path) -> tuple[list[str], list[str]]:
    """Exact PF file names (without .md) and single-word PF titles."""
    stems = sorted(p.stem for p in pfcanon.glob("*.md") if not p.stem.startswith("PF10"))
    single = [words[0] for words in map(_title_words, stems) if len(words) == 1]
    return stems, single


def _normalize(text: str) -> str:
    text = re.sub(r"[*`]", "", text)
    text = text.replace("_", " ")  # underscores separate words, as in "HDE_Governance"
    text = re.sub(r"\bPF[\s-]?(\d)", r"PF\1", text)
    return re.sub(r"\bHDE[\s-]+Build[\s-]+Notes\b", "HDE Build Notes", text, flags=re.IGNORECASE)


def _units(text: str) -> list[tuple[int, str]]:
    """Rendered sentences with the source line each starts on."""
    units: list[tuple[int, str]] = []
    paragraph: list[tuple[int, str]] = []
    in_quote = False

    def flush() -> None:
        if not paragraph:
            return
        joined, starts = "", []
        for number, line in paragraph:
            starts.append((len(joined), number))
            joined += line + " "
        position = 0
        for sentence in _SENTENCE_END.split(joined):
            offset = joined.index(sentence, position)
            position = offset + len(sentence)
            line = max(n for start, n in starts if start <= offset)
            units.append((line, sentence.strip()))
        paragraph.clear()

    for number, raw in enumerate(text.splitlines(), 1):
        line = _normalize(raw).strip()
        quoted = line.startswith(">")
        # A quote line continues the quote paragraph above it; other block starts begin a new one.
        continues_quote = quoted and paragraph and in_quote
        line = line.lstrip("> ").strip() if quoted else line
        if not line or (_BLOCK_START.match(line) or quoted) and not continues_quote:
            flush()
        in_quote = quoted or (in_quote and bool(line))
        if line:
            paragraph.append((number, line))
        if _SINGLE_LINE_BLOCK.match(line):
            flush()  # headings and table rows never continue onto the next line
    flush()
    return units


def scan(text: str, titles: list[str]) -> list[str]:
    violations: list[str] = []
    title_patterns = [(t, re.compile(r"\b" + r"[\s_-]+".join(map(re.escape, t.split())) + r"\b", re.IGNORECASE)) for t in titles]
    for number, sentence in _units(text):
        where = f"AGENTS.md:{number}"
        for match in _PF_NUMBER.finditer(sentence):
            if match.group(1) != "10":
                violations.append(f"{where}:pf_document_named:{match.group(0)}")
        for match in _ADDENDUM_NUMBER.finditer(sentence):
            violations.append(f"{where}:addendum_number:{match.group(0)}")
        if _NAME.search(sentence) and (locator := _LOCATOR.search(sentence)):
            violations.append(f"{where}:pf10_locator:{locator.group(0)}")
        for match in _HEADING.finditer(sentence):
            violations.append(f"{where}:pf10_heading:{match.group(0)}")
        for match in _PFCANON_FILE.finditer(sentence):
            violations.append(f"{where}:pf_filename:{match.group(0)}")
        for title, pattern in title_patterns:
            if pattern.search(sentence):
                violations.append(f"{where}:pf_title:{title}")
    return violations


def scan_names(text: str, stems: list[str], single: list[str]) -> list[str]:
    violations: list[str] = []
    for number, sentence in _units(text):
        for stem in stems:
            if stem.lower() in sentence.lower():
                violations.append(f"AGENTS.md:{number}:pf_filename:{stem}")
        for word in single:
            if re.search(rf"\bthe\s+{re.escape(word)}\s+(?:document|doc|file|guide)\b", sentence, re.IGNORECASE):
                violations.append(f"AGENTS.md:{number}:pf_title:{word}")
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
