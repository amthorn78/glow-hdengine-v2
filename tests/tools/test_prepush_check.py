"""Owner test for tools/ci/prepush_check.py (HDE-CRD-0002 S20).

Fast and hermetic: it never runs the repository's own test suite, a real lane
step or the attestation build.  Reports run against throwaway clones of this
repository or small synthetic git repositories under ``tmp_path``, and every
run proves that the repository it read is byte-identical before and after,
ignored files and ``.git`` included.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path, PurePosixPath

import pytest

from ci.checks import classify_ci_changes as classifier

_BYTECODE = sys.dont_write_bytecode
from tools.ci import prepush_check as tool  # noqa: E402

sys.dont_write_bytecode = _BYTECODE

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/ci/prepush_check.py"
WORKFLOW = ROOT / ".github/workflows/ci.yml"
IDENTITY = ("-c", "user.name=prepush-test", "-c", "user.email=prepush-test@invalid", "-c", "commit.gpgsign=false",
            "-c", "maintenance.auto=false", "-c", "gc.auto=0")
# The keys the tool must remove from every child, stated independently of the
# tool's own list (instruction ID-9, plus the ENGINE_ENV alias).
CHILD_KEYS = ("DATABASE_URL", "GEO_API_KEY", "HD_API_KEY", "HDAPI_KEY", "HDAPI_BASE_URL", "HD_API_BASE_URL",
              "HD_GEOCODE_KEY", "HDE_VENDOR_OVERRIDE_AUDIT_PATH", "GH_TOKEN", "GITHUB_TOKEN", "ENGINE_ENV")
DUMMY_KEYS = {key: "dummy-not-a-secret" for key in CHILD_KEYS}


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *IDENTITY, *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def _snapshot(root: Path) -> dict[str, tuple[object, ...]]:
    """Every file and directory under ``root``, ignored files and .git included.

    Any write to an entry changes its ``st_ctime_ns``, which user space cannot
    set back, and creating or removing an entry changes its directory's
    ``st_mtime_ns``; git metadata outside ``objects/`` is also compared by content.
    """
    state: dict[str, tuple[object, ...]] = {}
    top = str(root)
    for directory, dirnames, filenames in os.walk(top):
        for name in (*dirnames, *filenames):
            full = os.path.join(directory, name)
            info = os.lstat(full)
            rel = os.path.relpath(full, top)
            entry: tuple[object, ...] = (info.st_mode, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)
            if name in filenames and rel.startswith(".git/") and not rel.startswith(".git/objects/") \
                    and not os.path.islink(full):
                with open(full, "rb") as stream:
                    entry += (hashlib.sha256(stream.read()).hexdigest(),)
            state[rel] = entry
    info = os.lstat(top)
    state["."] = (info.st_mode, info.st_ino, info.st_mtime_ns, info.st_ctime_ns)
    return state


def _run(repo: Path, *args: str, extra_env: dict[str, str] | None = None,
         tool_path: Path = TOOL) -> subprocess.CompletedProcess[str]:
    """Run the tool against ``repo`` and assert the read-only rule around it."""
    env = {**os.environ, **DUMMY_KEYS, **(extra_env or {})}
    before = _snapshot(repo)
    result = subprocess.run([sys.executable, str(tool_path), *args, "--repo-root", str(repo)],
                            env=env, capture_output=True, text=True, check=False, timeout=300)
    assert _snapshot(repo) == before, result.stdout + result.stderr
    assert not (repo / ".git/worktrees").exists()
    for value in DUMMY_KEYS.values():
        assert value not in result.stdout + result.stderr
    return result


def _clone(destination: Path) -> Path:
    head = _git(ROOT, "rev-parse", "HEAD")
    subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", "--no-checkout", str(ROOT), str(destination)],
                   check=True, capture_output=True)
    _git(destination, "-c", "advice.detachedHead=false", "checkout", "--quiet", "--detach", head)
    # An ignored file the read-only rule must also cover.
    (destination / "tests/__pycache__").mkdir(exist_ok=True)
    (destination / "tests/__pycache__/sentinel.cpython-312.pyc").write_bytes(b"\x00sentinel")
    return destination


@pytest.fixture(scope="module")
def repo_clone(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return _clone(tmp_path_factory.mktemp("prepush") / "clone")


def _synthetic(root: Path, files: dict[str, str]) -> Path:
    root.mkdir(parents=True)
    for rel, body in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(body), encoding="utf-8")
    _git(root, "init", "--quiet", "--initial-branch=main")
    _git(root, "add", "-A")
    _git(root, "commit", "--quiet", "-m", "fixture")
    return root


def _report_lines(stdout: str, report: str) -> list[str]:
    prefix = f"{report}: "
    return [line[len(prefix):] for line in stdout.splitlines() if line.startswith(prefix)]


# --------------------------------------------------------------------------
# workflow parser (parse_workflow, parse_jobs), which sweep uses; read on a fixed excerpt so
# that a change to .github/workflows/ci.yml needs no change here (HDE-CRD-0003 S11)
# --------------------------------------------------------------------------

# .github/workflows/ci.yml lines 1-78 at 996fa276, verbatim except the two path-filter entries for the
# PF documents directory: the header, the test job's settings and its first three steps hold every form the parser
# tests below read.
PARSER_WORKFLOW = """\
name: ci

on:
  pull_request:
    paths:
      - '**'
      - '!docs/crd/**'
      - '!docs/ephemeral/**'
      - '!docs/graph/**'
      - '!docs/plans/**'
      - '!docs/prompt_ecosystem_management/**'
      - '!docs/qa/**'
      - '!docs/run/**'
      - '**.path_proof.txt'
      - 'docs/run/EPIC011_TEST_IDENTITIES.md'
      - 'docs/run/PROD_ENDPOINTS.json'
  push:
    branches:
      - main
    paths:
      - '**'
      - '!docs/crd/**'
      - '!docs/ephemeral/**'
      - '!docs/graph/**'
      - '!docs/plans/**'
      - '!docs/prompt_ecosystem_management/**'
      - '!docs/qa/**'
      - '!docs/run/**'
      - '**.path_proof.txt'
      - 'docs/run/EPIC011_TEST_IDENTITIES.md'
      - 'docs/run/PROD_ENDPOINTS.json'

