"""Guard: no tracked tool or test reads the code repository's deleted docs/pfcanon/ tree (HDE-CRD-0003 S17, RK-12).

The CI workflow's path filter ignores docs/pfcanon/**, so a reader of that tree, or a tree
re-added there, would again go unseen. PF documents that tools and tests read come from the
PF tool inputs (tools/pf_tool_inputs/). This guard is lexical: it finds every mention of the
tree in tracked Python and shell files and admits only the reviewed mentions below, each of
which names the path without reading from it. A reader that builds the path without the word
is not detected; that is its stated limit.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SELF = "tests/tools/test_pf_document_reader_guard.py"
# The authoritative PF home, docs/hde/pfcanon/ in amthorn78/glow-docs, is not a code-repository path.
MENTION = re.compile(r"(?<!hde/)pfcanon", re.IGNORECASE)

# (path, exact stripped line): reviewed mentions that name docs/pfcanon/ without reading it.
ALLOWED: dict[tuple[str, str], str] = {
    ("ci/checks/check_agents_md_citations.py", "* a docs/pfcanon file path, or the exact name of a PF file, fails;"):
        "docstring of the AGENTS.md refusal",
    ("ci/checks/check_agents_md_citations.py", '_PFCANON_FILE = re.compile(r"docs/pfcanon/[^\\s)]+\\.md")'):
        "refusal pattern for a cited path",
    ("ci/checks/check_agents_md_citations.py", "for match in _PFCANON_FILE.finditer(sentence):"):
        "use of that refusal pattern",
    ("ci/checks/check_direct_db_contract.py", '"docs/pfcanon/",'):
        "scan exclusion",
    ("ci/checks/classify_ci_changes.py", '"docs/pfcanon/",'):
        "documentation prefix, which returns no lanes (WU-PR-01 instruction section 6)",
    (
        "tests/charts/test_chart_loader_import_guard.py",
        '["git", "ls-files", "-z", "--", "*.py", ":(exclude)docs/ephemeral/", ":(exclude)docs/pfcanon/"],',
    ): "pathspec exclusion",
    ("tests/qa/test_epic029_requalification.py", '"docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.1.md",'):
        "protected-path parameter of a refusal test",
    (
        "tests/qa/test_generate_epic_close_pack.py",
        'assert [path for path in inputs if path.startswith(("docs/ephemeral/", "docs/pfcanon/", "tools/pf_tool_inputs/"))] == []',
    ): "assertion that no pack binds the path",
    (
        "tests/qa/test_generate_epic_close_pack.py",
        'assert "docs/ephemeral" not in report and "docs/pfcanon" not in report and "tools/pf_tool_inputs" not in report',
    ): "assertion that no report names the path",
    ("tests/qa/test_generate_epic_close_pack.py", '"docs/pfcanon/PF30.1-Canon-HDE-CRD-Records-v0.9.2.md",'):
        "refused causal-input parameter",
    ("tests/qa/test_generate_epic_close_pack.py", '"docs/PFCanon/PF10-HDE-Build-Notes-v13.9.md",'):
        "refused causal-input parameter",
    (
        "tests/qa/test_generate_epic_close_pack.py",
        'for name, plan in (("ephemeral", "docs/ephemeral/HDE-EPIC123-implementation-plan-v1.0.md"), '
        '("canon", "docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.5.md")):',
    ): "refused plan-path parameters",
    ("tests/unit/test_check_agents_md_citations.py", '"addendum 2.14 says", "read docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md",'):
        "refused AGENTS.md sample",
    ("tests/unit/test_check_agents_md_citations.py", '"search `docs/pfcanon/*.md docs/ephemeral/<CHANGE-ID>-*.md`",'):
        "permitted AGENTS.md sample",
    ("tests/unit/test_check_agents_md_citations.py", '"Resolve all canon from `docs/pfcanon/` on `main`.",'):
        "permitted AGENTS.md sample",
    (
        "tools/ci/prepush_check.py",
        '_REPLAY_PATHS = ["**", "!docs/crd/**", "!docs/ephemeral/**", "!docs/graph/**", "!docs/pfcanon/**", "!docs/plans/**",',
    ): "replay of the workflow path filter, until WU-PR-02 removes replay",
    ("tools/qa/generate_epic026_close_pack.py", 'PF23_PATH = ROOT / "docs" / "pfcanon" / "PF23-Canon-Reality-Audits-v1.0.3.md"'):
        "D-18: retired reader with no caller, fail-closed in the classifier (WU-PR-01 instruction section 6)",
    ("tools/qa/generate_epic029_close_pack.py", 'or primary_rel.startswith("docs/pfcanon/")'):
        "protected-prefix test",
    (
        "tools/qa/generate_epic_close_pack.py",
        "# under docs/pfcanon/ changes version at any time, so neither is ever a causal input, pointer or",
    ): "comment on the refusal pattern",
    ("tools/qa/generate_epic_close_pack.py", 'r"(?:docs/(?:ephemeral|pfcanon)|tools/pf_tool_inputs)(?:/|\\Z)", re.IGNORECASE'):
        "refusal pattern for a causal input",
}

# Reader lines as they stood on main at eaa2685, before HDE-CRD-0003 S17.
BASELINE_READER_LINES = (
    '/ "pfcanon"',
    '(config.repo_root / "docs" / "pfcanon").glob(',
    'BUILD_NOTES_PATTERN = "docs/pfcanon/PF10-HDE-Build-Notes-v*.md"',
    'pfcanon = root / "docs" / "pfcanon"',
    'pf04_paths = sorted(Path("docs/pfcanon").glob("PF04-Canon-HDE-Governance-*.md"))',
    'r"docs/pfcanon/PF(?:[0-9]{2}(?:\\.[0-9]+)?)?[- ]+(?:(?:Canon|Reference)[- ]+)?"',
)


def _tracked(*pathspecs: str) -> list[str]:
    output = subprocess.run(
        ["git", "ls-files", "-z", "--", *pathspecs], cwd=ROOT, capture_output=True, check=True
    ).stdout.decode("utf-8")
    return [path for path in output.split("\0") if path]


def _unlisted(path: str, lines: list[str]) -> list[str]:
    return [
        f"{path}:{number}:{line.strip()}"
        for number, line in enumerate(lines, 1)
        if MENTION.search(line) and (path, line.strip()) not in ALLOWED
    ]


def test_no_docs_pfcanon_tree_is_tracked() -> None:
    assert _tracked("docs/pfcanon/") == []


def test_no_tracked_tool_or_test_reads_docs_pfcanon() -> None:
    found: set[tuple[str, str]] = set()
    unlisted: list[str] = []
    for path in _tracked("*.py", "*.sh"):
        if path.startswith("docs/") or path == SELF:
            continue
        lines = (ROOT / path).read_text(encoding="utf-8", errors="replace").splitlines()
        unlisted += _unlisted(path, lines)
        found.update((path, line.strip()) for line in lines if MENTION.search(line))
    assert unlisted == [], "read PF documents through tools/pf_tool_inputs/resolver.py"
    assert sorted(set(ALLOWED) - found) == [], "remove allowlist entries that no longer occur"


def test_the_guard_refuses_the_baseline_readers() -> None:
    for line in BASELINE_READER_LINES:
        assert _unlisted("tools/qa/qa_harness.py", [line]) != [], line
