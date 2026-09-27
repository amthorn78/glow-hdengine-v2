from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
_SPEC = importlib.util.spec_from_file_location(
    "check_agents_md_citations", ROOT / "ci" / "checks" / "check_agents_md_citations.py"
)
check = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(check)

TITLES = ["HDE Governance", "Glow QA Guide", "Plan Templates"]


@pytest.mark.parametrize(
    "line, kind",
    [
        ("apply PF04 rules", "pf_document_named"),
        ("see PF09.5 status", "pf_document_named"),
        ("PF10 — HDE Build Notes §2.8 applies", "pf10_locator"),
        ("PF10 v13.4 is current", "pf10_locator"),
        ("addendum PF10-CANON-001 governs", "pf10_locator"),
        ("under PF10 addendum 2.29", "pf10_locator"),
        ("addendum 2.14 says", "addendum_number"),
        ("read docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md", "pf_filename"),
        ("the Glow QA Guide requires it", "pf_title"),
        ("per hde governance", "pf_title"),
    ],
)
def test_citations_are_rejected(line: str, kind: str) -> None:
    violations = check.scan(line + "\n", TITLES)
    assert any(f":{kind}:" in row for row in violations), violations


@pytest.mark.parametrize(
    "line",
    [
        "PF10 is the canonical override and amendment mechanism.",
        "Where PF10 establishes a later rule, the applicable PF10 rule governs.",
        "search `docs/pfcanon/*.md docs/ephemeral/<CHANGE-ID>-*.md`",
        "Resolve all canon from `docs/pfcanon/` on `main`.",
        "tools/evidence/update_evidence_index.py --check",
    ],
)
def test_permitted_lines_pass(line: str) -> None:
    assert check.scan(line + "\n", TITLES) == []


def test_titles_derive_from_pfcanon_filenames(tmp_path: Path) -> None:
    for name in (
        "PF04-Canon-HDE-Governance-v2.8.6.md",
        "PF19-Canon-Glow-QA-Guide-v3.0.5.md",
        "PF10-HDE-Build-Notes-v13.4.1.md",
        "PF08-Reference-Human Design System.md",
    ):
        (tmp_path / name).write_text("x\n", encoding="utf-8")
    titles = check.pf_titles(tmp_path)
    assert "HDE Governance" in titles and "Glow QA Guide" in titles
    assert "Human Design System" in titles
    assert not any("Build Notes" in title for title in titles)


def test_repository_agents_md_passes() -> None:
    assert check.main(ROOT) == 0
