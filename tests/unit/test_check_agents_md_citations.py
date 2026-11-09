from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

from tools.pf_tool_inputs.refresh import git_blob_id, write_input_set
from tools.pf_tool_inputs.resolver import MANIFEST_REL, pf_entries

ROOT = Path(__file__).resolve().parents[2]
_SPEC = importlib.util.spec_from_file_location(
    "check_agents_md_citations", ROOT / "ci" / "checks" / "check_agents_md_citations.py"
)
check = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(check)

TITLES = ["HDE Governance", "Glow QA Guide", "Plan Templates"]


# Every prohibited form found so far, one per row. Each must fail the check;
# the category reported is not asserted, only that the text is rejected.
REJECTED = [
    # PF documents other than PF10, by number
    "apply PF04 rules", "see PF09.5 status", "Read PF-04 first.", "See PF 19.",
    # PF10 with a locator, either order, any separator or emphasis
    "PF10 — HDE Build Notes §2.8 applies", "PF10 v13.4 is current", "PF10 version 13.4 is current",
    "see PF10 (v13.4)", "PF10 paragraph 3 says", "PF10 subsection 2.29.1 applies",
    "addendum PF10-CANON-001 governs", "under PF10 addendum 2.29", "`PF10` §2.29 applies",
    "HDE Build Notes §2.29 governs", "HDE Build Notes addendum 2.29 governs", "HDE Build Notes v13.4 is current",
    "HDE-Build-Notes §2.29 governs", "PF-10 section 2.29 applies.",
    "See section 2.29 of PF10.", "per § 2.30 in the HDE Build Notes", "paragraph 3 of PF10 applies",
    # PF10 by heading
    "PF10 — Repository canon authority and canon consultation", "HDE Build Notes — Repository canon authority",
    "PF10: repository canon authority", "**PF10** — Repository canon authority",
    # addendum numbers, filenames and titles
    "addendum 2.14 says", "read docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md",
    "the Glow QA Guide requires it", "per hde governance", "Read HDE-Governance first.", "See Glow-QA-Guide.",
    # soft-wrapped across lines
    "PF10 governs as described in\n§2.29 of that document.", "Apply HDE Build Notes\nv13.4.2 here.",
    "Read HDE\nGovernance first.", "Read HDE-\nGovernance first.",
    "PF10 governs as described\nin the canonical document\n§2.29 today.",
    # blockquotes wrap too; addendum numbers either way round
    "> PF10 governs as described in\n> §2.29 of that document.",
    "PF10's 2.29 addendum governs", "the 2.29 addendum in PF10 applies",
    "PF10 governs; Section 2.29 applies",
    "See Glow_QA_Guide.", "Read HDE_Governance first.",
]


@pytest.mark.parametrize("text", REJECTED)
def test_prohibited_forms_are_rejected(text: str) -> None:
    assert check.scan(text + "\n", TITLES) != []


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


def _manifest_entries(root: Path, names: tuple[str, ...]):
    """PF tool-input manifest entries for these file names (HDE-CRD-0003 S17)."""
    write_input_set(root, "0" * 40, [(name, b"x\n", git_blob_id(b"x\n")) for name in names], vendored_ids=())
    return pf_entries(root)


def test_titles_come_from_the_pf_tool_input_manifest(tmp_path: Path) -> None:
    entries = _manifest_entries(
        tmp_path,
        (
            "PF04-Canon-HDE-Governance-v2.8.6.md",
            "PF19-Canon-Glow-QA-Guide-v3.0.5.md",
            "PF10-HDE-Build-Notes-v13.4.1.md",
            "PF08-Reference-Human Design System.md",
            "PF-Reference-Glow Story.md",
        ),
    )
    titles = check.pf_titles(entries)
    assert "HDE Governance" in titles and "Glow QA Guide" in titles
    assert "Human Design System" in titles and "Glow Story" in titles
    assert not any("Build Notes" in title for title in titles)


def test_repository_agents_md_passes() -> None:
    assert check.main(ROOT) == 0


def _agents_copy(root: Path, extra: str) -> None:
    (root / "AGENTS.md").write_text((ROOT / "AGENTS.md").read_text(encoding="utf-8") + extra, encoding="utf-8")
    manifest = root / MANIFEST_REL
    manifest.parent.mkdir(parents=True)
    manifest.write_bytes((ROOT / MANIFEST_REL).read_bytes())


def test_a_cited_pf_title_is_refused(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    # HDE-CRD-0003 S17: the repository's AGENTS.md, with one sentence citing a PF title
    # from the PF tool-input manifest, is refused.
    _agents_copy(tmp_path, "\nFollow the HDE Governance rules.\n")
    assert check.main(tmp_path) == 1
    assert ":pf_title:HDE Governance" in capsys.readouterr().err


def test_a_cited_pf_file_name_is_refused(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (name,) = [e.file_name for e in pf_entries(ROOT) if e.pf_id == "PF19"]
    _agents_copy(tmp_path, f"\nThe rules are in {name}.\n")
    assert check.main(tmp_path) == 1
    assert f":pf_filename:{name.removesuffix('.md')}" in capsys.readouterr().err


def test_an_unreadable_manifest_fails_the_check(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (tmp_path / "AGENTS.md").write_text((ROOT / "AGENTS.md").read_text(encoding="utf-8"), encoding="utf-8")
    assert check.main(tmp_path) == 2
    assert "AGENTS_MD_CITATIONS_PF_INPUTS_INVALID:PF_TOOL_INPUTS_MANIFEST_MISSING" in capsys.readouterr().err


def test_single_word_and_exact_file_names(tmp_path: Path) -> None:
    entries = _manifest_entries(tmp_path, ("PF-Invocation.md", "PF10-HDE-Build-Notes-v13.4.1.md"))
    stems, single = check.pf_names(entries)
    assert stems == ["PF-Invocation"] and single == ["Invocation"]
    assert any(":pf_filename:" in r for r in check.scan_names("see PF-Invocation.md\n", stems, single))
    assert any(":pf_title:" in r for r in check.scan_names("per the Invocation document\n", stems, single))
    assert check.scan_names("each prompt invocation is recorded\n", stems, single) == []


def test_list_items_are_not_joined() -> None:
    assert check.scan("PF10 governs.\n- 2 items follow\n", TITLES) == []


def test_separate_sentences_are_not_joined() -> None:
    assert check.scan("PF10 governs where it speaks. Section 3 of the plan lists the steps.\n", TITLES) == []


@pytest.mark.parametrize(
    "text",
    ["# PF10 governs\nSection 3 of the plan lists the steps.\n", "| PF10 | x |\nSection 3 of the plan lists the steps.\n"],
)
def test_headings_and_table_rows_stand_alone(text: str) -> None:
    assert check.scan(text, TITLES) == []


def test_separate_quotes_are_not_joined() -> None:
    assert check.scan("> PF10 governs.\n\n> Section 3 of the plan lists the steps.\n", TITLES) == []
