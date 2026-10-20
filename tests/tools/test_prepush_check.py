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
IDENTITY = ("-c", "user.name=prepush-test", "-c", "user.email=prepush-test@invalid", "-c", "commit.gpgsign=false")
# The keys the tool must remove from every child, stated independently of the
# tool's own list (instruction ID-9, plus the ENGINE_ENV alias).
CHILD_KEYS = ("DATABASE_URL", "GEO_API_KEY", "HD_API_KEY", "HDAPI_KEY", "HDAPI_BASE_URL", "HD_API_BASE_URL",
              "HD_GEOCODE_KEY", "HDE_VENDOR_OVERRIDE_AUDIT_PATH", "GH_TOKEN", "GITHUB_TOKEN", "ENGINE_ENV")
DUMMY_KEYS = {key: "dummy-not-a-secret" for key in CHILD_KEYS}
EXCLUDED = {
    "Check out exact candidate head",
    "Set up Python 3.12",
    "Install applicable validation dependencies",
}


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
    subprocess.run(["git", "clone", "--quiet", "--shared", "--no-checkout", str(ROOT), str(destination)],
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
# replay inventory (contract G-3) and expression handling
# --------------------------------------------------------------------------

def test_replay_inventory_pins_every_step_of_the_ci_test_job() -> None:
    # The replay models exactly this workflow: a PR that changes ci.yml updates the pin and the model with it.
    assert hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() == tool.REPLAY_WORKFLOW_SHA256
    text = WORKFLOW.read_text(encoding="utf-8")
    job, steps = tool.replay_steps(text)
    names = [str(step["name"]) for step in steps]
    inventory = [name for name, _kind, _reason in tool.REPLAY_INVENTORY]
    assert names == inventory
    excluded = {name for name, kind, _reason in tool.REPLAY_INVENTORY if kind == tool.REPLAY_EXCLUDED}
    executed = {name for name, kind, _reason in tool.REPLAY_INVENTORY if kind == tool.REPLAY_EXECUTED}
    assert excluded == EXCLUDED
    assert excluded | executed == set(names) and not excluded & executed
    assert all(reason for _name, kind, reason in tool.REPLAY_INVENTORY if kind == tool.REPLAY_EXCLUDED)
    assert {str(step.get("uses", "")).split("@")[0] for step in steps if "uses" in step} == {
        "actions/checkout", "actions/setup-python"}
    assert all("run" in step for step in steps if step["name"] in executed)
    assert job.env == tool.CLOSED_RAILS
    assert tool._python_version(steps) == "3.12"


@pytest.mark.parametrize(
    "mutate",
    [
        lambda text: text.replace("name: Run CLI and compatibility lane", "name: Run CLI lane"),
        lambda text: text.replace(
            "      - name: Verify truthful applicability",
            "      - name: A new step\n        run: echo new\n\n      - name: Verify truthful applicability"),
        lambda text: text.replace("        id: env_pins\n", "        id: env_pins\n        continue-on-error: true\n"),
        lambda text: text.replace("ref: ${{ github.event.pull_request.head.sha || github.sha }}", "ref: main"),
        lambda text: text.replace("          fetch-depth: 0\n", "          fetch-depth: 0\n          submodules: true\n"),
        lambda text: text.replace("fetch-depth: 0", "fetch-depth: 1"),
        lambda text: text.replace("          python-version: '3.12'\n", "          python-version: '3.12'\n          architecture: x86\n"),
        lambda text: text.replace("runs-on: ubuntu-latest", "runs-on: macos-latest"),
        lambda text: text.replace("\njobs:\n", "\nenv:\n  EXTRA: one\n\njobs:\n"),
        lambda text: text.replace("actions/checkout@v4", "actions/checkout@v5"),
        lambda text: text.replace("actions/setup-python@v5", "actions/setup-python@main"),
        lambda text: text.replace("run: python3 ci/checks/check_agents_md_citations.py",
                                  'run: python3 ci/checks/check_agents_md_citations.py --sha "$GITHUB_SHA"'),
        lambda text: text.replace("          BASE_SHA: ", "          RUNNER_OS: Linux\n          BASE_SHA: "),
        lambda text: text.replace("      APP_ENV: dev\n", "      APP_ENV: dev\n      GITHUB_WORKSPACE: /w\n", 1),
        lambda text: text.replace("persist-credentials: false", "persist-credentials: true"),
        lambda text: text.replace("        uses: actions/checkout@v4\n",
                                  "        if: ${{ false }}\n        uses: actions/checkout@v4\n"),
        lambda text: text.replace("        id: dependencies\n",
                                  "        id: dependencies\n        env:\n          PIP_INDEX_URL: x\n"),
        lambda text: text.replace("        run: python3 ci/checks/check_agents_md_citations.py",
                                  "        env: invalid\n        run: python3 ci/checks/check_agents_md_citations.py"),
        lambda text: text.replace("runs-on: ubuntu-latest", "runs-on: ubuntu-24.04-arm"),
        lambda text: text.replace("        run: python3 ci/checks/check_agents_md_citations.py\n", ""),
        lambda text: text.rstrip("\n") + ("\n\n  other:\n    runs-on: ubuntu-latest\n    steps:\n"
                                          "      - name: fail\n        run: exit 1\n"),
        lambda text: text.replace("          BASE_SHA: ${{ github.event.pull_request.base.sha || github.event.before }}\n",
                                  "          BASE_SHA:\n            nested: invalid\n"),
        lambda text: text.replace(
            "        id: python_setup\n        if: ${{ steps.classify.outputs.needs_python == 'true' }}\n",
            "        id: python_setup\n        if:\n          nested: invalid\n"),
        lambda text: text.replace(
            "        id: dependencies\n        if: ${{ steps.classify.outputs.needs_python == 'true' }}\n",
            "        id: dependencies\n        if: ${{ false }}\n"),
        lambda text: text.replace(
            "        id: python_setup\n        if: ${{ steps.classify.outputs.needs_python == 'true' }}\n",
            "        id: python_setup\n        if: ${{ false }}\n"),
        lambda text: text.replace(
            "        id: dependencies\n        if: ${{ steps.classify.outputs.needs_python == 'true' }}\n",
            "        id: dependencies\n"),
        lambda text: text.replace("run: python3 ci/checks/check_agents_md_citations.py", "run: true"),
        lambda text: text.replace("          HEAD_SHA: ${{ github.event.pull_request.head.sha || github.sha }}",
                                  "          HEAD_SHA: 1.0"),
        lambda text: text.replace("permissions:\n  contents: read\n", "permissions: invalid\n"),
        lambda text: text.replace("permissions:\n  contents: read\n", "permissions:\n  contents: write\n"),
        lambda text: text.replace("name: ci\n", "name: true\n", 1),
        lambda text: text.replace("\njobs:\n", "\nrun-name: ${{ github.sha }}\n\njobs:\n"),
        lambda text: text.replace("  cancel-in-progress: ${{ github.event_name == 'pull_request' }}\n", ""),
        lambda text: text.replace("      - '!docs/qa/**'\n", "", 1),
        lambda text: text.replace("    branches:\n      - main\n", "    branches:\n      - 'main*'\n"),
        lambda text: text.replace("        uses: actions/checkout@v4\n",
                                  "        id: classify\n        uses: actions/checkout@v4\n"),
        lambda text: text.replace("        uses: actions/checkout@v4\n",
                                  "        id: Classify\n        uses: actions/checkout@v4\n"),
        lambda text: text.replace("        id: env_pins\n", "        id: env.pins\n"),
        lambda text: text.replace("        id: env_pins\n", "        id: __env_pins\n"),
    ],
    ids=["renamed", "added", "unsupported-key", "checkout-ref", "checkout-submodules", "checkout-depth",
         "setup-python-input", "runner", "workflow-env", "checkout-revision", "setup-python-revision",
         "runner-variable-in-run", "runner-variable-step-env", "runner-variable-job-env", "checkout-credentials",
         "checkout-condition", "install-env", "step-env-not-a-mapping", "runner-label", "executed-without-run",
         "second-job", "structured-env-value", "step-if-not-a-string", "install-condition",
         "setup-python-condition", "install-condition-removed", "run-boolean", "step-env-float",
         "permissions-scalar", "permissions-value", "name-boolean", "run-name-added", "concurrency-key-removed",
         "pull-request-path-removed", "push-branch", "repeated-id", "repeated-id-case", "id-form", "id-reserved"],
)
def test_replay_inventory_drift_is_a_tooling_failure(mutate) -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    mutated = mutate(text)
    assert mutated != text
    with pytest.raises(tool.ToolingError, match="REPLAY_INVENTORY_DRIFT"):
        tool.replay_steps(mutated)


def test_the_workflow_header_is_compared_with_its_scalar_types(monkeypatch: pytest.MonkeyPatch) -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    monkeypatch.setitem(tool.REPLAY_WORKFLOW_HEADER, "name", "true")
    assert len(tool.replay_steps(text.replace("name: ci\n", "name: 'true'\n", 1))[1]) == len(tool.REPLAY_INVENTORY)
    # Plain, the same text is a YAML boolean, which GitHub does not read as the string.
    with pytest.raises(tool.ToolingError, match="REPLAY_INVENTORY_DRIFT: .*: name$"):
        tool.replay_steps(text.replace("name: ci\n", "name: true\n", 1))


def test_replay_needs_an_x86_64_linux_machine(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(tool.sys, "platform", "linux")
    monkeypatch.setattr(tool.platform, "machine", lambda: "x86_64")
    assert tool.replay_machine() is None
    monkeypatch.setattr(tool.platform, "machine", lambda: "aarch64")
    assert tool.replay_machine() == "linux aarch64"
    monkeypatch.setattr(tool.platform, "machine", lambda: "x86_64")
    monkeypatch.setattr(tool.sys, "platform", "darwin")
    assert tool.replay_machine() == "darwin x86_64"


def test_a_temporary_directory_inside_the_repository_is_refused_before_anything_is_created(tmp_path: Path) -> None:
    repo = _synthetic(tmp_path / "temp-inside", {"data.txt": "tracked\n"})
    (repo / "scratch").mkdir()  # empty, so git status stays clean
    result = _run(repo, "build-notes", extra_env={"TMPDIR": str(repo / "scratch")})
    assert result.returncode == tool.EXIT_REFUSED, result.stdout + result.stderr
    assert "PREPUSH_CHECK_REFUSED: the temporary directory would be inside the repository" in result.stderr
    assert not any((repo / "scratch").iterdir())


def test_a_step_that_is_not_a_mapping_is_refused() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    mutated = text.replace("      - name: Verify truthful applicability",
                           "      - echo hi\n\n      - name: Verify truthful applicability")
    assert mutated != text
    with pytest.raises(tool.ToolingError, match="unsupported shape"):
        tool.replay_steps(mutated)
    nested_job_env = text.replace("      APP_ENV: dev\n", "      APP_ENV:\n        nested: invalid\n", 1)
    assert nested_job_env != text
    with pytest.raises(tool.ToolingError, match="unsupported shape"):
        tool.replay_steps(nested_job_env)


@pytest.mark.parametrize("value", ["{nested: invalid}", "[a, b]", "&anchor x", "*alias", "!tag x", "|+", ">2",
                                   '"echo replay_pass\\nexit 1"', '"unterminated', "'a' b", "a: b", "- x", "# c",
                                   "]", "}", ",x", "] x", "-\tx", "?\tx", ":\tx", "? x", "foo:\tbar"])
def test_yaml_forms_the_parser_does_not_model_are_refused(value: str) -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    mutated = text.replace("          BASE_SHA: ${{ github.event.pull_request.base.sha || github.event.before }}",
                           f"          BASE_SHA: {value}")
    assert mutated != text
    with pytest.raises(tool.ToolingError, match="unsupported YAML value"):
        tool.replay_steps(mutated)


def test_quoted_scalars_and_keys_are_read_as_yaml_reads_them() -> None:
    assert tool._plain('"x" # comment') == "x"
    assert tool._plain("'it''s'  # comment") == "it's"
    assert tool._plain("plain value\t# comment") == "plain value"
    # "-", "?" and ":" followed by a non-space begin a plain scalar, and flow indicators may follow its first character.
    for value in ("-x", "?x", ":x", "a,b", "a]", "x}", "foo:bar"):
        assert tool._plain(value) == value
    # GitHub rejects a repeated key; a key is a plain word followed by ': '.
    text = WORKFLOW.read_text(encoding="utf-8")
    line = "        run: python3 ci/checks/check_agents_md_citations.py\n"
    for mutated, message in ((text.replace(line, line + "        run: exit 0\n"), "repeated"),
                             (text.replace(line, line.replace("run: ", "run:")), "unsupported workflow key"),
                             (text.replace(line, line.replace("run:", '"run":')), "unsupported workflow key")):
        assert mutated != text
        with pytest.raises(tool.ToolingError, match=message):
            tool.replay_steps(mutated)


def test_implicitly_typed_scalars_are_refused_unless_github_writes_them_back_unchanged() -> None:
    # GitHub reads the workflow as YAML 1.2 and writes an env value it reads as a boolean or an integer back as
    # true, false or decimal; any other spelling, a null or a float would become another string.
    text = WORKFLOW.read_text(encoding="utf-8")
    env_line = "      APP_ENV: dev\n"
    for value in ("1.0", "0x10", "010", "+1", "True", "~", "null", ".inf"):
        with pytest.raises(tool.ToolingError, match="unsupported shape"):
            tool.replay_steps(text.replace(env_line, f"      APP_ENV: {value}\n"))
    for value in ("true", "false", "0", "12", "-3"):
        assert tool.replay_steps(text.replace(env_line, f"      APP_ENV: {value}\n"))[0].env["APP_ENV"] == value
    with pytest.raises(tool.ToolingError, match="unsupported workflow key"):
        tool.replay_steps(text.replace(env_line, env_line + "      true: x\n"))
    assert isinstance(tool._plain("TRUE"), tool._Resolved) and not isinstance(tool._plain("'true'"), tool._Resolved)
    assert not isinstance(tool._plain("ubuntu-latest"), tool._Resolved)


def test_the_whole_workflow_is_one_mapping_without_repeated_keys() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    second_jobs = "\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - name: only\n        run: exit 1\n"
    for appended in ("\nname: other\n", second_jobs):
        with pytest.raises(tool.ToolingError, match="repeated"):
            tool.replay_steps(text + appended)
    # The sweep's coverage reads the jobs through the same parse.
    with pytest.raises(tool.ToolingError, match="repeated"):
        tool.pytest_command_tokens(text + second_jobs)


def test_sequence_entries_share_one_indentation() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    entries = "    paths:\n      - '**'\n      - '!docs/crd/**'\n"
    for new in ("    paths:\n      - '**'\n        - '!docs/crd/**'\n",
                "    paths:\n        - '**'\n      - '!docs/crd/**'\n"):
        mutated = text.replace(entries, new, 1)
        assert mutated != text
        with pytest.raises(tool.ToolingError, match="indented differently from its sequence's first entry"):
            tool.replay_steps(mutated)


def test_tabs_in_indentation_are_refused_and_elsewhere_read_as_yaml_reads_them() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    body = "          set -euo pipefail\n"
    for old, new in (("name: ci\n", "\tname: ci\n"), ("  contents: read\n", "\tcontents: read\n"),
                     ("      - main\n", "    \t- main\n"), (body, "        \tset -euo pipefail\n"),
                     ("permissions:\n", "permissions:\n \t\n")):
        mutated = text.replace(old, new, 1)
        assert mutated != text
        with pytest.raises(tool.ToolingError, match="a tab in the indentation of line"):
            tool.replay_steps(mutated)
    with pytest.raises(tool.ToolingError, match="whitespace with a tab"):
        tool.replay_steps(text.replace(body, body + "\t\n", 1))
    # A tab after a block's indentation is content, and one after a key's colon separates its value.
    assert tool.replay_steps(text.replace(body, "          \tset -euo pipefail\n", 1))[1][1]["run"].startswith(
        "\tset -euo pipefail\n")
    tab_separated = text.replace("  contents: read\n", "  contents:\tread\n")
    assert len(tool.replay_steps(tab_separated)[1]) == len(tool.REPLAY_INVENTORY)


def test_block_scalars_are_read_as_yaml_reads_them_or_refused() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    line = "        run: python3 ci/checks/check_agents_md_citations.py\n"

    def run_of(block: str) -> object:
        mutated = text.replace(line, block)
        assert mutated != text
        return tool.replay_steps(mutated)[1][2]["run"]

    assert run_of("        run: >-\n          echo a\n          echo b\n\n          echo c\n") == "echo a echo b\necho c"
    assert run_of("        run: |\n          echo a\n            echo b\n") == "echo a\n  echo b\n"
    # A folded block keeps the line breaks around a more-indented line, which is not modelled.
    with pytest.raises(tool.ToolingError, match="more indented"):
        run_of("        run: >\n          echo replay_pass\n            exit 1\n")
    with pytest.raises(tool.ToolingError, match="less indented"):
        run_of("        run: |\n            echo a\n          echo b\n")


@pytest.mark.parametrize("extra", ["\npytest", "; pytest", " && pytest", " | cat", " $(true)", " `true`",
                                   ' "$HOME"', " > log", " # note", " \\\n -r more.txt", " 'unterminated"])
def test_the_install_substitute_stands_in_for_one_simple_command_only(tmp_path: Path, extra: str) -> None:
    with pytest.raises(ValueError, match="not one simple command"):
        tool._install_check("python -m pip install pytest" + extra, tmp_path)


@pytest.mark.parametrize("run", ["python -m pip install", "pip install", "python -m pip install  "])
def test_an_install_step_with_nothing_to_install_is_refused(tmp_path: Path, run: str) -> None:
    with pytest.raises(ValueError, match="names nothing to install"):
        tool._install_check(run, tmp_path)
    outcome, detail = tool._substitute({"run": run}, "reason", tmp_path, "3.12", "3.12")
    assert outcome == "failure" and detail.startswith("TOOLING") and "names nothing to install" in detail


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


def test_expressions_cover_the_workflow_forms() -> None:
    contexts = {
        "github": {"event_name": "pull_request", "sha": "merge",
                   "event": {"before": "", "pull_request": {"base": {"sha": "b"}, "head": {"sha": "h"}}}},
        "steps": {"classify": {"outcome": "success", "outputs": {"needs_python": "true", "qa": "false"}}},
    }
    expressions = tool.Expressions(contexts, job_failed=False)
    assert tool.interpolate("${{ github.event.pull_request.head.sha || github.sha }}", expressions) == "h"
    assert tool.interpolate("${{ github.event.pull_request.base.sha || github.event.before }}", expressions) == "b"
    assert tool.interpolate('--event-name "${{ github.event_name }}"', expressions) == '--event-name "pull_request"'
    assert tool.interpolate("${{ steps.classify.outcome }}/${{ steps.missing.outcome }}", expressions) == "success/"
    assert tool.condition("${{ steps.classify.outputs.needs_python == 'true' }}", expressions) is True
    assert tool.condition("${{ steps.classify.outputs.qa == 'true' }}", expressions) is False
    expressions.job_failed = True
    assert tool.condition("${{ steps.classify.outputs.needs_python == 'true' }}", expressions) is False
    assert tool.condition("${{ always() }}", expressions) is True
    assert tool.condition(None, expressions) is False
    push = tool.Expressions({"github": {"event_name": "push", "sha": "s", "event": {"before": "p", "pull_request": {}}}},
                            job_failed=False)
    assert tool.interpolate("${{ github.event.pull_request.head.sha || github.sha }}", push) == "s"
    assert tool.interpolate("${{ github.event.pull_request.base.sha || github.event.before }}", push) == "p"
    for unsupported in ("${{ fromJSON('1') }}", "${{ secrets.TOKEN }}", "${{ matrix.os }}"):
        with pytest.raises(tool.ToolingError):
            tool.interpolate(unsupported, expressions)
    # On a pull_request the merge commit and the payload's before are not modelled: discarded by || they are
    # harmless, used they are tooling, as is any github path the replay does not model.
    pull = tool.Expressions(tool.replay_contexts("pull_request", "b", "h"), job_failed=False)
    assert tool.interpolate("${{ github.event.pull_request.head.sha || github.sha }}", pull) == "h"
    assert tool.interpolate("${{ github.event.pull_request.base.sha || github.event.before }}", pull) == "b"
    for unmodelled in ("${{ github.sha }}", "${{ github.event.before == 'x' }}", "${{ github.run_id }}",
                       "${{ github.workspace }}", "${{ github.event.pull_request.title }}", "${{ env.LC_ALL }}"):
        with pytest.raises(tool.ToolingError, match="not modelled|unsupported context"):
            tool.interpolate(unmodelled, pull)
    with pytest.raises(tool.ToolingError, match="not modelled"):
        tool.condition("${{ github.sha }}", pull)
    push = tool.Expressions(tool.replay_contexts("push", "p", "s"), job_failed=False)
    assert tool.interpolate("${{ github.sha }}/${{ github.event.before }}", push) == "s/p"
    assert tool.interpolate("${{ github.event.pull_request.head.sha || github.sha }}", push) == "s"


@pytest.mark.parametrize(
    "expression, value",
    [
        ("steps.classify.outputs.needs_python == 'true'", True),
        ("steps.classify.outputs.needs_python == 'TRUE'", True),
        ("steps.classify.outputs.needs_python != 'false'", True),
        ("github.event_name == 'push'", False),
        ("true == true", True),
        ("false != true", True),
        ("!steps.classify.outputs.needs_python == false", True),
        ("'\u00e9' == '\u00e9'", True),
        ("false == ''", "converts a boolean and a string"),
        ("false != ''", "converts a boolean and a string"),
        ("true == '1'", "converts a boolean and a string"),
        ("steps.classify.outputs.needs_python == true", "converts a boolean and a string"),
        ("'\u00e9' == '\u00c9'", "non-ASCII"),
        ("'k' == '\u212a'", "non-ASCII"),
        ("steps.classify.outputs == ''", "is an object"),
        ("steps.classify != 'x'", "is an object"),
        ("steps.classify.outputs || 'x'", "is an object"),
        ("!steps.classify", "is an object"),
    ],
)
def test_comparisons_are_github_s_where_no_conversion_is_needed_and_refused_otherwise(
        expression: str, value: object) -> None:
    # GitHub converts operands of different types to numbers (false == '' is true there) and compares objects
    # by reference; the replay models strings and booleans only.
    contexts = tool.replay_contexts("pull_request", "b", "h")
    contexts["steps"] = {"classify": {"outcome": "success", "outputs": {"needs_python": "true"}}}
    expressions = tool.Expressions(contexts, job_failed=False)
    if isinstance(value, bool):
        assert expressions.evaluate(expression) is value
    else:
        with pytest.raises(tool.ToolingError, match=value):
            expressions.evaluate(expression)
    for text in ("${{ steps.classify.outputs }}", "${{ steps.classify }}"):
        with pytest.raises(tool.ToolingError, match="is an object"):
            tool.interpolate(text, expressions)


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


def test_a_step_whose_output_the_runner_rejects_fails(tmp_path: Path) -> None:
    expressions = tool.Expressions(tool.replay_contexts("pull_request", "b", "h"), job_failed=False)
    env = tool.child_environment(dict(os.environ), tmp_path)
    copy = tmp_path / "copy"
    copy.mkdir()

    def run(body: str) -> tuple[str, str, dict[str, str]]:
        return tool._execute({"run": body, "shell": "bash"}, 1, copy, env, expressions, tmp_path)

    assert run('echo product=true >> "$GITHUB_OUTPUT"') == ("success", "", {"product": "true"})
    outcome, detail, outputs = run('echo product=true >> "$GITHUB_OUTPUT"\necho invalid >> "$GITHUB_OUTPUT"')
    assert (outcome, outputs) == ("failure", {"product": "true"})
    assert detail.startswith(f"BEHAVIOR {_REJECTED} 'invalid'")
    outcome, detail, _outputs = run('printf "body<<EOF\\nx\\nEOF\\n" >> "$GITHUB_OUTPUT"\nexit 3')
    assert outcome == "failure" and detail.splitlines()[:2] == [
        "BEHAVIOR exit 3", f"TOOLING GITHUB_OUTPUT record 'body<<EOF' {_UNMODELLED}"]


def test_lanes_refuses_classifier_output_the_runner_would_reject(tmp_path: Path) -> None:
    output, targets = tmp_path / "output.txt", tmp_path / "targets.txt"
    output.write_text("product=true\ninvalid\n", encoding="utf-8")
    targets.write_text("", encoding="utf-8")
    report = tool.Report("lanes")
    assert tool._print_outputs(report, output, targets) == {"product": "true"}
    assert report.status == "FAIL"
    assert f"lanes: FAILURE classifier output: {_REJECTED} 'invalid', which is neither NAME=VALUE nor " \
           "NAME<<DELIMITER" in report.lines


def test_interpreter_substitute_requires_the_workflow_python(tmp_path: Path) -> None:
    step = {"uses": "actions/setup-python@v5", "with": {"python-version": "3.12"}}
    outcome, detail = tool._substitute(step, "reason", tmp_path, "3.12", "3.11")
    assert outcome == "failure" and detail.startswith("TOOLING")
    assert tool._substitute(step, "reason", tmp_path, "3.12", "3.12")[0] == "success"


def _site(root: Path, distributions: dict[str, str]) -> list[str]:
    """A synthetic site directory holding the named distributions at the given versions."""
    for name, version in distributions.items():
        info = root / f"{name}-{version}.dist-info"
        info.mkdir(parents=True)
        (info / "METADATA").write_text(f"Metadata-Version: 2.1\nName: {name}\nVersion: {version}\n", encoding="utf-8")
    return [str(root)]


def test_install_substitute_checks_only_that_each_named_distribution_is_installed(tmp_path: Path) -> None:
    site = _site(tmp_path / "site", {"present": "1.0", "glow_fixture": "0.0.0"})
    (tmp_path / "requirements.txt").write_text("# fixture\npresent[extra]>=99,<100 ; python_version < '2'\n",
                                               encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text('[project]\nname = "glow-fixture"\n', encoding="utf-8")
    run = "python -m pip install 'present>=5' -r requirements.txt -e ."
    # The step's stated precondition is that CI's install is already present; versions, extras and markers
    # are the caller's to match.
    assert tool._install_check(run, tmp_path, site) == []
    (tmp_path / "requirements.txt").write_text("absent>=1\n", encoding="utf-8")
    assert tool._install_check(run, tmp_path, site) == ["absent"]
    (tmp_path / "pyproject.toml").write_text('[project]\nname = "uninstalled-project"\n', encoding="utf-8")
    assert tool._install_check(run, tmp_path, site) == ["absent", "uninstalled-project"]
    for unreadable in ("present @ https://example.invalid/present.whl", "./present", "git+https://example.invalid/x"):
        (tmp_path / "requirements.txt").write_text(unreadable + "\n", encoding="utf-8")
        with pytest.raises(ValueError, match="unsupported requirement"):
            tool._install_check(run, tmp_path, site)
    (tmp_path / "pyproject.toml").write_text("[build-system]\nrequires = []\n", encoding="utf-8")
    with pytest.raises(ValueError, match="names no \\[project\\] name"):
        tool._install_check("python -m pip install -e .", tmp_path, site)
    # Nothing beyond the [project] name is read, so a pyproject.toml change elsewhere cannot break the replay.
    (tmp_path / "pyproject.toml").write_text('[build-system]\nbuild-backend = "other"\n[project]\n'
                                             'name = "glow-fixture"\nversion = "9"\n[tool.setuptools]\nx = 1\n',
                                             encoding="utf-8")
    assert tool._install_check("python -m pip install -e .", tmp_path, site) == []
    (tmp_path / "requirements.txt").write_text("distribution-that-is-not-installed\n", encoding="utf-8")
    outcome, detail = tool._substitute({"run": "python -m pip install -r requirements.txt"}, "reason", tmp_path,
                                       "3.12", "3.12")
    assert outcome == "failure" and detail == ("TOOLING the caller's environment lacks distributions the install "
                                               "step names: distribution-that-is-not-installed")


def test_the_real_install_step_names_only_installed_distributions() -> None:
    step = next(s for s in tool.replay_steps(WORKFLOW.read_text(encoding="utf-8"))[1]
                if s["name"] == "Install applicable validation dependencies")
    outcome, detail = tool._substitute(step, "reason", ROOT, "3.12", "3.12")
    assert outcome == "success", detail
    assert detail.startswith("reason: every distribution the step names is installed")


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
    roots = guard_tokens | set(classifier._full_validation_test_targets())
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


# --------------------------------------------------------------------------
# every report on the repository: read-only, and the expected answers
# --------------------------------------------------------------------------

def test_reports_on_a_clone_of_the_repository_are_read_only(repo_clone: Path) -> None:
    from engine.config.registry_loader import ADMITTED_RELEASE_ROSTER, ADMITTED_RELEASE_VERSION

    notes = _run(repo_clone, "build-notes")
    assert notes.returncode == tool.EXIT_OK, notes.stdout + notes.stderr
    (line,) = [line for line in _report_lines(notes.stdout, "build-notes") if line.startswith("path=")]
    path, _size, digest = (part.split("=", 1)[1] for part in line.split())
    assert re.fullmatch(r"docs/pfcanon/PF10-HDE-Build-Notes-v[^/]*\.md", path)
    assert digest == hashlib.sha256((repo_clone / path).read_bytes()).hexdigest()

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

@pytest.mark.parametrize("names, ok", [((), False), (("v1.0",), True), (("v1.0", "v1.1"), False)])
def test_build_notes_requires_exactly_one_file(tmp_path: Path, names: tuple[str, ...], ok: bool) -> None:
    files = {f"docs/pfcanon/PF10-HDE-Build-Notes-{n}.md": f"notes {n}\n" for n in names}
    repo = _synthetic(tmp_path / "notes", {"README.txt": "fixture\n", "docs/pfcanon/PF01-Other.md": "x\n", **files})
    result = _run(repo, "build-notes")
    if ok:
        assert result.returncode == tool.EXIT_OK, result.stdout + result.stderr
        digest = hashlib.sha256(b"notes v1.0\n").hexdigest()
        assert f"build-notes: path=docs/pfcanon/PF10-HDE-Build-Notes-v1.0.md bytes=11 sha256={digest}" in result.stdout
    else:
        assert result.returncode == tool.EXIT_REPORT_FAILED
        assert f"found {len(names)}" in result.stdout


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
    assert set(tool.REMOVED_ENV_KEYS) == set(CHILD_KEYS) and not set(CHILD_KEYS) & set(tool.CHILD_INHERITED_KEYS)


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
# replay: a synthetic workflow with the real step inventory
# --------------------------------------------------------------------------

def _replay_workflow(product_body: str) -> str:
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    run_steps = {
        "Classify affected CI lanes": ("classify", "", (
            'test -n "$BASE_SHA" && test -n "$HEAD_SHA"\n'
            'echo "event=${{ github.event_name }}"\n'
            "printf 'product=true\\nqa=false\\nneeds_python=true\\nchanged_tests=false\\n' >> \"$GITHUB_OUTPUT\"")),
        "Check AGENTS.md cites no project documents": ("", "", "bash ci/runner_env.sh\necho citations"),
        "Verify pytest readiness": ("pytest_readiness", "needs_python", "python -m pytest --version"),
        "Verify closed deterministic environment": ("env_pins", "needs_python", (
            'test "$SAFE_MODE" = 1 && test "$ALLOW_NETWORK" = 0 && test "$TZ" = UTC\n'
            "test -z \"" + "".join(f"${{{key}:-}}" for key in CHILD_KEYS) + "\"\n"
            'test -n "$RUNNER_TEMP"')),
        "Run affected behavioral tests in isolation": ("changed_tests", "changed_tests", "exit 1"),
        "Run product mechanics and ordering lane": ("product_lane", "product", product_body),
        "Run CLI and compatibility lane": ("compat_lane", "compat", "exit 1"),
        "Run database and runtime-contract lane": ("db_lane", "db", "exit 1"),
        "Run rails policy and secret-safety lane": ("rails_lane", "rails", "exit 1"),
        "Run governed evidence integrity lane": ("evidence_lane", "evidence", "exit 1"),
        "Run approved generic QA subsystem lane in isolation": ("qa_lane", "qa", "exit 1"),
        "Build and verify exact-source release attestation": ("release_lane", "release", "exit 1"),
    }
    header = WORKFLOW.read_text(encoding="utf-8").split("\njobs:\n", 1)[0]
    lines = header.splitlines() + ["jobs:", "  test:", "    runs-on: ubuntu-latest", "    env:"]
    lines += [f'      {k}: "{v}"' for k, v in tool.CLOSED_RAILS.items()]
    lines.append("    steps:")
    for name, _kind, _reason in tool.REPLAY_INVENTORY:
        lines.append(f"      - name: {name}")
        if name == "Check out exact candidate head":
            lines += ["        uses: actions/checkout@v4", "        with:", "          fetch-depth: 0",
                      "          persist-credentials: false",
                      "          ref: ${{ github.event.pull_request.head.sha || github.sha }}"]
        elif name == "Set up Python 3.12":
            lines += ["        id: python_setup", "        if: ${{ steps.classify.outputs.needs_python == 'true' }}",
                      "        uses: actions/setup-python@v5", "        with:", f"          python-version: '{version}'"]
        elif name == "Install applicable validation dependencies":
            lines += ["        id: dependencies", "        if: ${{ steps.classify.outputs.needs_python == 'true' }}",
                      "        run: >-", "          python -m pip install", "          -r requirements.txt"]
        elif name == "Verify truthful applicability and clean candidate tree":
            lines += ["        id: final_audit", "        if: ${{ always() }}", "        shell: bash", "        env:",
                      "          SETUP: ${{ steps.python_setup.outcome }}",
                      "          DEPS: ${{ steps.dependencies.outcome }}",
                      "          PRODUCT: ${{ steps.product_lane.outcome }}",
                      "          QA: ${{ steps.qa_lane.outcome }}",
                      "        run: |",
                      '          test "$SETUP/$DEPS/$PRODUCT/$QA" = "success/success/success/skipped"',
                      "          test -z \"$(git status --short --untracked-files=all)\"",
                      "          echo CI_APPLICABILITY_AND_EXACT_HEAD_OK"]
        else:
            step_id, flag, body = run_steps[name]
            if step_id:
                lines.append(f"        id: {step_id}")
            if name == "Classify affected CI lanes":
                lines += ["        env:", "          BASE_SHA: ${{ github.event.pull_request.base.sha || github.event.before }}",
                          "          HEAD_SHA: ${{ github.event.pull_request.head.sha || github.sha }}"]
            if flag:
                lines.append(f"        if: ${{{{ steps.classify.outputs.{flag} == 'true' }}}}")
            lines += ["        shell: bash", "        run: |"] + [f"          {line}" for line in body.splitlines()]
        lines.append("")
    return "\n".join(lines)


def _pinned_tool(tmp_path: Path, workflow: str) -> Path:
    """A copy of the tool whose REPLAY_WORKFLOW_SHA256 is the given workflow's."""
    source = TOOL.read_text(encoding="utf-8")
    pin = f'REPLAY_WORKFLOW_SHA256 = "{tool.REPLAY_WORKFLOW_SHA256}"'
    assert source.count(pin) == 1
    copy = tmp_path / "pinned-tool" / "prepush_check.py"
    copy.parent.mkdir()
    copy.write_text(source.replace(pin, f'REPLAY_WORKFLOW_SHA256 = "{hashlib.sha256(workflow.encode()).hexdigest()}"'),
                    encoding="utf-8")
    return copy


@pytest.mark.parametrize("product_body, ok", [("echo PRODUCT_RAN", True), ("echo PRODUCT_FAILED\nexit 1", False)],
                         ids=["green", "lane-fails"])
def test_replay_runs_a_synthetic_workflow_in_a_throwaway_copy(tmp_path: Path, product_body: str, ok: bool) -> None:
    workflow = _replay_workflow(product_body)
    repo = _synthetic(tmp_path / "replay", {
        ".github/workflows/ci.yml": workflow,
        "requirements.txt": "pytest\n",
        # A script a step calls sees only the runner variables the replay models and none of the caller's others.
        "ci/runner_env.sh": ('set -e\n'
                             'test -z "${GITHUB_SHA:-}${RUNNER_OS:-}${GITHUB_WORKSPACE:-}${AWS_SECRET_ACCESS_KEY:-}"\n'
                             'test "$GITHUB_ACTIONS/$GITHUB_EVENT_NAME" = true/pull_request\n'),
    })
    # The real tool refuses a workflow other than the one it models, before reading it.
    refused = _run(repo, "replay", "--full")
    assert refused.returncode == tool.EXIT_REPORT_FAILED, refused.stdout + refused.stderr
    assert ("replay: TOOLING_FAILURE REPLAY_INVENTORY_DRIFT: the head's .github/workflows/ci.yml has SHA-256 "
            f"{hashlib.sha256(workflow.encode()).hexdigest()}, not the modelled {tool.REPLAY_WORKFLOW_SHA256}") \
        in refused.stdout
    assert not any(line.startswith("replay: step ") for line in refused.stdout.splitlines())
    result = _run(repo, "replay", "--full", tool_path=_pinned_tool(tmp_path, workflow),
                  extra_env={"GITHUB_SHA": "caller", "RUNNER_OS": "caller", "GITHUB_WORKSPACE": "/caller",
                             "AWS_SECRET_ACCESS_KEY": "aws-dummy"})
    lines = _report_lines(result.stdout, "replay")
    steps = {line.split(" ", 3)[1]: line for line in lines if line.startswith("step ")}
    assert len(steps) == len(tool.REPLAY_INVENTORY)
    assert steps["01"].startswith("step 01 SUCCESS [excluded, substituted]")
    assert steps["04"].startswith("step 04 SUCCESS [excluded, substituted]")
    assert steps["05"].startswith("step 05 SUCCESS [excluded, substituted]")
    assert steps["08"].startswith("step 08 SKIPPED")
    assert steps["14"].startswith("step 14 SKIPPED")
    assert "  event=pull_request" in lines
    if ok:
        assert result.returncode == tool.EXIT_OK, result.stdout + result.stderr
        assert steps["09"].startswith("step 09 SUCCESS")
        assert steps["16"].startswith("step 16 SUCCESS")
        assert "  CI_APPLICABILITY_AND_EXACT_HEAD_OK" in lines
    else:
        assert result.returncode == tool.EXIT_REPORT_FAILED
        assert steps["09"].startswith("step 09 FAILURE")
        assert "  BEHAVIOR exit 1" in lines and "  PRODUCT_FAILED" in lines
        assert steps["16"].startswith("step 16 FAILURE")
        assert "  CI_APPLICABILITY_AND_EXACT_HEAD_OK" not in lines
