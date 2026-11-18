"""Command-existence test of the operator runbooks (HDE-EPIC043 WU-PR-06; HDE-COAG003.1).

Every command path the runbooks name exists in the tree. A named command is a
token of a fenced ``bash``, ``sh`` or ``text`` block, or of an inline code span,
that is a repository path: it contains ``/``, or it is a bare ``.py`` or ``.sh``
file name; tokens holding a placeholder (``<…>``), a variable (``$``), an
assignment (``=``), a URL (``://``), a glob or a brace, absolute paths and option
flags are not paths. A token after ``python -m`` is a module name and must be
importable. Prose that names no such token is outside the test.
"""
from __future__ import annotations

import importlib.util
import re
import shlex
from pathlib import Path

from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS

ROOT = Path(__file__).resolve().parents[2]
RUNBOOK_DIR = ROOT / "docs/runbooks"
RUNBOOKS = ("build_verify_release_rollback.md", "incidents.md")
_FENCE = re.compile(r"^```(?P<info>\S*)\s*$")
_INLINE = re.compile(r"`([^`\n]+)`")
_EXCLUDED = ("://", "<", ">", "$", "*", "{", "}", "=")


def _code_lines(text: str) -> list[str]:
    lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        match = _FENCE.match(line.strip())
        if match:
            fence = None if fence is not None else match["info"]
            continue
        if fence is not None:
            if fence in ("bash", "sh", "text"):
                lines.append(line.strip())
        else:
            lines.extend(_INLINE.findall(line))
    return lines


def _tokens(line: str) -> list[str]:
    try:
        return shlex.split(line)
    except ValueError:
        return line.split()


def named_commands(text: str) -> tuple[list[str], list[str]]:
    """Return (paths, modules) named in a runbook text."""
    paths: list[str] = []
    modules: list[str] = []
    for line in _code_lines(text):
        tokens = _tokens(line)
        for index, token in enumerate(tokens):
            if index > 0 and tokens[index - 1] == "-m" and index > 1 and tokens[index - 2].startswith("python"):
                modules.append(token)
                continue
            if any(mark in token for mark in _EXCLUDED) or token.startswith(("/", "-")):
                continue
            if "/" in token or token.endswith((".py", ".sh")):
                paths.append(token.rstrip(".,;:"))
    return paths, modules


def missing_commands(text: str, root: Path = ROOT) -> list[str]:
    paths, modules = named_commands(text)
    missing = [path for path in paths if not (root / path).exists()]
    missing += [module for module in modules if importlib.util.find_spec(module) is None]
    return missing


def test_runbooks_are_the_two_governed_files():
    assert sorted(path.name for path in RUNBOOK_DIR.iterdir()) == sorted(RUNBOOKS)


def test_every_command_the_runbooks_name_exists():
    for name in RUNBOOKS:
        text = (RUNBOOK_DIR / name).read_text(encoding="utf-8")
        paths, _ = named_commands(text)
        assert paths, f"{name} names no command"
        assert missing_commands(text) == [], name


def test_the_release_runbook_names_the_harness_and_the_check_forms():
    paths, modules = named_commands((RUNBOOK_DIR / RUNBOOKS[0]).read_text(encoding="utf-8"))
    for path in (
        "scripts/ops/post_deploy_smoke.py",
        "scripts/m10_cutover_guard.py",
        "scripts/release_id_recompute.py",
        "ci/checks/check_release_identity.sh",
        "tools/evidence/build_release_attestation.py",
        "tools/evidence/update_evidence_index.py",
        "ci/checks/check_mirror_schema.sh",
    ):
        assert path in paths
    assert {"pip", "pytest"} <= set(modules)


def test_a_runbook_naming_an_absent_path_fails_on_that_path(tmp_path):
    text = "```bash\npython scripts/does_not_exist.py --check\n```\n"
    assert missing_commands(text) == ["scripts/does_not_exist.py"]
    assert missing_commands("Run `scripts/ops/post_deploy_smoke.py`.\n") == []


def test_the_runbooks_name_no_retired_database_transport_key():
    for name in RUNBOOKS:
        text = (RUNBOOK_DIR / name).read_text(encoding="utf-8")
        assert not [key for key in RETIRED_DB_TRANSPORT_KEYS if key in text], name