permissions:
  contents: read

concurrency:
  group: ci-${{ github.workflow }}-${{ github.event.pull_request.number || github.run_id }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      LC_ALL: C
      LANG: C
      TZ: UTC
      SAFE_MODE: "1"
      ALLOW_NETWORK: "0"
      APP_ENV: dev
      PYTHONDONTWRITEBYTECODE: "1"
    steps:
      - name: Check out exact candidate head
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false
          ref: ${{ github.event.pull_request.head.sha || github.sha }}

      - name: Classify affected CI lanes
        id: classify
        shell: bash
        env:
          BASE_SHA: ${{ github.event.pull_request.base.sha || github.event.before }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha || github.sha }}
        run: |
          set -euo pipefail
          python3 ci/checks/classify_ci_changes.py \\
            --base "$BASE_SHA" \\
            --head "$HEAD_SHA" \\
            --event-name "${{ github.event_name }}" \\
            --github-output "$GITHUB_OUTPUT" \\
            --changed-tests-output "$RUNNER_TEMP/ci-changed-test-targets.txt"

      - name: Check AGENTS.md cites no project documents
        shell: bash
        run: python3 ci/checks/check_agents_md_citations.py
"""


def test_a_temporary_directory_inside_the_repository_is_refused_before_anything_is_created(tmp_path: Path) -> None:
    repo = _synthetic(tmp_path / "temp-inside", {"data.txt": "tracked\n"})
    (repo / "scratch").mkdir()  # empty, so git status stays clean
    result = _run(repo, "build-notes", extra_env={"TMPDIR": str(repo / "scratch")})
    assert result.returncode == tool.EXIT_REFUSED, result.stdout + result.stderr
    assert "PREPUSH_CHECK_REFUSED: the temporary directory would be inside the repository" in result.stderr
    assert not any((repo / "scratch").iterdir())


def test_a_step_that_is_not_a_mapping_is_refused() -> None:
    text = PARSER_WORKFLOW
    mutated = text.replace("      - name: Check AGENTS.md cites no project documents",
                           "      - echo hi\n\n      - name: Check AGENTS.md cites no project documents")
    assert mutated != text
    with pytest.raises(tool.ToolingError, match="unsupported shape"):
        tool.parse_jobs(mutated)
    nested_job_env = text.replace("      APP_ENV: dev\n", "      APP_ENV:\n        nested: invalid\n", 1)
    assert nested_job_env != text
    with pytest.raises(tool.ToolingError, match="unsupported shape"):
        tool.parse_jobs(nested_job_env)


@pytest.mark.parametrize("value", ["{nested: invalid}", "[a, b]", "&anchor x", "*alias", "!tag x", "|+", ">2",
                                   '"echo replay_pass\\nexit 1"', '"unterminated', "'a' b", "a: b", "- x", "# c",
                                   "]", "}", ",x", "] x", "-\tx", "?\tx", ":\tx", "? x", "foo:\tbar"])
def test_yaml_forms_the_parser_does_not_model_are_refused(value: str) -> None:
    text = PARSER_WORKFLOW
    mutated = text.replace("          BASE_SHA: ${{ github.event.pull_request.base.sha || github.event.before }}",
                           f"          BASE_SHA: {value}")
    assert mutated != text
    with pytest.raises(tool.ToolingError, match="unsupported YAML value"):
        tool.parse_jobs(mutated)


def test_quoted_scalars_and_keys_are_read_as_yaml_reads_them() -> None:
    assert tool._plain('"x" # comment') == "x"
    assert tool._plain("'it''s'  # comment") == "it's"
    assert tool._plain("plain value\t# comment") == "plain value"
    # "-", "?" and ":" followed by a non-space begin a plain scalar, and flow indicators may follow its first character.
    for value in ("-x", "?x", ":x", "a,b", "a]", "x}", "foo:bar"):
        assert tool._plain(value) == value
    # GitHub rejects a repeated key; a key is a plain word followed by ': '.
    text = PARSER_WORKFLOW
    line = "        run: python3 ci/checks/check_agents_md_citations.py\n"
    for mutated, message in ((text.replace(line, line + "        run: exit 0\n"), "repeated"),
                             (text.replace(line, line.replace("run: ", "run:")), "unsupported workflow key"),
                             (text.replace(line, line.replace("run:", '"run":')), "unsupported workflow key")):
        assert mutated != text
        with pytest.raises(tool.ToolingError, match=message):
            tool.parse_jobs(mutated)


def test_implicitly_typed_scalars_are_refused_unless_github_writes_them_back_unchanged() -> None:
    # GitHub reads the workflow as YAML 1.2 and writes an env value it reads as a boolean or an integer back as
    # true, false or decimal; any other spelling, a null or a float would become another string.
    text = PARSER_WORKFLOW
    env_line = "      APP_ENV: dev\n"
    for value in ("1.0", "0x10", "010", "+1", "True", "~", "null", ".inf"):
        with pytest.raises(tool.ToolingError, match="unsupported shape"):
            tool.parse_jobs(text.replace(env_line, f"      APP_ENV: {value}\n"))
    for value in ("true", "false", "0", "12", "-3"):
        assert tool.parse_jobs(text.replace(env_line, f"      APP_ENV: {value}\n"))["test"].env["APP_ENV"] == value
    with pytest.raises(tool.ToolingError, match="unsupported workflow key"):
        tool.parse_jobs(text.replace(env_line, env_line + "      true: x\n"))
    assert isinstance(tool._plain("TRUE"), tool._Resolved) and not isinstance(tool._plain("'true'"), tool._Resolved)
    assert not isinstance(tool._plain("ubuntu-latest"), tool._Resolved)


def test_the_whole_workflow_is_one_mapping_without_repeated_keys() -> None:
    text = PARSER_WORKFLOW
    second_jobs = "\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - name: only\n        run: exit 1\n"
    for appended in ("\nname: other\n", second_jobs):
        with pytest.raises(tool.ToolingError, match="repeated"):
            tool.parse_jobs(text + appended)
    # The sweep's coverage reads the jobs through the same parse.
    with pytest.raises(tool.ToolingError, match="repeated"):
        tool.pytest_command_tokens(text + second_jobs)


def test_sequence_entries_share_one_indentation() -> None:
    text = PARSER_WORKFLOW
    entries = "    paths:\n      - '**'\n      - '!docs/crd/**'\n"
    for new in ("    paths:\n      - '**'\n        - '!docs/crd/**'\n",
                "    paths:\n        - '**'\n      - '!docs/crd/**'\n"):
        mutated = text.replace(entries, new, 1)
        assert mutated != text
        with pytest.raises(tool.ToolingError, match="indented differently from its sequence's first entry"):
            tool.parse_jobs(mutated)


def test_tabs_in_indentation_are_refused_and_elsewhere_read_as_yaml_reads_them() -> None:
    text = PARSER_WORKFLOW
    body = "          set -euo pipefail\n"
    for old, new in (("name: ci\n", "\tname: ci\n"), ("  contents: read\n", "\tcontents: read\n"),
                     ("      - main\n", "    \t- main\n"), (body, "        \tset -euo pipefail\n"),
                     ("permissions:\n", "permissions:\n \t\n")):
        mutated = text.replace(old, new, 1)
        assert mutated != text
        with pytest.raises(tool.ToolingError, match="a tab in the indentation of line"):
            tool.parse_jobs(mutated)
    with pytest.raises(tool.ToolingError, match="whitespace with a tab"):
        tool.parse_jobs(text.replace(body, body + "\t\n", 1))
    # A tab after a block's indentation is content, and one after a key's colon separates its value.
    assert tool.parse_jobs(text.replace(body, "          \tset -euo pipefail\n", 1))["test"].steps[1]["run"].startswith(
        "\tset -euo pipefail\n")
    tab_separated = text.replace("  contents: read\n", "  contents:\tread\n")
    assert len(tool.parse_jobs(tab_separated)["test"].steps) == len(tool.parse_jobs(text)["test"].steps) == 3


def test_block_scalars_are_read_as_yaml_reads_them_or_refused() -> None:
    text = PARSER_WORKFLOW
    line = "        run: python3 ci/checks/check_agents_md_citations.py\n"

    def run_of(block: str) -> object:
        mutated = text.replace(line, block)
        assert mutated != text
        return tool.parse_jobs(mutated)["test"].steps[2]["run"]

    assert run_of("        run: >-\n          echo a\n          echo b\n\n          echo c\n") == "echo a echo b\necho c"
    assert run_of("        run: |\n          echo a\n            echo b\n") == "echo a\n  echo b\n"
    # A folded block keeps the line breaks around a more-indented line, which is not modelled.
    with pytest.raises(tool.ToolingError, match="more indented"):
        run_of("        run: >\n          echo replay_pass\n            exit 1\n")
    with pytest.raises(tool.ToolingError, match="less indented"):
        run_of("        run: |\n            echo a\n          echo b\n")


def test_an_unexpected_report_exception_still_reaches_the_read_only_check(
        tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    repo = _synthetic(tmp_path / "raises", {"data.txt": "tracked\n"})

    def raises(context: object, report: object) -> None:
        raise TypeError("boom")

    monkeypatch.setitem(tool.RUNNERS, "build-notes", raises)
    assert tool.main(["build-notes", "--repo-root", str(repo)]) == tool.EXIT_REPORT_FAILED
    out = capsys.readouterr().out
    assert "build-notes: TOOLING_FAILURE TypeError: boom" in out
    assert "PREPUSH_CHECK_RESULT: FAIL build-notes=FAIL; repository unchanged" in out


_REJECTED = "the runner rejects GITHUB_OUTPUT record"
_UNMODELLED = "is a form the replay does not model"


@pytest.mark.parametrize(
    "data, outputs, problem",
    [
        (b"", {}, None),
        (b"a=1\n\nb=x=y\nk=v<<x\nlast=", {"a": "1", "b": "x=y", "k": "v<<x", "last": ""}, None),
        (b"a=1\ninvalid\nb=2\n", {"a": "1"}, ("BEHAVIOR", _REJECTED)),
        (b"body<<EOF\nx\nEOF\n", {}, ("TOOLING", _UNMODELLED)),
        (b"a<<b=c\n", {}, ("TOOLING", _UNMODELLED)),
        (b"a=1\n=v\n", {"a": "1"}, ("TOOLING", _UNMODELLED)),
        (b"a=1\r\n", {}, ("TOOLING", _UNMODELLED)),
        (b"\r\n", {}, ("TOOLING", _UNMODELLED)),
        (b"a=\xff\n", {}, ("TOOLING", "is not UTF-8")),
    ],
    ids=["empty", "name-value", "no-separator", "heredoc", "heredoc-first", "empty-name", "carriage-return",
         "carriage-return-alone", "not-utf-8"],
)
def test_github_output_is_read_as_the_linux_runner_reads_it(
        data: bytes, outputs: dict[str, str], problem: tuple[str, str] | None) -> None:
    got, got_problem = tool.parse_github_output(data)
    assert got == outputs
    assert (got_problem is None) == (problem is None)
    if problem:
        assert got_problem[0] == problem[0] and problem[1] in got_problem[1]


def test_lanes_refuses_classifier_output_the_runner_would_reject(tmp_path: Path) -> None:
    output, targets = tmp_path / "output.txt", tmp_path / "targets.txt"
    output.write_text("product=true\ninvalid\n", encoding="utf-8")
    targets.write_text("", encoding="utf-8")
    report = tool.Report("lanes")
    assert tool._print_outputs(report, output, targets) == {"product": "true"}
    assert report.status == "FAIL"
    assert f"lanes: FAILURE classifier output: {_REJECTED} 'invalid', which is neither NAME=VALUE nor " \
           "NAME<<DELIMITER" in report.lines


def test_coverage_matches_the_binding_definition_and_the_guard_on_the_repository() -> None:
    coverage = tool.compute_coverage(ROOT)
    text = WORKFLOW.read_text(encoding="utf-8")
    guard_tokens = set(re.findall(r"tests/[A-Za-z0-9_./-]+", text))
    assert set(coverage["pytest_command_tokens"]) == guard_tokens
    assert set(coverage["anywhere_tokens"]) == guard_tokens
    assert coverage["full_validation_targets"] == len(classifier._full_validation_test_targets())
    listed = _git(ROOT, "ls-files", "--", "tests").splitlines()
    tracked = [p for p in listed if PurePosixPath(p).name.startswith("test_") and p.endswith(".py")]
    assert coverage["tracked"] == len(tracked)
    roots = guard_tokens | set(classifier._full_validation_test_targets()) | set(classifier._CLOSE_STAGE_TESTS)
    guard_uncovered = [p for p in tracked if not any(p == r or p.startswith(r.rstrip("/") + "/") for r in roots)]
    assert coverage["uncovered"] == guard_uncovered == []
    assert "tests/tools/test_prepush_check.py" in classifier._full_validation_test_targets()


SYNTHETIC_CLASSIFIER = '''
def _full_validation_test_targets():
    return ("tests/full/test_full.py",)
'''
SWEEP_WORKFLOW = """\
name: ci
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Lane
        run: |
          echo tests/extra
          python -m pytest -q tests/lane
