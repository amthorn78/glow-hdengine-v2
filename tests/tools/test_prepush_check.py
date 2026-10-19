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


def _run(repo: Path, *args: str, extra_env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    """Run the tool against ``repo`` and assert the read-only rule around it."""
    env = {**os.environ, **DUMMY_KEYS, **(extra_env or {})}
    before = _snapshot(repo)
    result = subprocess.run([sys.executable, str(TOOL), *args, "--repo-root", str(repo)],
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
    ],
    ids=["renamed", "added", "unsupported-key"],
)
def test_replay_inventory_drift_is_a_tooling_failure(mutate) -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    mutated = mutate(text)
    assert mutated != text
    with pytest.raises(tool.ToolingError, match="REPLAY_INVENTORY_DRIFT"):
        tool.replay_steps(mutated)


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


def test_interpreter_substitute_requires_the_workflow_python(tmp_path: Path) -> None:
    step = {"uses": "actions/setup-python@v5", "with": {"python-version": "3.12"}}
    outcome, detail = tool._substitute(step, "reason", tmp_path, "3.12", "3.11")
    assert outcome == "failure" and detail.startswith("TOOLING")
    assert tool._substitute(step, "reason", tmp_path, "3.12", "3.12")[0] == "success"


# --------------------------------------------------------------------------
# sweep: the coverage definition (contract G-2)
# --------------------------------------------------------------------------

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
    assert "lanes: TOOLING_FAILURE FileNotFoundError" in result.stdout
    assert "membership: TOOLING_FAILURE FileNotFoundError" in result.stdout
    assert "PREPUSH_CHECK_RESULT: FAIL lanes=FAIL membership=FAIL; repository unchanged" in result.stdout


def test_child_environment_is_closed_rails_without_keys(tmp_path: Path) -> None:
    base = {**DUMMY_KEYS, "PATH": "/usr/bin", "SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "prod",
            "GIT_OPTIONAL_LOCKS": "0", "HOME": "/home/x"}
    env = tool.child_environment(base, tmp_path)
    assert not set(DUMMY_KEYS) & set(env)
    assert {k: env[k] for k in tool.CLOSED_RAILS} == tool.CLOSED_RAILS
    assert env["PATH"].split(os.pathsep)[0] == str(Path(sys.executable).parent)
    assert env["TMPDIR"].startswith(str(tmp_path)) and env["XDG_STATE_HOME"].startswith(str(tmp_path))
    assert "GIT_OPTIONAL_LOCKS" not in env and env["HOME"] == "/home/x"
    assert set(tool.REMOVED_ENV_KEYS) == set(CHILD_KEYS)


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
        "Check AGENTS.md cites no project documents": ("", "", "echo citations"),
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
    lines = ["name: ci", "jobs:", "  test:", "    runs-on: ubuntu-latest", "    env:"]
    lines += [f'      {k}: "{v}"' for k, v in tool.CLOSED_RAILS.items()]
    lines.append("    steps:")
    for name, _kind, _reason in tool.REPLAY_INVENTORY:
        lines.append(f"      - name: {name}")
        if name == "Check out exact candidate head":
            lines += ["        uses: actions/checkout@v4", "        with:", "          fetch-depth: 0"]
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


@pytest.mark.parametrize("product_body, ok", [("echo PRODUCT_RAN", True), ("echo PRODUCT_FAILED\nexit 1", False)],
                         ids=["green", "lane-fails"])
def test_replay_runs_a_synthetic_workflow_in_a_throwaway_copy(tmp_path: Path, product_body: str, ok: bool) -> None:
    repo = _synthetic(tmp_path / "replay", {
        ".github/workflows/ci.yml": _replay_workflow(product_body),
        "requirements.txt": "pytest\n",
    })
    result = _run(repo, "replay", "--full")
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
