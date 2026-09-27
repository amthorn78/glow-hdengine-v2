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
        ("PF10 — HDE Build Notes v13.4 applies", "pf10_"),
        ("PF10 version 13.4 is current", "pf10_version"),
        ("see PF10 (v13.4)", "pf10_version"),
        ("PF10 paragraph 3 says", "pf10_locator"),
        ("HDE Build Notes §2.29 governs", "pf10_locator"),
        ("HDE Build Notes addendum 2.29 governs", "pf10_locator"),
        ("HDE Build Notes v13.4 is current", "pf10_"),
        ("PF10 subsection 2.29.1 applies", "pf10_locator"),
        ("PF10 — Repository canon authority and canon consultation", "pf10_heading"),
        ("HDE Build Notes — Repository canon authority", "pf10_heading"),
        ("PF10: repository canon authority", "pf10_heading"),
        ("**PF10** — Repository canon authority", "pf10_heading"),
        ("`PF10` §2.29 applies", "pf10_locator"),
        ("read docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md", "pf_filename"),
        ("the Glow QA Guide requires it", "pf_title"),
        ("per hde governance", "pf_title"),
    ],
)
def test_citations_are_rejected(line: str, kind: str) -> None:
    violations = check.scan(line + "\n", TITLES)
    assert any(f":{kind}" in row for row in violations), violations


@pytest.mark.parametrize(
    "line",
    [
        "PF10 is the canonical override and amendment mechanism.",
        "PF10 — HDE Build Notes is the override mechanism.",
        "HDE Build Notes is PF10's title.",
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
        "PF-Reference-Glow Story.md",
    ):
        (tmp_path / name).write_text("x\n", encoding="utf-8")
    titles = check.pf_titles(tmp_path)
    assert "HDE Governance" in titles and "Glow QA Guide" in titles
    assert "Human Design System" in titles and "Glow Story" in titles
    assert not any("Build Notes" in title for title in titles)


def test_repository_agents_md_passes() -> None:
    assert check.main(ROOT) == 0


def test_single_word_and_exact_file_names(tmp_path: Path) -> None:
    (tmp_path / "PF-Invocation.md").write_text("x\n", encoding="utf-8")
    (tmp_path / "PF10-HDE-Build-Notes-v13.4.1.md").write_text("x\n", encoding="utf-8")
    stems, single = check.pf_names(tmp_path)
    assert stems == ["PF-Invocation"] and single == ["Invocation"]
    assert any(":pf_filename:" in r for r in check.scan_names("see PF-Invocation.md\n", stems, single))
    assert any(":pf_title:" in r for r in check.scan_names("per the Invocation document\n", stems, single))
    assert check.scan_names("each prompt invocation is recorded\n", stems, single) == []


@pytest.mark.parametrize(
    ("text", "kind"),
    [
        ("PF10 governs as described in\n§2.29 of that document.\n", "pf10_locator"),
        ("Apply HDE Build Notes\nv13.4.2 here.\n", "pf10_version"),
        ("Read HDE\nGovernance first.\n", "pf_title"),
    ],
)
def test_wrapped_citations_are_rejected(text: str, kind: str) -> None:
    assert any(f":{kind}:" in row for row in check.scan(text, TITLES))


def test_list_items_are_not_joined() -> None:
    assert check.scan("PF10 governs.\n- 2 items follow\n", TITLES) == []