"""


def test_sweep_flags_runs_and_classifies_a_synthetic_uncovered_set(tmp_path: Path) -> None:
    repo = _synthetic(tmp_path / "synthetic", {
        ".github/workflows/ci.yml": SWEEP_WORKFLOW,
        "ci/checks/classify_ci_changes.py": SYNTHETIC_CLASSIFIER,
        "data.txt": "tracked\n",
        "tests/lane/test_lane.py": "def test_lane():\n    pass\n",
        "tests/full/test_full.py": "def test_full():\n    pass\n",
        "tests/extra/test_pass.py": "def test_pass():\n    pass\n",
        "tests/extra/test_fail.py": "def test_fail():\n    assert False\n",
        "tests/extra/test_import.py": "import module_that_does_not_exist\n",
        "tests/extra/test_writes.py": (
            "from pathlib import Path\n\n"
            "def test_writes():\n"
            "    Path(__file__).resolve().parents[2].joinpath('data.txt').write_text('rewritten\\n')\n"
        ),
    })
    # The guard's wider token set accepts tests/extra; the binding definition does not.
    text = (repo / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert "tests/extra" in tool.anywhere_tokens(text) and "tests/extra" not in tool.pytest_command_tokens(text)

    result = _run(repo, "sweep")
    assert result.returncode == tool.EXIT_REPORT_FAILED, result.stdout + result.stderr
    lines = _report_lines(result.stdout, "sweep")
    expected = ["tests/extra/test_fail.py", "tests/extra/test_import.py",
                "tests/extra/test_pass.py", "tests/extra/test_writes.py"]
    assert [line.split(" ", 1)[1] for line in lines if line.startswith("uncovered ")] == expected
    outcome = {line.rsplit(" ", 1)[1]: line for line in lines if line.startswith("file ")}
    assert outcome["tests/extra/test_pass.py"].startswith("file PASS")
    assert outcome["tests/extra/test_writes.py"].startswith("file PASS")
    assert outcome["tests/extra/test_fail.py"].startswith("file BEHAVIOR")
    assert outcome["tests/extra/test_import.py"].startswith("file TOOLING")
    assert any(line.startswith("copy after run: CHANGED") for line in lines)
    assert "status=FAIL" in lines[-1]

    listed = _run(repo, "sweep", "--no-run")
    assert listed.returncode == tool.EXIT_REPORT_FAILED
    assert "sweep: run: not executed (--no-run)" in listed.stdout

    (repo / "tests/extra").rename(repo / "tests/lane/extra")
    _git(repo, "add", "-A")
    _git(repo, "commit", "--quiet", "-m", "cover")
    covered = _run(repo, "sweep")
    assert covered.returncode == tool.EXIT_OK, covered.stdout + covered.stderr
    assert "uncovered=0" in covered.stdout

    # A sweep environment without ruby is a tooling failure even when no file is uncovered.
    bin_dir = tmp_path / "bin-without-ruby"
    bin_dir.mkdir()
    for name in ("git", "bash", "curl", "sh"):
        found = shutil.which(name)
        if found:
            (bin_dir / name).symlink_to(found)
    no_ruby = _run(repo, "sweep", extra_env={"PATH": str(bin_dir)})
    assert no_ruby.returncode == tool.EXIT_REPORT_FAILED, no_ruby.stdout + no_ruby.stderr
    assert "sweep: TOOLING_FAILURE missing on PATH: ruby" in no_ruby.stdout and "uncovered=0" in no_ruby.stdout


def test_repository_state_covers_ignored_files(tmp_path: Path) -> None:
    repo = _synthetic(tmp_path / "ignored", {".gitignore": "*.log\nbuild/\n", "data.txt": "tracked\n"})
    (repo / "kept.log").write_text("one\n", encoding="utf-8")
    (repo / "build").mkdir()
    (repo / "build/out.bin").write_bytes(b"\x00")
    before = tool.repository_state(repo)
    assert not before.status and [entry[0] for entry in before.ignored] == ["build/out.bin", "kept.log"]
    assert tool.repository_state(repo) == before
    (repo / "kept.log").write_text("two\n", encoding="utf-8")
    rewritten = tool.repository_state(repo)
    assert rewritten != before and not rewritten.status
    (repo / "new.log").write_text("", encoding="utf-8")
    created = tool.repository_state(repo)
    assert created != rewritten and not created.status
    (repo / "build/out.bin").unlink()
    deleted = tool.repository_state(repo)
    assert deleted != created
    # Empty directories, ignored or not, appear in neither listing; their parents' identities change.
    (repo / "build/empty").mkdir()
    ignored_directory = tool.repository_state(repo)
    assert ignored_directory != deleted and not ignored_directory.status
    (repo / "build/empty").rmdir()
    assert tool.repository_state(repo) != ignored_directory
    (repo / "untracked-empty").mkdir()
    untracked_directory = tool.repository_state(repo)
    assert not untracked_directory.status and ".git" not in {entry[0] for entry in untracked_directory.directories}
    assert "untracked-empty" in {entry[0] for entry in untracked_directory.directories}
    # Nor does an empty directory in the git metadata; its name is part of the metadata digest.
    (repo / ".git" / "refs" / "empty").mkdir()
    metadata_directory = tool.repository_state(repo)
    assert metadata_directory.metadata != untracked_directory.metadata and not metadata_directory.status
    (repo / ".git" / "refs" / "empty").rmdir()
    assert tool.repository_state(repo).metadata == untracked_directory.metadata
    # git status compares content, so a tracked file rewritten with its own bytes is seen by its identity.
    settled = tool.repository_state(repo)
    (repo / "data.txt").write_text("tracked\n", encoding="utf-8")
    rewritten_tracked = tool.repository_state(repo)
    assert rewritten_tracked.tracked != settled.tracked and rewritten_tracked.status == settled.status
    # An object is not read, so a same-length overwrite of an unreachable one is seen by its identity too.
    blob = subprocess.run(["git", "-C", str(repo), "hash-object", "-w", "--stdin"], input=b"unreachable\n",
                          check=True, capture_output=True).stdout.decode().strip()
    loose = repo / ".git" / "objects" / blob[:2] / blob[2:]
    settled = tool.repository_state(repo)
    loose.chmod(0o644)
    loose.write_bytes(bytes(len(loose.read_bytes())))
    assert tool.repository_state(repo).metadata != settled.metadata
    # Other git metadata is read, and its identity is recorded too: a rewrite with the same bytes is seen.
    settled = tool.repository_state(repo)
    config = repo / ".git" / "config"
    config.write_bytes(config.read_bytes())
    assert tool.repository_state(repo).metadata != settled.metadata


# A fixed past instant: a file set to it and then written or freshened has a changed mtime on any clock.
PAST_NS = 1_600_000_000_000_000_000


def _set_past(paths: list[Path]) -> None:
    assert paths
    for path in paths:
        os.utime(path, ns=(PAST_NS, PAST_NS))


def _write_existing_blob(repo: Path) -> None:
    subprocess.run(["git", "-C", str(repo), "hash-object", "-w", "--stdin"], input=b"alpha\n", check=True,
                   capture_output=True)


@pytest.mark.parametrize("packed", [True, False], ids=["packed", "loose"])
def test_a_copy_owns_its_objects_so_a_write_in_it_cannot_freshen_the_source(tmp_path: Path, packed: bool) -> None:
    """QA110-F01: writing again an object that a reachable store already holds makes git freshen (re-time) the file
    holding it, so a copy that borrowed the source's objects would change the source's pack or loose object."""
    source = _synthetic(tmp_path / "source", {"a.txt": "alpha\n", "d/b.txt": "beta\n"})
    if packed:
        _git(source, "repack", "-a", "-d", "-q")
        _git(source, "prune-packed", "-q")
    head = _git(source, "rev-parse", "HEAD")
    objects = source / ".git" / "objects"
    blob = _git(source, "hash-object", "a.txt")
    (held,) = sorted(objects.glob("pack/*.pack")) if packed else [objects / blob[:2] / blob[2:]]
    _set_past([path for path in objects.rglob("*") if path.is_file()])
    before = tool.repository_state(source)
    copy = tool.make_copy(source, head, tmp_path / "copy")
    assert not (copy / ".git" / "objects" / "info" / "alternates").exists()
    assert tool.repository_state(source) == before
    _write_existing_blob(copy)
    assert tool.repository_state(source) == before
    assert tool.state_changes(before, tool.repository_state(source)) == []
    # Negative control: a borrowing copy shows the mechanism this test guards against, in git metadata only.
    shared = tmp_path / "shared"
    subprocess.run(["git", "clone", "--quiet", "--shared", "--no-checkout", "--", str(source), str(shared)],
                   check=True, capture_output=True)
    _git(shared, "-c", "advice.detachedHead=false", "checkout", "--quiet", "--detach", head)
    assert tool.repository_state(source) == before
    _write_existing_blob(shared)
    freshened = tool.repository_state(source)
    assert freshened.metadata != before.metadata
    assert (freshened.head, freshened.status, freshened.tracked, freshened.ignored, freshened.directories) == \
        (before.head, before.status, before.tracked, before.ignored, before.directories)
    git_dir = tool.git_text(source, "rev-parse", "--absolute-git-dir")
    assert tool.state_changes(before, freshened) == [
        f"git metadata {git_dir}/{held.relative_to(source / '.git').as_posix()} (mtime, ctime)"]


def test_a_copy_of_a_source_that_borrows_objects_borrows_none_itself(tmp_path: Path) -> None:
    base = _synthetic(tmp_path / "base", {"a.txt": "alpha\n"})
    _git(base, "repack", "-a", "-d", "-q")
    source = tmp_path / "borrowing"
    subprocess.run(["git", "clone", "--quiet", "--shared", "--", str(base), str(source)], check=True,
                   capture_output=True)
    assert (source / ".git" / "objects" / "info" / "alternates").exists()
    head = _git(source, "rev-parse", "HEAD")
    _set_past([path for path in (base / ".git" / "objects").rglob("*") if path.is_file()])
    before_base, before_source = tool.repository_state(base), tool.repository_state(source)
    copy = tool.make_copy(source, head, tmp_path / "copy")
    assert not (copy / ".git" / "objects" / "info" / "alternates").exists()
    _write_existing_blob(copy)
    assert tool.repository_state(source) == before_source
    assert tool.repository_state(base) == before_base


def test_a_read_only_violation_names_the_changed_entries(tmp_path: Path) -> None:
    repo = _synthetic(tmp_path / "named", {"README.txt": "fixture\n"})
    config = repo / ".git" / "config"
    _set_past([repo / "README.txt", config])
    before = tool.repository_state(repo)
    config.write_bytes(config.read_bytes())
    (repo / "README.txt").write_text("fixture\n", encoding="utf-8")
    after = tool.repository_state(repo)
    changes = tool.state_changes(before, after)
    git_dir = tool.git_text(repo, "rev-parse", "--absolute-git-dir")
    assert [line.rsplit(" (", 1)[0] for line in changes] == ["tracked README.txt", f"git metadata {git_dir}/config"]
    # Rewritten with the same bytes: only the times moved, and no content or digest is named.
    for line in changes:
        moved = set(line.rsplit(" (", 1)[1].removesuffix(")").split(", "))
        assert "mtime" in moved and moved <= {"mtime", "ctime"}, line
    assert all("fixture" not in line and not re.search(r"[0-9a-f]{40}", line) for line in changes)
    assert tool.state_changes(before, after, limit=1) == [changes[0], "and 1 more"]


# --------------------------------------------------------------------------
# every report on the repository: read-only, and the expected answers
# --------------------------------------------------------------------------

def test_reports_on_a_clone_of_the_repository_are_read_only(repo_clone: Path) -> None:
    from engine.config.registry_loader import ADMITTED_RELEASE_ROSTER, ADMITTED_RELEASE_VERSION

    notes = _run(repo_clone, "build-notes")
    assert notes.returncode == tool.EXIT_OK, notes.stdout + notes.stderr
    (line,) = [line for line in _report_lines(notes.stdout, "build-notes") if line.startswith("path=")]
    path, _size, digest = (part.split("=", 1)[1] for part in line.split())
    # HDE-CRD-0003 S17: the vendored HDE Build Notes copy, in agreement with the resolver.
    from tools.pf_tool_inputs import resolver

    entry = resolver.pf_entry("PF10", repo_clone)
    assert path == tool.BUILD_NOTES_COPY == resolver.copy_rel("PF10")
    assert digest == entry.sha256 == hashlib.sha256(resolver.pf_document("PF10", root=repo_clone).read_bytes()).hexdigest()
    (source,) = [line for line in _report_lines(notes.stdout, "build-notes") if line.startswith("source=")]
    assert source == (
        f"source=amthorn78/glow-docs:docs/hde/pfcanon/{entry.file_name} "
        f"commit={resolver.source_commit(repo_clone)} blob={entry.source_blob}"
    )

    paths = [*ADMITTED_RELEASE_ROSTER, "tools/ci/prepush_check.py"]
    membership = _run(repo_clone, "membership", *(arg for p in paths for arg in ("--path", p)))
    assert membership.returncode == tool.EXIT_OK, membership.stdout + membership.stderr
    lines = _report_lines(membership.stdout, "membership")
    assert {line.split(" ", 1)[1] for line in lines if line.startswith("member ")} == set(ADMITTED_RELEASE_ROSTER)
    assert "not-member tools/ci/prepush_check.py" in lines
    assert f"version={ADMITTED_RELEASE_VERSION} roster={len(ADMITTED_RELEASE_ROSTER)}" in lines[0]
    assert tool.admitted_release(repo_clone) == (ADMITTED_RELEASE_VERSION, frozenset(ADMITTED_RELEASE_ROSTER))

    sweep = _run(repo_clone, "sweep")
    assert sweep.returncode == tool.EXIT_OK, sweep.stdout + sweep.stderr
    assert "uncovered=0" in sweep.stdout

    full = _run(repo_clone, "lanes", "--full")
    assert full.returncode == tool.EXIT_OK, full.stdout + full.stderr
    assert "reason=identical_refs_full_validation" in full.stdout
    assert f"lanes: changed_test_targets={len(classifier._full_validation_test_targets())}" in full.stdout

    usage = _run(repo_clone, "membership")
    assert usage.returncode == tool.EXIT_REPORT_FAILED
    assert "membership needs at least one --path" in usage.stdout


# --------------------------------------------------------------------------
# lanes: equal to the classifier (both modes, refusals included)
# --------------------------------------------------------------------------

def _classifier_cli(repo: Path, base: str, head: str, event: str, tmp: Path) -> tuple[int, str, str, list[str], list[str]]:
    output, targets = tmp / f"gh-{event}-{head[:8]}", tmp / f"t-{event}-{head[:8]}"
    output.unlink(missing_ok=True)
    result = subprocess.run(
        [sys.executable, "-B", str(repo / tool.CLASSIFIER_PATH), "--base", base, "--head", head,
         "--event-name", event, "--repo-root", str(repo), "--github-output", str(output),
         "--changed-tests-output", str(targets)],
        cwd=repo, capture_output=True, text=True, check=False)
    read = (lambda p: p.read_text(encoding="utf-8").splitlines() if p.exists() else [])
    return result.returncode, result.stdout.strip(), result.stderr.strip(), read(output), read(targets)


def test_lanes_equals_the_classifier_for_refs_and_for_given_paths(tmp_path: Path) -> None:
    repo = _clone(tmp_path / "clone")
    (repo / "tests/__pycache__/sentinel.cpython-312.pyc").unlink()
    base = _git(repo, "rev-parse", "HEAD")
    with (repo / "tools/ci/prepush_check.py").open("a", encoding="utf-8") as stream:
        stream.write("# lanes equality fixture\n")
    _git(repo, "commit", "--quiet", "-am", "tool change")
    tool_change = _git(repo, "rev-parse", "HEAD")
    (repo / "ci/checks/unregistered_check.py").write_text("pass\n", encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "--quiet", "-m", "unregistered")
    refused = _git(repo, "rev-parse", "HEAD")
    # Refs keep both commits reachable for clones of this clone (a shallow
    # source makes ``git clone --shared`` fall back to copying ref history).
    _git(repo, "branch", "fixture-tool-change", tool_change)
    _git(repo, "branch", "fixture-refused", refused)
    _git(repo, "-c", "advice.detachedHead=false", "checkout", "--quiet", "--detach", tool_change)

    for head, event in ((tool_change, "pull_request"), (tool_change, "push"), (refused, "pull_request")):
        expected = _classifier_cli(repo if head == tool_change else _clone_at(repo, head, tmp_path),
                                   base, head, event, tmp_path)
        result = _run(repo, "lanes", "--base", base, "--head", head, "--event", event)
        lines = _report_lines(result.stdout, "lanes")
        if expected[0] == 0:
            assert result.returncode == tool.EXIT_OK, result.stdout + result.stderr
            assert expected[1] in lines
            assert [line[len("output "):] for line in lines if line.startswith("output ")] == expected[3]
            assert [line[len("target "):] for line in lines if line.startswith("target ")] == expected[4]
        else:
            assert result.returncode == tool.EXIT_REPORT_FAILED
            assert f"FAILURE classifier exit {expected[0]}: {expected[2]}" in lines
            assert "CI_CHANGE_CLASSIFIER_ERROR:" in expected[2]
    assert "tests/tools/test_prepush_check.py" in _classifier_cli(repo, base, tool_change, "push", tmp_path)[4]

    for paths in (["tools/ci/prepush_check.py"], ["VERIFY.sh"], ["docs/ephemeral/x.md"],
                  ["ci/checks/classify_ci_changes.py"], ["ci/checks/unregistered_check.py"],
                  ["tools/ci/another_tool.py"]):
        result = _run(repo, "lanes", *(arg for p in paths for arg in ("--path", p)))
        lines = _report_lines(result.stdout, "lanes")
        module = tool.load_classifier(repo)
        try:
            outcome = module.classify_paths(paths, governed_paths=module._load_governed_primary_paths(repo))
            targets = outcome.test_targets or module.changed_test_targets(repo, paths)
        except ValueError as exc:
            assert result.returncode == tool.EXIT_REPORT_FAILED
            assert f"FAILURE CI_CHANGE_CLASSIFIER_ERROR:{exc}" in lines
            continue
        expected_output = tmp_path / "expected-output"
        expected_output.unlink(missing_ok=True)
        module.write_github_output(expected_output, module.Classification(
            flags=outcome.flags, reason=outcome.reason, path_count=outcome.path_count, test_targets=targets))
        assert result.returncode == tool.EXIT_OK, result.stdout + result.stderr
        assert [line[len("output "):] for line in lines if line.startswith("output ")] == \
            expected_output.read_text(encoding="utf-8").splitlines()
        assert [line[len("target "):] for line in lines if line.startswith("target ")] == list(targets)


def test_lanes_and_membership_run_the_classifier_only_in_a_throwaway_copy(tmp_path: Path) -> None:
    repo = _clone(tmp_path / "clone")
    # A classifier that, whenever it is loaded, writes beside itself and says where it ran.
    classifier_file = repo / tool.CLASSIFIER_PATH
    imports = "from pathlib import Path, PurePosixPath\n"
    source = classifier_file.read_text(encoding="utf-8")
    assert source.count(imports) == 1
    classifier_file.write_text(source.replace(imports, imports + (
        "Path(__file__).with_name('classifier-ran.txt').write_text(os.getcwd() + '\\n')\n"
        "print('classifier ran in ' + os.getcwd())\n")), encoding="utf-8")
    _git(repo, "commit", "--quiet", "-am", "classifier with a write on load")
    # _run also asserts that the checkout, ignored files and .git included, is unchanged by each run.
    for args in (("lanes", "--full"), ("lanes", "--path", "tools/ci/prepush_check.py"),
                 ("membership", "--path", "tools/ci/prepush_check.py")):
        result = _run(repo, *args)
        assert result.returncode == tool.EXIT_OK, result.stdout + result.stderr
        assert not (repo / "ci/checks/classifier-ran.txt").exists()
    # The script form prints into the report: it ran in the throwaway copy.
    full = _run(repo, "lanes", "--full")
    (where,) = [line.split("classifier ran in ", 1)[1] for line in _report_lines(full.stdout, "lanes")
                if line.startswith("classifier ran in ")]
    assert Path(where).name == "lanes-copy" and not Path(where).resolve().is_relative_to(repo.resolve())


def _clone_at(source: Path, commit: str, tmp_path: Path) -> Path:
    destination = tmp_path / f"at-{commit[:12]}"
    if not destination.exists():
        subprocess.run(["git", "clone", "--quiet", "--shared", "--no-checkout", str(source), str(destination)],
                       check=True, capture_output=True)
        _git(destination, "-c", "advice.detachedHead=false", "checkout", "--quiet", "--detach", commit)
    return destination


# --------------------------------------------------------------------------
# build-notes uniqueness, dirty-tree refusal, child environment, no hook
# --------------------------------------------------------------------------

def _manifest_document(name: str, body: bytes, *, vendored: bool) -> dict[str, object]:
    pf_id = name.split("-", 1)[0]
    return {
        "file_name": name,
        "pf_id": pf_id,
        "sha256": hashlib.sha256(body).hexdigest(),
        "size_bytes": len(body),
        "source_blob": "1" * 40,
        "title": "fixture",
        "vendored": vendored,
    }


@pytest.mark.parametrize("names, ok", [((), False), (("v1.0",), True), (("v1.0", "v1.1"), False)])
def test_build_notes_requires_exactly_one_file(tmp_path: Path, names: tuple[str, ...], ok: bool) -> None:
    # The PF tool-input manifest at HEAD must name exactly one vendored PF10 entry (HDE-CRD-0003 S17).
    documents = [_manifest_document("PF01-Other.md", b"x\n", vendored=False)] + [
        _manifest_document(f"PF10-HDE-Build-Notes-{n}.md", f"notes {n}\n".encode(), vendored=True) for n in names
    ]
    manifest = {
        "documents": documents,
        "schema_version": "pf_tool_inputs.v1",
        "source_commit": "2" * 40,
        "source_path": "docs/hde/pfcanon/",
        "source_repository": "amthorn78/glow-docs",
    }
    files = {"README.txt": "fixture\n", tool.PF_TOOL_INPUTS_MANIFEST: json.dumps(manifest, sort_keys=True) + "\n"}
    if names:
        files[tool.BUILD_NOTES_COPY] = f"notes {names[0]}\n"
    repo = _synthetic(tmp_path / "notes", files)
    result = _run(repo, "build-notes")
    if ok:
        assert result.returncode == tool.EXIT_OK, result.stdout + result.stderr
        digest = hashlib.sha256(b"notes v1.0\n").hexdigest()
        assert f"build-notes: path={tool.BUILD_NOTES_COPY} bytes=11 sha256={digest}" in result.stdout
        assert (
            "build-notes: source=amthorn78/glow-docs:docs/hde/pfcanon/PF10-HDE-Build-Notes-v1.0.md "
            f"commit={'2' * 40} blob={'1' * 40}"
        ) in result.stdout
    else:
        assert result.returncode == tool.EXIT_REPORT_FAILED
        assert f"found {len(names)}" in result.stdout


def test_build_notes_refuses_a_copy_that_does_not_match_the_manifest(tmp_path: Path) -> None:
    manifest = {
        "documents": [_manifest_document("PF10-HDE-Build-Notes-v1.0.md", b"notes v1.0\n", vendored=True)],
        "schema_version": "pf_tool_inputs.v1",
        "source_commit": "2" * 40,
        "source_path": "docs/hde/pfcanon/",
        "source_repository": "amthorn78/glow-docs",
    }
    repo = _synthetic(
        tmp_path / "mismatch",
        {tool.PF_TOOL_INPUTS_MANIFEST: json.dumps(manifest) + "\n", tool.BUILD_NOTES_COPY: "notes v1.1\n"},
    )
    result = _run(repo, "build-notes")
    assert result.returncode == tool.EXIT_REPORT_FAILED
    assert "vendored PF10 bytes do not match the manifest" in result.stdout


@pytest.mark.parametrize("dirty", ["modified", "staged", "untracked"])
def test_dirty_tree_is_refused_before_any_report(tmp_path: Path, dirty: str) -> None:
    repo = _synthetic(tmp_path / "dirty", {"tracked.txt": "one\n"})
    if dirty == "untracked":
        (repo / "new.txt").write_text("new\n", encoding="utf-8")
    else:
        (repo / "tracked.txt").write_text("two\n", encoding="utf-8")
        if dirty == "staged":
            _git(repo, "add", "tracked.txt")
    result = _run(repo, "build-notes")
    assert result.returncode == tool.EXIT_REFUSED
    assert "PREPUSH_CHECK_REFUSED: the working tree is not clean" in result.stderr
    assert "build-notes:" not in result.stdout


def test_a_report_without_its_inputs_is_a_tooling_failure(tmp_path: Path) -> None:
    repo = _synthetic(tmp_path / "bare", {"README.txt": "fixture\n"})
    result = _run(repo, "membership", "lanes", "--path", "README.txt")
    assert result.returncode == tool.EXIT_REPORT_FAILED, result.stdout + result.stderr
    for report in ("lanes", "membership"):
        (line,) = [line for line in result.stdout.splitlines() if line.startswith(f"{report}: TOOLING_FAILURE")]
        assert "failed in the throwaway copy" in line and "FileNotFoundError" in line
    assert "PREPUSH_CHECK_RESULT: FAIL lanes=FAIL membership=FAIL; repository unchanged" in result.stdout


def test_child_environment_is_closed_rails_without_keys(tmp_path: Path) -> None:
    base = {**DUMMY_KEYS, "PATH": "/usr/bin", "SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "prod",
            "GIT_OPTIONAL_LOCKS": "0", "HOME": "/home/x", "USER": "x", "AWS_SECRET_ACCESS_KEY": "aws-dummy",
            "HTTPS_PROXY": "http://proxy.invalid", "GITHUB_SHA": "caller", "GIT_DIR": "/elsewhere"}
    env = tool.child_environment(base, tmp_path)
    assert not set(DUMMY_KEYS) & set(env)
    assert {k: env[k] for k in tool.CLOSED_RAILS} == tool.CLOSED_RAILS
    assert env["PATH"].split(os.pathsep)[0] == str(Path(sys.executable).parent)
    assert env["TMPDIR"].startswith(str(tmp_path)) and env["XDG_STATE_HOME"].startswith(str(tmp_path))
    # Only the allowlisted caller variables are inherited; everything else is the tool's own.
    assert set(env) == {"HOME", "PATH", "USER", "TMPDIR", "XDG_STATE_HOME", *tool.CLOSED_RAILS}
    assert env["HOME"] == "/home/x" and env["USER"] == "x"
    assert not set(CHILD_KEYS) & set(tool.CHILD_INHERITED_KEYS)


def test_tool_installs_no_hook_fetches_nothing_and_opens_no_network() -> None:
    tree = ast.parse(TOOL.read_text(encoding="utf-8"))
    imported = {alias.name.split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.Import)
                for alias in node.names}
    imported |= {node.module.split(".")[0] for node in ast.walk(tree)
                 if isinstance(node, ast.ImportFrom) and node.module}
    assert not imported & {"socket", "ssl", "urllib", "http", "requests", "ftplib", "smtplib"}
    strings = {node.value for node in ast.walk(tree) if isinstance(node, ast.Constant) and isinstance(node.value, str)}
    assert not strings & {"fetch", "remote", "hooks", "core.hooksPath", "worktree"}


# --------------------------------------------------------------------------
# replay is not a report (HDE-CRD-0003 S11, P-2)
# --------------------------------------------------------------------------

def test_replay_is_not_a_report(tmp_path: Path) -> None:
    assert tool.REPORTS == ("lanes", "membership", "build-notes", "sweep")
    assert set(tool.RUNNERS) == set(tool.REPORTS)
    repo = _synthetic(tmp_path / "usage", {"data.txt": "tracked\n"})
    refused = _run(repo, "replay")
    assert refused.returncode == tool.EXIT_USAGE == 2, refused.stdout + refused.stderr
    assert "invalid choice: 'replay'" in refused.stderr and "PREPUSH_CHECK:" not in refused.stdout
    shown = subprocess.run([sys.executable, str(TOOL), "--help"], capture_output=True, text=True, check=False)
    assert shown.returncode == 0 and "replay" not in shown.stdout.lower()


def test_no_pre_push_file_pins_the_workflow_bytes() -> None:
    # A change to ci.yml needs no change to the tool or to this test (S11 measure).
    digest = hashlib.sha256(WORKFLOW.read_bytes()).hexdigest()
    assert digest not in TOOL.read_text(encoding="utf-8")
    assert digest not in Path(__file__).read_text(encoding="utf-8")
    assert "REPLAY_" not in TOOL.read_text(encoding="utf-8")
