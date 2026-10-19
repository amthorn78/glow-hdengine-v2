#!/usr/bin/env python3
"""Read-only pre-push and pre-plan check (HDE-CRD-0002 S20).

One command with five reports, each read-only with respect to the repository:

* ``lanes``: the CI lane classification for a base and head, or for given
  paths, delegated to ``ci/checks/classify_ci_changes.py``;
* ``membership``: whether given paths are members of the admitted release
  roster;
* ``build-notes``: the unique ``docs/pfcanon/PF10-HDE-Build-Notes-v*.md`` and
  its SHA-256;
* ``sweep``: the tracked test files no CI lane and no full-validation target
  reaches, run in a throwaway copy of the head;
* ``replay``: every step of the ``test`` job of ``.github/workflows/ci.yml``,
  read from the head's workflow text and replayed in a throwaway copy.

Every write goes under one owner-only temporary directory outside the
repository, removed at exit.  The tool refuses a dirty tree, acts on committed
revisions only, resolves refs locally, opens no network connection and runs
children under closed rails.  Its green is not CI's green and not QA; its
output is not governed evidence.
"""
from __future__ import annotations

import sys

# Importing repository modules must not write __pycache__ into the checkout.
sys.dont_write_bytecode = True

import argparse  # noqa: E402
import ast  # noqa: E402
import fnmatch  # noqa: E402
import hashlib  # noqa: E402
import importlib.metadata  # noqa: E402
import importlib.util  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import platform  # noqa: E402
import re  # noqa: E402
import shlex  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import tempfile  # noqa: E402
import time  # noqa: E402
import tomllib  # noqa: E402
import xml.etree.ElementTree as ET  # noqa: E402
from dataclasses import dataclass, field  # noqa: E402
from pathlib import Path, PurePosixPath  # noqa: E402
from typing import Iterable, Sequence  # noqa: E402

TOOL_PATH = Path(__file__).resolve()
ROOT = TOOL_PATH.parents[2]
REPORTS = ("lanes", "membership", "build-notes", "sweep", "replay")
WORKFLOW_PATH = ".github/workflows/ci.yml"
CLASSIFIER_PATH = "ci/checks/classify_ci_changes.py"
REGISTRY_LOADER_PATH = "engine/config/registry_loader.py"
MANIFEST_PATH = "catalog/manifest.json"
BUILD_NOTES_DIRECTORY = "docs/pfcanon/"
BUILD_NOTES_PATTERN = "docs/pfcanon/PF10-HDE-Build-Notes-v*.md"
REPLAY_JOB = "test"
DEFAULT_BASE = "origin/main"
DEFAULT_HEAD = "HEAD"

EXIT_OK = 0
EXIT_REPORT_FAILED = 1
EXIT_USAGE = 2
EXIT_REFUSED = 3
EXIT_READ_ONLY_VIOLATION = 4

# Removed from every child environment (vendor, database and GitHub keys).
REMOVED_ENV_KEYS = (
    "DATABASE_URL",
    "ENGINE_ENV",
    "GEO_API_KEY",
    "GH_TOKEN",
    "GITHUB_TOKEN",
    "HDAPI_BASE_URL",
    "HDAPI_KEY",
    "HDE_VENDOR_OVERRIDE_AUDIT_PATH",
    "HD_API_BASE_URL",
    "HD_API_KEY",
    "HD_GEOCODE_KEY",
)
# The only environment values the tool prints.
PRINTED_PINS = ("LC_ALL", "LANG", "TZ", "SAFE_MODE", "ALLOW_NETWORK", "APP_ENV")
CLOSED_RAILS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
    "PYTHONDONTWRITEBYTECODE": "1",
}
SWEEP_TOOLS = ("bash", "curl", "ruby")

# Every step of the ``test`` job, in file order.  A step the workflow adds,
# renames or removes fails the replay (and the owner test) until this list
# knows it, so the replay never silently runs a different job.
REPLAY_EXCLUDED = "excluded"
REPLAY_EXECUTED = "executed"
REPLAY_INVENTORY: tuple[tuple[str, str, str], ...] = (
    ("Check out exact candidate head", REPLAY_EXCLUDED,
     "uses: actions/checkout; replaced by a throwaway clone of the head outside the repository"),
    ("Classify affected CI lanes", REPLAY_EXECUTED, ""),
    ("Check AGENTS.md cites no project documents", REPLAY_EXECUTED, ""),
    ("Set up Python 3.12", REPLAY_EXCLUDED,
     "uses: actions/setup-python; replaced by the caller's interpreter, whose major.minor must equal python-version"),
    ("Install applicable validation dependencies", REPLAY_EXCLUDED,
     "needs the package index; the caller's environment must already hold every distribution the step installs"),
    ("Verify pytest readiness", REPLAY_EXECUTED, ""),
    ("Verify closed deterministic environment", REPLAY_EXECUTED, ""),
    ("Run affected behavioral tests in isolation", REPLAY_EXECUTED, ""),
    ("Run product mechanics and ordering lane", REPLAY_EXECUTED, ""),
    ("Run CLI and compatibility lane", REPLAY_EXECUTED, ""),
    ("Run database and runtime-contract lane", REPLAY_EXECUTED, ""),
    ("Run rails policy and secret-safety lane", REPLAY_EXECUTED, ""),
    ("Run governed evidence integrity lane", REPLAY_EXECUTED, ""),
    ("Run approved generic QA subsystem lane in isolation", REPLAY_EXECUTED, ""),
    ("Build and verify exact-source release attestation", REPLAY_EXECUTED, ""),
    ("Verify truthful applicability and clean candidate tree", REPLAY_EXECUTED, ""),
)
REPLAY_STEP_KEYS = frozenset({"name", "id", "if", "uses", "shell", "run", "env", "with"})
REPLAY_JOB_KEYS = frozenset({"runs-on", "env", "steps"})

_TESTS_TOKEN_RE = re.compile(r"tests/[A-Za-z0-9_./-]+")
# PEP 508 requirements as the install step and installed metadata write them:
# a distribution, optional extras, PEP 440 clauses (optionally parenthesized)
# and an environment marker.  A URL, a local-version clause, a legacy marker
# name or any other form the replay cannot verify fails closed.
_REQUIREMENT_RE = re.compile(
    r"([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)\s*(?:\[([A-Za-z0-9._,\s-]*)\])?"
    r"\s*(\([^()]*\)|[^;()]*?)\s*(?:;\s*(.*\S))?\s*")
_CLAUSE_RE = re.compile(r"(===|~=|==|!=|<=|>=|<|>)\s*([^\s,;()]+)")
_WILDCARD_RE = re.compile(r"(?:[0-9]+!)?[0-9]+(?:\.[0-9]+)*\.\*")
_MARKER_TOKEN_RE = re.compile(
    r"\s*(?:(?P<paren>[()])|(?P<op>===|==|!=|<=|>=|~=|<|>|not\s+in\b|in\b)|(?P<bool>and\b|or\b)"
    r"|'(?P<single>[^']*)'|\"(?P<double>[^\"]*)\"|(?P<var>[a-z_]+))")
# Version comparison applies only to these variables; the others compare as
# strings with ==, !=, in and not in, and any other operator on them fails
# closed (packaging releases disagree there).
_MARKER_VERSION_VARIABLES = frozenset({"implementation_version", "platform_release", "python_full_version",
                                       "python_version"})
_MARKER_VARIABLES = frozenset({
    "extra", "implementation_name", "implementation_version", "os_name", "platform_machine",
    "platform_python_implementation", "platform_release", "platform_system", "platform_version",
    "python_full_version", "python_version", "sys_platform",
})
_VERSION_RE = re.compile(
    r"v?(?:([0-9]+)!)?([0-9]+(?:\.[0-9]+)*)"
    r"(?:[-_.]?(alpha|beta|preview|pre|rc|a|b|c)[-_.]?([0-9]*))?"
    r"(?:-([0-9]+)|[-_.]?(?:post|rev|r)[-_.]?([0-9]*))?"
    r"(?:[-_.]?(dev)[-_.]?([0-9]*))?"
    r"(\+[a-z0-9]+(?:[-_.][a-z0-9]+)*)?", re.IGNORECASE)
_PRE_RANK = {"alpha": 0, "a": 0, "beta": 1, "b": 1, "preview": 2, "pre": 2, "rc": 2, "c": 2}
_EXPRESSION_RE = re.compile(r"\$\{\{(.*?)\}\}", re.DOTALL)
_STATUS_FUNCTIONS = ("always()", "success()", "failure()", "cancelled()")


class ToolingError(RuntimeError):
    """A report could not run as specified (distinct from a behavior failure)."""


class Refusal(RuntimeError):
    """The invocation is refused before any report runs."""


# --------------------------------------------------------------------------
# Git and repository state (never writes to the repository)
# --------------------------------------------------------------------------

def _git_env() -> dict[str, str]:
    env = dict(os.environ)
    # A plain ``git status`` rewrites .git/index after a timestamp change.
    env["GIT_OPTIONAL_LOCKS"] = "0"
    for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
        env.pop(key, None)
    return env


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        env=_git_env(),
        capture_output=True,
        check=False,
    )
    if check and result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise ToolingError(f"git {' '.join(args)} failed: {message}")
    return result


def git_text(repo: Path, *args: str) -> str:
    return git(repo, *args).stdout.decode("utf-8").strip()


def resolve_commit(repo: Path, ref: str) -> str:
    result = git(repo, "rev-parse", "--verify", "--quiet", "--end-of-options", f"{ref}^{{commit}}", check=False)
    if result.returncode != 0:
        raise ToolingError(f"ref {ref!r} does not resolve to a local commit (refs are not fetched)")
    return result.stdout.decode("ascii").strip()


def _metadata_digest(directory: Path) -> str:
    """Digest of git metadata: file bytes, plus names and sizes under objects/."""
    digest = hashlib.sha256()
    for path in sorted(p for p in directory.rglob("*") if p.is_file() or p.is_symlink()):
        rel = path.relative_to(directory).as_posix()
        if rel.startswith("objects/"):
            digest.update(f"{rel}\0{path.lstat().st_size}\0".encode())
            continue
        digest.update(rel.encode() + b"\0")
        if path.is_symlink():
            digest.update(os.readlink(path).encode())
        else:
            digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


@dataclass(frozen=True)
class RepositoryState:
    head: str
    status: bytes
    metadata: tuple[tuple[str, str], ...]


def repository_state(repo: Path) -> RepositoryState:
    head = git_text(repo, "rev-parse", "--verify", "HEAD")
    status = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all").stdout
    directories = {
        Path(git_text(repo, "rev-parse", "--absolute-git-dir")),
        (repo / git_text(repo, "rev-parse", "--git-common-dir")).resolve(),
    }
    metadata = tuple(sorted((str(d), _metadata_digest(d)) for d in directories))
    return RepositoryState(head=head, status=status, metadata=metadata)


def make_copy(repo: Path, commit: str, destination: Path) -> Path:
    """Clone ``commit`` outside the repository; the source repository is only read."""
    result = subprocess.run(
        ["git", "clone", "--quiet", "--shared", "--no-checkout", "--", str(repo), str(destination)],
        env=_git_env(),
        capture_output=True,
        check=False,
        cwd=destination.parent,
    )
    if result.returncode != 0:
        raise ToolingError("git clone into the temporary directory failed: "
                           + result.stderr.decode("utf-8", errors="replace").strip())
    if git(destination, "cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode != 0:
        raise ToolingError(f"commit {commit} is not available to the throwaway copy")
    git(destination, "-c", "advice.detachedHead=false", "checkout", "--quiet", "--detach", commit)
    if git_text(destination, "rev-parse", "HEAD") != commit:
        raise ToolingError("throwaway copy is not at the requested commit")
    return destination


def copy_status(copy: Path) -> tuple[bool, str]:
    diff = subprocess.run(["git", "-C", str(copy), "diff", "--exit-code", "--name-only"],
                          capture_output=True, text=True, check=False)
    status = subprocess.run(["git", "-C", str(copy), "status", "--short", "--untracked-files=all"],
                            capture_output=True, text=True, check=False)
    clean = diff.returncode == 0 and not status.stdout.strip()
    return clean, status.stdout.strip()


# --------------------------------------------------------------------------
# Repository modules, loaded from a given root without writing bytecode
# --------------------------------------------------------------------------

_LOADED = 0


def load_classifier(root: Path):
    global _LOADED
    _LOADED += 1
    name = f"_prepush_classifier_{_LOADED}"
    spec = importlib.util.spec_from_file_location(name, root / CLASSIFIER_PATH)
    if spec is None or spec.loader is None:
        raise ToolingError(f"cannot load {CLASSIFIER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def admitted_release(root: Path) -> tuple[str, frozenset[str]]:
    """Read ADMITTED_RELEASE_VERSION and ADMITTED_RELEASE_ROSTER by AST; never imports."""
    tree = ast.parse((root / REGISTRY_LOADER_PATH).read_text(encoding="utf-8"))
    values: dict[str, ast.expr] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            values[node.targets[0].id] = node.value
    try:
        version = ast.literal_eval(values["ADMITTED_RELEASE_VERSION"])
        roster_node = values["ADMITTED_RELEASE_ROSTER"]
        while isinstance(roster_node, ast.Call) and isinstance(roster_node.func, ast.Name) \
                and roster_node.func.id in {"tuple", "sorted", "frozenset"} and len(roster_node.args) == 1:
            roster_node = roster_node.args[0]
        roster = ast.literal_eval(roster_node)
    except (KeyError, ValueError) as exc:
        raise ToolingError(f"ADMITTED_RELEASE_ROSTER is not a literal in {REGISTRY_LOADER_PATH}") from exc
    if not isinstance(version, str) or not all(isinstance(p, str) for p in roster):
        raise ToolingError("admitted release constants have an unexpected shape")
    return version, frozenset(roster)


# --------------------------------------------------------------------------
# Workflow text (standard library only; the subset ci.yml uses)
# --------------------------------------------------------------------------

@dataclass
class Job:
    keys: dict[str, object]
    env: dict[str, str]
    steps: list[dict[str, object]]


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _plain(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        inner = value[1:-1]
        return inner.replace("''", "'") if value[0] == "'" else inner
    if " #" in value:
        value = value.split(" #", 1)[0].rstrip()
    return value


def _block(lines: list[str], start: int, parent_indent: int, style: str) -> tuple[str, int]:
    body: list[str] = []
    index = start
    block_indent = None
    while index < len(lines):
        line = lines[index]
        if line.strip() and _indent(line) <= parent_indent:
            break
        if line.strip() and block_indent is None:
            block_indent = _indent(line)
        body.append(line[block_indent:] if block_indent is not None and line.strip() else "")
        index += 1
    while body and not body[-1]:
        body.pop()
    if style.startswith("|"):
        text = "\n".join(body)
    else:
        paragraphs: list[str] = []
        current: list[str] = []
        for item in body:
            if item:
                current.append(item)
            else:
                paragraphs.append(" ".join(current))
                current = []
        paragraphs.append(" ".join(current))
        text = "\n".join(paragraphs)
    if not style.endswith("-"):
        text += "\n"
    return text, index


def _mapping(lines: list[str], start: int, parent_indent: int) -> tuple[dict[str, object], int]:
    result: dict[str, object] = {}
    index = start
    key_indent = None
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        indent = _indent(line)
        if indent <= parent_indent:
            break
        if key_indent is None:
            key_indent = indent
        if indent != key_indent or line.lstrip().startswith("- "):
            raise ToolingError(f"unsupported workflow structure at line {index + 1}")
        key, sep, rest = line.strip().partition(":")
        if not sep:
            raise ToolingError(f"unsupported workflow line {index + 1}")
        rest = rest.strip()
        index += 1
        if rest in {"|", "|-", ">", ">-"}:
            result[key], index = _block(lines, index, indent, rest)
        elif rest == "":
            if index < len(lines) and lines[index].strip().startswith("- ") and _indent(lines[index]) > indent:
                result[key], index = _sequence(lines, index, indent)
            else:
                result[key], index = _mapping(lines, index, indent)
        else:
            result[key] = _plain(rest)
    return result, index


def _sequence(lines: list[str], start: int, parent_indent: int) -> tuple[list[object], int]:
    items: list[object] = []
    index = start
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        indent = _indent(line)
        if indent <= parent_indent or not line.lstrip().startswith("- "):
            break
        content = line[indent + 2:]
        if ":" in content and not content.lstrip().startswith(("'", '"')):
            # A mapping item: re-read its first line as a key at indent + 2.
            lines = lines[:index] + [" " * (indent + 2) + content] + lines[index + 1:]
            item, index = _mapping(lines, index, indent)
            items.append(item)
        else:
            items.append(_plain(content))
            index += 1
    return items, index


def parse_jobs(text: str) -> dict[str, Job]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.rstrip() == "jobs:":
            mapping, _ = _mapping(lines, index + 1, 0)
            break
    else:
        raise ToolingError(f"{WORKFLOW_PATH} has no jobs")
    jobs: dict[str, Job] = {}
    for name, body in mapping.items():
        if not isinstance(body, dict):
            raise ToolingError(f"job {name!r} is not a mapping")
        steps = body.get("steps", [])
        env = body.get("env", {})
        if not isinstance(steps, list) or not isinstance(env, dict):
            raise ToolingError(f"job {name!r} has an unsupported shape")
        jobs[name] = Job(keys=body, env={k: str(v) for k, v in env.items()},
                         steps=[s for s in steps if isinstance(s, dict)])
    return jobs


def pytest_command_tokens(text: str) -> set[str]:
    """``tests/...`` tokens of ``python -m pytest`` commands in every step's ``run:``."""
    tokens: set[str] = set()
    for job in parse_jobs(text).values():
        for step in job.steps:
            run = step.get("run")
            if not isinstance(run, str):
                continue
            for command in run.replace("\\\n", " ").splitlines():
                if "python -m pytest" not in command:
                    continue
                try:
                    words = shlex.split(command, comments=True)
                except ValueError:
                    words = command.split()
                for word in words:
                    if word.startswith("tests/"):
                        tokens.add(word)
    return tokens


def anywhere_tokens(text: str) -> set[str]:
    """Every ``tests/`` token anywhere in the workflow (the coverage guard's set)."""
    return set(_TESTS_TOKEN_RE.findall(text))


# --------------------------------------------------------------------------
# Coverage (binding definition: WU-PR-01 instruction v1.0 section 5.1)
# --------------------------------------------------------------------------

def _reached(path: str, roots: Iterable[str]) -> bool:
    return any(path == root or path.startswith(f"{root.rstrip('/')}/") for root in roots)


def compute_coverage(root: Path) -> dict[str, object]:
    """Uncovered tracked test files of the checkout at ``root``, from its own files."""
    listed = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--", "tests"],
                            capture_output=True, check=True).stdout.decode("utf-8").split("\0")
    tracked = sorted(p for p in listed if p and PurePosixPath(p).name.startswith("test_") and p.endswith(".py"))
    text = (root / WORKFLOW_PATH).read_text(encoding="utf-8")
    command_tokens = pytest_command_tokens(text)
    targets = tuple(load_classifier(root)._full_validation_test_targets())
    roots = command_tokens | set(targets)
    return {
        "tracked": len(tracked),
        "pytest_command_tokens": sorted(command_tokens),
        "anywhere_tokens": sorted(anywhere_tokens(text)),
        "full_validation_targets": len(targets),
        "uncovered": [p for p in tracked if not _reached(p, roots)],
    }


def coverage_in_child(copy: Path, env: dict[str, str]) -> dict[str, object]:
    """Compute coverage in a separate process against the copy's own classifier."""
    code = (
        "import importlib.util, json, sys\n"
        "sys.dont_write_bytecode = True\n"
        "spec = importlib.util.spec_from_file_location('_prepush_check_child', sys.argv[1])\n"
        "module = importlib.util.module_from_spec(spec)\n"
        "sys.modules['_prepush_check_child'] = module\n"
        "spec.loader.exec_module(module)\n"
        "from pathlib import Path\n"
        "print(json.dumps(module.compute_coverage(Path(sys.argv[2]))))\n"
    )
    result = subprocess.run([sys.executable, "-B", "-c", code, str(TOOL_PATH), str(copy)],
                            cwd=copy, env=env, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise ToolingError("coverage computation failed: " + result.stderr.strip()[-2000:])
    return json.loads(result.stdout)


# --------------------------------------------------------------------------
# Child environments (closed rails, no keys)
# --------------------------------------------------------------------------

def child_environment(base: dict[str, str], temporary: Path, extra: dict[str, str] | None = None) -> dict[str, str]:
    env = {k: v for k, v in base.items() if k not in REMOVED_ENV_KEYS}
    env.update(CLOSED_RAILS)
    interpreter_dir = str(Path(sys.executable).parent)
    env["PATH"] = interpreter_dir + os.pathsep + base.get("PATH", os.defpath)
    for name in ("tmp", "xdg_state"):
        (temporary / name).mkdir(exist_ok=True)
    env["TMPDIR"] = str(temporary / "tmp")
    env["XDG_STATE_HOME"] = str(temporary / "xdg_state")
    env.pop("GIT_OPTIONAL_LOCKS", None)
    if extra:
        env.update(extra)
    return env


# --------------------------------------------------------------------------
# Report plumbing
# --------------------------------------------------------------------------

@dataclass
class Report:
    name: str
    lines: list[str] = field(default_factory=list)
    status: str = "PASS"

    def out(self, text: str) -> None:
        for line in text.splitlines() or [""]:
            self.lines.append(f"{self.name}: {line}")
            print(f"{self.name}: {line}", flush=True)

    def fail(self, text: str, *, tooling: bool = False) -> None:
        self.status = "FAIL"
        self.out(("TOOLING_FAILURE " if tooling else "FAILURE ") + text)


@dataclass
class Context:
    repo: Path
    temporary: Path
    head_ref: str
    base_ref: str
    event: str
    paths: list[str]
    full: bool
    no_run: bool


def _normalized_paths(context: Context, report: Report) -> list[str] | None:
    classifier = load_classifier(context.repo)
    normalized = []
    for raw in context.paths:
        try:
            normalized.append(classifier._normalized_path(raw))
        except ValueError as exc:
            report.fail(f"invalid path {raw!r}: {exc}")
            return None
    return normalized


# --------------------------------------------------------------------------
# lanes
# --------------------------------------------------------------------------

def report_lanes(context: Context, report: Report) -> None:
    outputs = _lanes_for_given_paths(context, report) if context.paths else _lanes_for_refs(context, report)
    if outputs.get("reason") == "documentation_only":
        report.out("note: reason=documentation_only means the workflow's path filter starts no hosted run")


def _lanes_for_given_paths(context: Context, report: Report) -> dict[str, str]:
    classifier = load_classifier(context.repo)
    report.out(f"mode=paths root={context.repo} paths={len(context.paths)}")
    report.out("note: changed-test targets are computed against the head's files; "
               "a planned file that does not exist yet selects no target of its own")
    try:
        governed = classifier._load_governed_primary_paths(context.repo)
        result = classifier.classify_paths(context.paths, governed_paths=governed)
        targets = result.test_targets or classifier.changed_test_targets(context.repo, context.paths)
        classification = classifier.Classification(
            flags=result.flags, reason=result.reason, path_count=result.path_count, test_targets=targets)
        output = context.temporary / "lanes-paths-github-output.txt"
        target_file = context.temporary / "lanes-paths-changed-tests.txt"
        output.unlink(missing_ok=True)
        classifier.write_github_output(output, classification)
        classifier.write_changed_test_targets(target_file, classification.test_targets)
    except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
        report.fail(f"CI_CHANGE_CLASSIFIER_ERROR:{exc}")
        return {}
    enabled = ",".join(lane for lane in classifier.LANES if classification.flags[lane]) or "none"
    report.out(f"classification reason={classification.reason};paths={classification.path_count};lanes={enabled}")
    return _print_outputs(report, output, target_file)


def _lanes_for_refs(context: Context, report: Report) -> dict[str, str]:
    try:
        head = resolve_commit(context.repo, context.head_ref)
        base = head if context.full else resolve_commit(context.repo, context.base_ref)
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return {}
    report.out(f"mode=refs event={context.event} base={context.base_ref}->{base} head={context.head_ref}->{head}"
               + (" (full validation: base set to head)" if context.full else ""))
    if context.event == "pull_request":
        report.out("note: pull_request compares the merge base of base and head with head (classifier rule)")
    root = context.repo
    if head != repository_state_head(context.repo):
        root = make_copy(context.repo, head, context.temporary / "lanes-copy")
        report.out(f"note: head is not the checkout's HEAD; classified in a throwaway copy at {head}")
    output = context.temporary / "lanes-refs-github-output.txt"
    target_file = context.temporary / "lanes-refs-changed-tests.txt"
    output.unlink(missing_ok=True)
    result = subprocess.run(
        [sys.executable, "-B", str(root / CLASSIFIER_PATH), "--base", base, "--head", head,
         "--event-name", context.event, "--repo-root", str(root),
         "--github-output", str(output), "--changed-tests-output", str(target_file)],
        cwd=root, env=child_environment(dict(os.environ), context.temporary, {"GIT_OPTIONAL_LOCKS": "0"}),
        capture_output=True, text=True, check=False)
    for line in result.stdout.splitlines():
        report.out(line)
    if result.returncode != 0:
        report.fail(f"classifier exit {result.returncode}: {result.stderr.strip()}")
        return {}
    return _print_outputs(report, output, target_file)


def repository_state_head(repo: Path) -> str:
    return git_text(repo, "rev-parse", "--verify", "HEAD")


def _print_outputs(report: Report, output: Path, target_file: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in output.read_text(encoding="utf-8").splitlines():
        report.out(f"output {line}")
        key, _sep, value = line.partition("=")
        values[key] = value
    targets = [t for t in target_file.read_text(encoding="utf-8").splitlines() if t]
    report.out(f"changed_test_targets={len(targets)}")
    for target in targets:
        report.out(f"target {target}")
    return values


# --------------------------------------------------------------------------
# membership and build-notes
# --------------------------------------------------------------------------

def report_membership(context: Context, report: Report) -> None:
    if not context.paths:
        report.fail("membership needs at least one --path")
        return
    paths = _normalized_paths(context, report)
    if paths is None:
        return
    try:
        version, roster = admitted_release(context.repo)
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return
    manifest = context.repo / MANIFEST_PATH
    release_id = hashlib.sha256(manifest.read_bytes()).hexdigest() if manifest.is_file() else "unavailable"
    report.out(f"admitted release version={version} roster={len(roster)} release_id={release_id}")
    members = 0
    for path in paths:
        member = path in roster
        members += member
        report.out(f"{'member' if member else 'not-member'} {path}")
    if members:
        report.out("note: changing a release member requires a same-version release manifest refresh "
                   "with convergence (information only; this tool runs no owner tool)")


def report_build_notes(context: Context, report: Report) -> None:
    listed = git(context.repo, "ls-tree", "-r", "-z", "--name-only", "HEAD", "--",
                 BUILD_NOTES_DIRECTORY).stdout.decode("utf-8").split("\0")
    matches = sorted(p for p in listed if p and fnmatch.fnmatchcase(p, BUILD_NOTES_PATTERN)
                     and "/" not in p[len(BUILD_NOTES_DIRECTORY):])
    if len(matches) != 1:
        report.fail(f"expected exactly one {BUILD_NOTES_PATTERN}, found {len(matches)}: "
                    + (", ".join(matches) or "none"))
        return
    data = (context.repo / matches[0]).read_bytes()
    report.out(f"path={matches[0]} bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()}")


# --------------------------------------------------------------------------
# sweep
# --------------------------------------------------------------------------

def report_sweep(context: Context, report: Report) -> None:
    try:
        head = resolve_commit(context.repo, context.head_ref)
        copy = make_copy(context.repo, head, context.temporary / "sweep-copy")
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return
    env = child_environment(dict(os.environ), context.temporary, {"PYTHONPATH": str(copy)})
    report.out(f"head={context.head_ref}->{head} copy={copy}")
    try:
        coverage = coverage_in_child(copy, env)
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return
    uncovered = list(coverage["uncovered"])
    report.out(f"tracked_test_files={coverage['tracked']} pytest_command_tokens={len(coverage['pytest_command_tokens'])} "
               f"workflow_tests_tokens={len(coverage['anywhere_tokens'])} "
               f"full_validation_targets={coverage['full_validation_targets']} uncovered={len(uncovered)}")
    for path in uncovered:
        report.out(f"uncovered {path}")
    if not uncovered:
        return
    report.fail(f"{len(uncovered)} tracked test file(s) reached by no CI lane and no full-validation target")
    if context.no_run:
        report.out("run: not executed (--no-run)")
        return
    _run_uncovered(copy, uncovered, env, context.temporary, report)


def _run_uncovered(copy: Path, files: list[str], env: dict[str, str], temporary: Path, report: Report) -> None:
    missing = [tool for tool in SWEEP_TOOLS if shutil.which(tool, path=env["PATH"]) is None]
    if missing:
        report.out("TOOLING_FAILURE missing on PATH: " + ", ".join(missing) + " (tests needing them fail as tooling)")
    junit = temporary / "sweep-junit.xml"
    started = time.monotonic()
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--continue-on-collection-errors",
         "-o", "junit_family=xunit1", f"--junitxml={junit}", "--", *files],
        cwd=copy, env=env, capture_output=True, text=True, check=False)
    report.out(f"run: pytest exit {result.returncode} in {time.monotonic() - started:.1f}s")
    outcomes = _junit_outcomes(junit, files) if junit.is_file() else {}
    for path in files:
        report.out(f"file {outcomes.get(path, 'TOOLING (no result recorded)')} {path}")
    clean, status = copy_status(copy)
    report.out("copy after run: " + ("clean" if clean else "CHANGED (the files rewrite tracked or untracked files)"))
    for line in status.splitlines():
        report.out(f"copy-status {line}")


def _junit_outcomes(junit: Path, files: list[str]) -> dict[str, str]:
    counts: dict[str, dict[str, int]] = {path: {"passed": 0, "failed": 0, "error": 0, "skipped": 0} for path in files}
    collection_errors: set[str] = set()
    for case in ET.parse(junit).getroot().iter("testcase"):
        path = case.get("file") or ""
        if path not in counts:
            classname = (case.get("classname") or "").replace(".", "/")
            path = next((p for p in files if p.removesuffix(".py") == classname or classname.startswith(p.removesuffix(".py"))), "")
        if path not in counts:
            continue
        if case.find("failure") is not None:
            counts[path]["failed"] += 1
        elif case.find("error") is not None:
            message = (case.find("error").get("message") or "")
            if "collection failure" in message or not case.get("name"):
                collection_errors.add(path)
            counts[path]["error"] += 1
        elif case.find("skipped") is not None:
            counts[path]["skipped"] += 1
        else:
            counts[path]["passed"] += 1
    outcomes = {}
    for path, c in counts.items():
        summary = f"(passed {c['passed']}, failed {c['failed']}, errors {c['error']}, skipped {c['skipped']})"
        if path in collection_errors:
            outcomes[path] = f"TOOLING collection or import error {summary}"
        elif c["failed"] or c["error"]:
            outcomes[path] = f"BEHAVIOR {summary}"
        elif not any(c.values()):
            outcomes[path] = "TOOLING (no test collected)"
        else:
            outcomes[path] = f"PASS {summary}"
    return outcomes


# --------------------------------------------------------------------------
# replay: expressions
# --------------------------------------------------------------------------

class Expressions:
    """The subset of GitHub Actions expressions ci.yml uses; anything else is tooling."""

    _TOKEN = re.compile(r"\s*(?:(\|\||&&|==|!=|\(|\)|!)|'((?:[^']|'')*)'|([A-Za-z_][A-Za-z0-9_.-]*(?:\(\))?))")

    def __init__(self, contexts: dict[str, object], job_failed: bool) -> None:
        self.contexts = contexts
        self.job_failed = job_failed

    def evaluate(self, text: str) -> object:
        self.tokens = self._tokenize(text)
        self.position = 0
        value = self._or()
        if self.position != len(self.tokens):
            raise ToolingError(f"unsupported expression: {text.strip()}")
        return value

    def _tokenize(self, text: str) -> list[tuple[str, str]]:
        tokens: list[tuple[str, str]] = []
        index = 0
        text = text.strip()
        while index < len(text):
            match = self._TOKEN.match(text, index)
            if not match or match.end() == index:
                raise ToolingError(f"unsupported expression: {text}")
            if match.group(1):
                tokens.append(("op", match.group(1)))
            elif match.group(2) is not None:
                tokens.append(("str", match.group(2).replace("''", "'")))
            else:
                tokens.append(("name", match.group(3)))
            index = match.end()
            while index < len(text) and text[index] == " ":
                index += 1
        return tokens

    def _peek(self) -> tuple[str, str] | None:
        return self.tokens[self.position] if self.position < len(self.tokens) else None

    def _or(self) -> object:
        value = self._and()
        while self._peek() == ("op", "||"):
            self.position += 1
            right = self._and()
            value = value if _truthy(value) else right
        return value

    def _and(self) -> object:
        value = self._compare()
        while self._peek() == ("op", "&&"):
            self.position += 1
            right = self._compare()
            value = right if _truthy(value) else value
        return value

    def _compare(self) -> object:
        left = self._unary()
        token = self._peek()
        if token in {("op", "=="), ("op", "!=")}:
            self.position += 1
            right = self._unary()
            equal = str(_string(left)).lower() == str(_string(right)).lower()
            return equal if token[1] == "==" else not equal
        return left

    def _unary(self) -> object:
        token = self._peek()
        if token == ("op", "!"):
            self.position += 1
            return not _truthy(self._unary())
        if token == ("op", "("):
            self.position += 1
            value = self._or()
            if self._peek() != ("op", ")"):
                raise ToolingError("unbalanced expression")
            self.position += 1
            return value
        if token is None:
            raise ToolingError("empty expression")
        self.position += 1
        kind, text = token
        if kind == "str":
            return text
        if text in {"true", "false"}:
            return text == "true"
        if text.endswith("()"):
            if text == "always()":
                return True
            if text == "success()":
                return not self.job_failed
            if text == "failure()":
                return self.job_failed
            if text == "cancelled()":
                return False
            raise ToolingError(f"unsupported function: {text}")
        return self._lookup(text)

    def _lookup(self, dotted: str) -> object:
        parts = dotted.split(".")
        if parts[0] not in self.contexts:
            raise ToolingError(f"unsupported context: {dotted}")
        value: object = self.contexts
        for part in parts:
            if isinstance(value, dict):
                value = value.get(part, "")
            else:
                return ""
        return value


def _truthy(value: object) -> bool:
    return bool(value) and value != 0


def _string(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return "" if value is None or isinstance(value, dict) else str(value)


def interpolate(text: str, expressions: Expressions) -> str:
    return _EXPRESSION_RE.sub(lambda m: _string(expressions.evaluate(m.group(1))), text)


def condition(text: object, expressions: Expressions) -> bool:
    if text in (None, ""):
        return not expressions.job_failed
    raw = str(text).strip()
    inner = _EXPRESSION_RE.fullmatch(raw)
    expression = inner.group(1) if inner else raw
    value = _truthy(expressions.evaluate(expression))
    if not any(function in expression.replace(" ", "") for function in _STATUS_FUNCTIONS):
        value = value and not expressions.job_failed
    return value


# --------------------------------------------------------------------------
# replay
# --------------------------------------------------------------------------

def replay_steps(text: str) -> tuple[Job, list[dict[str, object]]]:
    jobs = parse_jobs(text)
    if REPLAY_JOB not in jobs:
        raise ToolingError(f"{WORKFLOW_PATH} has no {REPLAY_JOB!r} job")
    job = jobs[REPLAY_JOB]
    unknown_job_keys = set(job.keys) - REPLAY_JOB_KEYS
    if unknown_job_keys:
        raise ToolingError(f"REPLAY_INVENTORY_DRIFT: unsupported job keys {sorted(unknown_job_keys)}")
    names = [str(step.get("name", "")) for step in job.steps]
    expected = [name for name, _kind, _reason in REPLAY_INVENTORY]
    if names != expected:
        raise ToolingError("REPLAY_INVENTORY_DRIFT: the test job's steps differ from the tool's inventory: "
                           f"workflow={names} tool={expected}")
    for step, (name, kind, _reason) in zip(job.steps, REPLAY_INVENTORY):
        unknown = set(step) - REPLAY_STEP_KEYS
        if unknown:
            raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} has unsupported keys {sorted(unknown)}")
        if ("uses" in step) != (kind == REPLAY_EXCLUDED and name != "Install applicable validation dependencies"):
            raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} changed between uses: and run:")
    return job, job.steps


def _python_version(steps: list[dict[str, object]]) -> str:
    for step in steps:
        uses = str(step.get("uses", ""))
        if uses.startswith("actions/setup-python@"):
            with_values = step.get("with", {})
            if isinstance(with_values, dict) and "python-version" in with_values:
                return str(with_values["python-version"])
    raise ToolingError("no actions/setup-python step with python-version")


@dataclass(frozen=True)
class _Version:
    release: tuple[int, ...]
    key: tuple[object, ...]  # PEP 440 order of the public version (local label excluded)
    prerelease: bool
    postrelease: bool
    local: bool


def _parse_version(text: str) -> _Version:
    match = _VERSION_RE.fullmatch(text.strip())
    if not match:
        raise ValueError(f"version {text.strip()!r} is not a PEP 440 version")
    epoch, release_text, pre, pre_n, post_implicit, post_n, dev, dev_n, local = match.groups()
    post = post_implicit if post_implicit is not None else post_n  # "" when "post" has no number
    release = tuple(int(part) for part in release_text.split("."))
    trimmed = release
    while len(trimmed) > 1 and trimmed[-1] == 0:
        trimmed = trimmed[:-1]
    if pre is not None:
        pre_key: tuple[int, int] = (_PRE_RANK[pre.lower()], int(pre_n or 0))
    else:
        pre_key = (-1, 0) if post is None and dev is not None else (3, 0)
    key = (int(epoch or 0), trimmed, pre_key, -1 if post is None else int(post or 0),
           (1, 0) if dev is None else (0, int(dev_n or 0)))
    return _Version(release, key, pre is not None or dev is not None, post is not None, local is not None)


def _canonical(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def _clause(operator: str, text: str) -> bool:
    """Whether ``operator text`` is a PEP 440 clause; raises for one the replay does not verify."""
    if operator not in {"===", "~=", "==", "!=", "<=", ">=", "<", ">"}:
        return False
    if operator == "===":
        return True
    if text.endswith(".*"):
        return operator in {"==", "!="} and bool(_WILDCARD_RE.fullmatch(text))
    try:
        version = _parse_version(text)
    except ValueError:
        return False
    if version.local:
        if operator in {"==", "!="}:
            raise ValueError(f"unsupported local-version clause {operator}{text}")
        return False
    return operator != "~=" or len(version.release) > 1


def _parse_clauses(specifier: str) -> list[tuple[str, str]] | None:
    """The PEP 440 clauses of a specifier ("" has none); None when one of them is not a clause."""
    clauses: list[tuple[str, str]] = []
    for clause in specifier.split(",") if specifier.strip() else ():
        parsed = _CLAUSE_RE.fullmatch(clause.strip())
        if not parsed or not _clause(*parsed.groups()):
            return None
        clauses.append((parsed.group(1), parsed.group(2)))
    return clauses


def _parse_requirement(text: str) -> tuple[str, frozenset[str], list[tuple[str, str]], object]:
    """A requirement's distribution name, extras, version clauses and marker (None when absent)."""
    match = _REQUIREMENT_RE.fullmatch(text.strip())
    specifier = match.group(3).strip() if match else ""
    clauses = _parse_clauses(specifier[1:-1] if specifier.startswith("(") else specifier) if match else None
    if not match or clauses is None:
        raise ValueError(f"unsupported requirement {text.strip()!r}")
    extras = frozenset(_canonical(extra) for extra in (match.group(2) or "").split(",") if extra.strip())
    return match.group(1), extras, clauses, _parse_marker(match.group(4)) if match.group(4) else None


def _parse_marker(text: str) -> object:
    """A PEP 508 marker as nested ("or" | "and", left, right) and ("cmp", left, op, right) tuples."""
    tokens: list[tuple[str, str]] = []
    position = 0
    while position < len(text):
        match = _MARKER_TOKEN_RE.match(text, position)
        if not match:
            raise ValueError(f"unsupported marker {text!r}")
        kind = str(match.lastgroup)
        value = match.group(kind)
        if kind == "var" and value not in _MARKER_VARIABLES:
            raise ValueError(f"unsupported marker variable {value!r} in {text!r}")
        tokens.append(("str" if kind in {"single", "double"} else kind, " ".join(value.split())))
        position = match.end()

    def disjunction(index: int) -> tuple[object, int]:
        node, index = conjunction(index)
        while index < len(tokens) and tokens[index] == ("bool", "or"):
            right, index = conjunction(index + 1)
            node = ("or", node, right)
        return node, index

    def conjunction(index: int) -> tuple[object, int]:
        node, index = atom(index)
        while index < len(tokens) and tokens[index] == ("bool", "and"):
            right, index = atom(index + 1)
            node = ("and", node, right)
        return node, index

    def atom(index: int) -> tuple[object, int]:
        if index < len(tokens) and tokens[index] == ("paren", "("):
            node, index = disjunction(index + 1)
            if index < len(tokens) and tokens[index] == ("paren", ")"):
                return node, index + 1
        elif len(tokens) - index >= 3 and tokens[index + 1][0] == "op" \
                and {tokens[index][0], tokens[index + 2][0]} == {"var", "str"}:
            return ("cmp", tokens[index], tokens[index + 1][1], tokens[index + 2]), index + 3
        raise ValueError(f"unsupported marker {text!r}")

    node, index = disjunction(0)
    if index != len(tokens):
        raise ValueError(f"unsupported marker {text!r}")
    return node


def _marker_environment() -> dict[str, str]:
    """PEP 508 marker values for this interpreter (the one the replay runs)."""
    info = sys.implementation.version
    implementation = f"{info.major}.{info.minor}.{info.micro}"
    if info.releaselevel != "final":
        implementation += info.releaselevel[0] + str(info.serial)
    return {
        "implementation_name": sys.implementation.name,
        "implementation_version": implementation,
        "os_name": os.name,
        "platform_machine": platform.machine(),
        "platform_python_implementation": platform.python_implementation(),
        "platform_release": platform.release(),
        "platform_system": platform.system(),
        "platform_version": platform.version(),
        "python_full_version": platform.python_version(),
        "python_version": ".".join(platform.python_version_tuple()[:2]),
        "sys_platform": sys.platform,
    }


def _marker_true(node: object, environment: dict[str, str]) -> bool:
    kind = node[0]  # type: ignore[index]
    if kind in {"or", "and"}:
        left, right = (_marker_true(part, environment) for part in node[1:])  # type: ignore[index]
        return (left or right) if kind == "or" else (left and right)
    _cmp, (left_kind, left), operator, (_right_kind, right) = node  # type: ignore[misc]
    variable = left if left_kind == "var" else right
    lhs = environment[left] if left_kind == "var" else left
    rhs = right if left_kind == "var" else environment[right]
    if variable == "extra":
        lhs, rhs = _canonical(lhs), _canonical(rhs)
    if variable in _MARKER_VERSION_VARIABLES and operator not in {"in", "not in"}:
        if not _clause(operator, rhs):
            raise ValueError(f"undefined marker comparison {lhs!r} {operator} {rhs!r}")
        try:
            return _satisfies(lhs, operator, rhs)
        except ValueError:
            return False  # a value that is not a version matches no version clause
    if operator not in {"==", "!=", "in", "not in"}:
        raise ValueError(f"undefined marker comparison {lhs!r} {operator} {rhs!r}")
    return {"==": lhs == rhs, "!=": lhs != rhs, "in": lhs in rhs, "not in": lhs not in rhs}[operator]


def _satisfies(installed: str, operator: str, text: str) -> bool:
    """PEP 440 clause matching for an installed version (pre-releases allowed, as pip checks one)."""
    if operator == "===":
        return installed.strip().lower() == text.lower()
    version = _parse_version(installed)
    if text.endswith(".*"):
        spec = _parse_version(text[:-2])
        width = len(spec.release)
        matched = version.key[0] == spec.key[0] and (version.release + (0,) * width)[:width] == spec.release
        return matched if operator == "==" else not matched
    spec = _parse_version(text)
    if operator == "~=":
        prefix = ".".join(str(part) for part in spec.release[:-1]) + ".*"
        return _satisfies(installed, ">=", text) and _satisfies(installed, "==", f"{spec.key[0]}!{prefix}")
    same_release = version.key[:2] == spec.key[:2]
    if operator in {"==", "!="}:
        return (version.key == spec.key) == (operator == "==")
    if operator == ">=":
        return version.key >= spec.key
    if operator == "<=":
        return version.key <= spec.key
    if operator == "<":
        return version.key < spec.key and not (version.prerelease and not spec.prerelease and same_release)
    return version.key > spec.key and not (
        ((version.postrelease and not spec.postrelease) or version.local) and same_release)


def _distribution(name: str, search_path: list[str] | None) -> importlib.metadata.Distribution | None:
    return next(iter(importlib.metadata.distributions(name=name, path=search_path or sys.path)), None)


def _unmet_requirements(roots: list[tuple[str, str]], search_path: list[str] | None) -> list[str]:
    """Requirements in the closure of ``roots`` (requirement, required by) the environment does not satisfy.

    Installed distributions' Requires-Dist entries are followed for the extras
    requested of them, with markers evaluated for this interpreter, as pip
    follows them; a satisfied closure is one CI's install would leave unchanged.
    """
    environment = _marker_environment()
    queue = [(text, required_by, frozenset({""})) for text, required_by in roots]
    visited: dict[str, set[str]] = {}
    unmet: set[str] = set()
    while queue:
        text, required_by, contexts = queue.pop(0)
        name, extras, clauses, marker = _parse_requirement(text)
        if not any(context == "" if marker is None else _marker_true(marker, {**environment, "extra": context})
                   for context in contexts):
            continue
        distribution = _distribution(name, search_path)
        if distribution is None:
            unmet.add(f"{name} (not installed; required by {required_by})")
            continue
        version = distribution.version
        if not all(_satisfies(version, operator, clause) for operator, clause in clauses):
            unmet.add(f"{name} {version} (needs {','.join(o + c for o, c in clauses)}; required by {required_by})")
        new = ({""} | extras) - visited.setdefault(_canonical(name), set())
        if new:
            visited[_canonical(name)] |= new
            queue += [(entry, distribution.metadata["Name"], frozenset(new)) for entry in distribution.requires or ()]
    return sorted(unmet)


def _requirement_lines(path: Path, seen: frozenset[Path] = frozenset()) -> list[str]:
    """A requirements file's requirements; nested -r files are followed, any other option fails closed."""
    if path.resolve() in seen:
        raise ValueError(f"requirements file {path.name} includes itself")
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").replace("\\\n", "").splitlines():
        line = re.sub(r"(^|\s)#.*", "", line).strip()
        nested = re.fullmatch(r"(?:-r|--requirement)(?:\s+|=)(\S+)", line)
        if nested:
            lines += _requirement_lines(path.parent / nested.group(1), seen | {path.resolve()})
        elif line.startswith("-"):
            raise ValueError(f"unsupported requirements-file option {line!r} in {path.name}")
        elif line:
            lines.append(line)
    return lines


def _install_check(run_text: str, copy: Path, search_path: list[str] | None = None) -> list[str]:
    """What the caller's environment lacks for CI's install step to change nothing.

    The step's requirements and their installed dependencies, extras included,
    must be satisfied; the editable project's installed version and entry points
    must equal the candidate's and its requires-python must admit this
    interpreter, so the replay never runs against a dependency set or a wrapper
    CI's install would replace, nor passes a candidate CI cannot install.  Build
    requirements, which pip fetches into an isolated build environment, are
    outside what an offline check can verify.
    """
    words = shlex.split(run_text)
    if "install" not in words or words[:words.index("install")] not in (["pip"], ["python", "-m", "pip"]):
        raise ValueError("the install step is not one 'python -m pip install' command")
    rest = words[words.index("install") + 1:]
    roots: list[tuple[str, str]] = []
    projects: list[dict[str, object]] = []
    index = 0
    while index < len(rest):
        word = rest[index]
        if word in {"-r", "--requirement", "-e", "--editable"} and index + 1 < len(rest):
            target = copy / rest[index + 1]
            if word in {"-r", "--requirement"}:
                roots += [(line, "the install step") for line in _requirement_lines(target)]
            else:
                project = tomllib.loads((target / "pyproject.toml").read_text(encoding="utf-8"))["project"]
                projects.append(project)
                roots.append((str(project["name"]), "the install step"))
                roots += [(str(dependency), str(project["name"])) for dependency in project.get("dependencies", [])]
            index += 2
            continue
        if word.startswith("-"):
            raise ValueError(f"unsupported install option {word!r}")
        roots.append((word, "the install step"))
        index += 1
    unmet = _unmet_requirements(roots, search_path)
    for project in projects:
        name = str(project["name"])
        distribution = _distribution(name, search_path)
        if distribution is None:
            continue  # already reported as not installed
        if "version" not in project:
            raise ValueError(f"the editable project {name!r} declares no static version")
        if _parse_version(distribution.version).key != _parse_version(str(project["version"])).key:
            unmet.append(f"{name} {distribution.version} (the candidate declares version {project['version']})")
        requires_python = str(project.get("requires-python", ""))
        python_clauses = _parse_clauses(requires_python)
        if python_clauses is None:
            raise ValueError(f"unsupported requires-python {requires_python!r} in {name!r}")
        if not all(_satisfies(platform.python_version(), o, c) for o, c in python_clauses):
            unmet.append(f"{name} requires-python {requires_python} (the interpreter is {platform.python_version()})")
        # pip reinstalls the editable project, so every entry-point group is regenerated from the candidate.
        declared: dict[str, dict[str, str]] = {"console_scripts": dict(project.get("scripts", {})),
                                               "gui_scripts": dict(project.get("gui-scripts", {}))}
        declared.update({str(group): dict(entries) for group, entries in dict(project.get("entry-points", {})).items()})
        installed: dict[str, dict[str, str]] = {}
        for entry in distribution.entry_points:
            installed.setdefault(entry.group, {})[entry.name] = entry.value
        for group in sorted(set(declared) | set(installed)):
            have = {key: "".join(str(value).split()) for key, value in installed.get(group, {}).items()}
            want = {key: "".join(str(value).split()) for key, value in declared.get(group, {}).items()}
            if have != want:
                unmet.append(f"{name} {group} {have} (the candidate declares {want})")
    return sorted(set(unmet))


def _resolution(copy: Path, env: dict[str, str], temporary: Path) -> list[tuple[str, str, bool]]:
    """Where each console script's module resolves under the replay environment."""
    pyproject = copy / "pyproject.toml"
    scripts = {}
    if pyproject.is_file():
        scripts = tomllib.loads(pyproject.read_text(encoding="utf-8")).get("project", {}).get("scripts", {})
    rows = []
    for script, target in sorted(scripts.items()):
        module = str(target).split(":", 1)[0]
        result = subprocess.run(
            [sys.executable, "-B", "-c",
             "import importlib.util, sys; s = importlib.util.find_spec(sys.argv[1]); print(s.origin if s else '')",
             module],
            cwd=temporary, env=env, capture_output=True, text=True, check=False)
        origin = result.stdout.strip()
        inside = bool(origin) and Path(origin).resolve().is_relative_to(copy.resolve())
        executable = shutil.which(script, path=env["PATH"]) or "not on PATH"
        rows.append((f"{script} ({executable}) -> {module}", origin or "not importable", inside))
    return rows


def _classify_failure(returncode: int, log: str) -> str:
    if returncode in {126, 127} or "command not found" in log:
        return "TOOLING"
    if any(marker in log for marker in ("errors during collection", "ImportError while importing test module",
                                         "ModuleNotFoundError")):
        return "TOOLING"
    return "BEHAVIOR"


def report_replay(context: Context, report: Report) -> None:
    try:
        head = resolve_commit(context.repo, context.head_ref)
        base = head if context.full else resolve_commit(context.repo, context.base_ref)
        copy = make_copy(context.repo, head, context.temporary / "replay-copy")
        if git(copy, "cat-file", "-e", f"{base}^{{commit}}", check=False).returncode != 0:
            raise ToolingError(f"base {base} is not available to the throwaway copy")
        job, steps = replay_steps((copy / WORKFLOW_PATH).read_text(encoding="utf-8"))
        python_version = _python_version(steps)
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return
    actual = f"{sys.version_info.major}.{sys.version_info.minor}"
    report.out(f"event={context.event} base={base} head={head}" + (" (full validation)" if context.full else ""))
    report.out(f"copy={copy} interpreter={sys.executable} python={sys.version.split()[0]} workflow_python={python_version}")
    runner_temp = context.temporary / "replay-runner-temp"
    runner_temp.mkdir()
    pull_request = context.event == "pull_request"
    contexts: dict[str, object] = {
        "github": {
            "event_name": context.event,
            "sha": head,
            "workflow": "ci",
            "event": {
                "before": "" if pull_request else base,
                "pull_request": {"base": {"sha": base}, "head": {"sha": head}} if pull_request else {},
            },
        },
        "steps": {},
        "env": {},
    }
    expressions = Expressions(contexts, job_failed=False)
    base_env = child_environment(dict(os.environ), context.temporary,
                                 {"PYTHONPATH": str(copy), "RUNNER_TEMP": str(runner_temp),
                                  "CI": "true", "GITHUB_ACTIONS": "true", "GITHUB_EVENT_NAME": context.event})
    try:
        base_env.update({k: interpolate(v, expressions) for k, v in job.env.items()})
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return
    report.out("job env " + " ".join(f"{k}={base_env[k]}" for k in PRINTED_PINS if k in base_env))
    for label, origin, inside in _resolution(copy, base_env, context.temporary):
        report.out(f"resolves {label}: {origin}" + ("" if inside else "  [outside the copy]"))
        if not inside and origin != "not importable":
            report.fail(f"{label} resolves outside the copy; tests would exercise other code", tooling=True)
    steps_context: dict[str, dict[str, object]] = contexts["steps"]  # type: ignore[assignment]
    job_failed = False
    total_started = time.monotonic()
    for number, (step, (name, kind, reason)) in enumerate(zip(steps, REPLAY_INVENTORY), start=1):
        step_id = str(step.get("id", ""))
        expressions.job_failed = job_failed
        try:
            applicable = condition(step.get("if"), expressions)
        except ToolingError as exc:
            report.fail(f"step {number} {name}: {exc}", tooling=True)
            return
        started = time.monotonic()
        outputs: dict[str, str] = {}
        detail = ""
        if not applicable:
            outcome = "skipped"
        elif kind == REPLAY_EXCLUDED:
            outcome, detail = _substitute(step, reason, copy, python_version, actual)
        else:
            outcome, detail, outputs = _execute(step, number, copy, base_env, expressions, context.temporary)
        if step_id:
            steps_context[step_id] = {"outcome": outcome, "conclusion": outcome, "outputs": outputs}
        label = "excluded, substituted" if kind == REPLAY_EXCLUDED and applicable else kind
        report.out(f"step {number:02d} {outcome.upper()} [{label}] {time.monotonic() - started:.1f}s {name}")
        for line in detail.splitlines():
            report.out(f"  {line}")
        if outcome == "failure":
            job_failed = True
            report.status = "FAIL"
    clean, status = copy_status(copy)
    report.out(f"replay step time {time.monotonic() - total_started:.1f}s; copy after replay: "
               + ("clean" if clean else "CHANGED"))
    for line in status.splitlines():
        report.out(f"copy-status {line}")


def _substitute(step: dict[str, object], reason: str, copy: Path,
                python_version: str, actual: str) -> tuple[str, str]:
    uses = str(step.get("uses", ""))
    if uses.startswith("actions/checkout@"):
        return "success", f"{reason}; copy at {git_text(copy, 'rev-parse', 'HEAD')}"
    if uses.startswith("actions/setup-python@"):
        if actual != python_version:
            return "failure", f"TOOLING interpreter {actual} is not the workflow's python-version {python_version}"
        return "success", f"{reason}: {actual}"
    run = str(step.get("run", ""))
    try:
        unmet = _install_check(run, copy)
    except (OSError, KeyError, ValueError, tomllib.TOMLDecodeError) as exc:
        return "failure", f"TOOLING cannot read the install step's inputs: {exc}"
    if unmet:
        return "failure", "TOOLING the caller's environment does not satisfy the install step: " + ", ".join(unmet)
    return "success", (f"{reason}: the environment already satisfies every requirement the step names, their "
                       "dependencies and extras, and the editable project's version and entry points")


def _execute(step: dict[str, object], number: int, copy: Path, base_env: dict[str, str],
             expressions: Expressions, temporary: Path) -> tuple[str, str, dict[str, str]]:
    try:
        script = interpolate(str(step.get("run", "")), expressions)
        env = dict(base_env)
        step_env = step.get("env", {})
        if isinstance(step_env, dict):
            env.update({k: interpolate(str(v), expressions) for k, v in step_env.items()})
    except ToolingError as exc:
        return "failure", f"TOOLING {exc}", {}
    output_file = temporary / f"replay-step-{number:02d}-output.txt"
    output_file.write_text("", encoding="utf-8")
    env["GITHUB_OUTPUT"] = str(output_file)
    script_file = temporary / f"replay-step-{number:02d}.sh"
    script_file.write_text(script, encoding="utf-8")
    shell = step.get("shell")
    if shell == "bash":
        command = ["bash", "--noprofile", "--norc", "-eo", "pipefail", str(script_file)]
    elif shell is None:
        command = ["bash", "-e", str(script_file)]
    else:
        return "failure", f"TOOLING unsupported shell {shell!r}", {}
    result = subprocess.run(command, cwd=copy, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, errors="replace", check=False)
    outputs = {}
    for line in output_file.read_text(encoding="utf-8").splitlines():
        key, sep, value = line.partition("=")
        if sep:
            outputs[key] = value
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    if result.returncode == 0:
        return "success", "\n".join(lines[-3:]), outputs
    kind = _classify_failure(result.returncode, result.stdout)
    return "failure", f"{kind} exit {result.returncode}\n" + "\n".join(lines[-30:]), outputs


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

RUNNERS = {
    "lanes": report_lanes,
    "membership": report_membership,
    "build-notes": report_build_notes,
    "sweep": report_sweep,
    "replay": report_replay,
}


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python tools/ci/prepush_check.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("reports", nargs="+", choices=(*REPORTS, "all"),
                        help="reports to run, always in the order lanes, membership, build-notes, sweep, replay")
    parser.add_argument("--base", default=DEFAULT_BASE, help="base ref for lanes and replay (local; default origin/main)")
    parser.add_argument("--head", default=DEFAULT_HEAD, help="head ref for lanes, sweep and replay (default HEAD)")
    parser.add_argument("--event", choices=("pull_request", "push"), default="pull_request",
                        help="CI event the classification and replay assume (default pull_request)")
    parser.add_argument("--path", dest="paths", action="append", default=[],
                        help="repository-relative path for lanes (given-paths mode) and membership; repeatable")
    parser.add_argument("--full", action="store_true",
                        help="lanes and replay with base equal to head: the classifier's full validation")
    parser.add_argument("--no-run", action="store_true", help="sweep: list the uncovered set without running it")
    parser.add_argument("--repo-root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    requested = REPORTS if "all" in args.reports else tuple(r for r in REPORTS if r in args.reports)
    repo = args.repo_root.resolve()
    try:
        top = git_text(repo, "rev-parse", "--show-toplevel")
    except ToolingError:
        print(f"PREPUSH_CHECK_REFUSED: {repo} is not a git working tree", file=sys.stderr)
        return EXIT_REFUSED
    if Path(top).resolve() != repo:
        print(f"PREPUSH_CHECK_REFUSED: {repo} is not the working tree's top level", file=sys.stderr)
        return EXIT_REFUSED
    before = repository_state(repo)
    if before.status:
        print("PREPUSH_CHECK_REFUSED: the working tree is not clean (untracked files included); "
              "commit or stash before running", file=sys.stderr)
        return EXIT_REFUSED
    temporary = Path(tempfile.mkdtemp(prefix="prepush-check-")).resolve()
    if temporary.is_relative_to(repo):
        shutil.rmtree(temporary, ignore_errors=True)
        print("PREPUSH_CHECK_REFUSED: the temporary directory would be inside the repository", file=sys.stderr)
        return EXIT_REFUSED
    print(f"PREPUSH_CHECK: repo={repo} head={before.head} python={sys.version.split()[0]} "
          f"reports={','.join(requested)}", flush=True)
    results: list[tuple[str, str, float]] = []
    context = Context(repo=repo, temporary=temporary, head_ref=args.head, base_ref=args.base,
                      event=args.event, paths=list(args.paths), full=args.full, no_run=args.no_run)
    try:
        for name in requested:
            report = Report(name)
            started = time.monotonic()
            try:
                RUNNERS[name](context, report)
            except ToolingError as exc:
                report.fail(str(exc), tooling=True)
            except (OSError, UnicodeError, ValueError, KeyError, subprocess.SubprocessError) as exc:
                # Keep the post-run read-only check reachable whatever a report raised.
                report.fail(f"{type(exc).__name__}: {exc}", tooling=True)
            duration = time.monotonic() - started
            report.out(f"status={report.status} duration={duration:.1f}s")
            results.append((name, report.status, duration))
    finally:
        shutil.rmtree(temporary, ignore_errors=True)
    after = repository_state(repo)
    if after != before:
        print("PREPUSH_CHECK_READ_ONLY_VIOLATION: the repository's tree, HEAD or git metadata changed",
              file=sys.stderr)
        return EXIT_READ_ONLY_VIOLATION
    overall = "PASS" if all(status == "PASS" for _n, status, _d in results) else "FAIL"
    print("PREPUSH_CHECK_RESULT: " + overall + " "
          + " ".join(f"{name}={status}" for name, status, _d in results)
          + "; repository unchanged (tree, HEAD and git metadata)", flush=True)
    print("PREPUSH_CHECK_NONCLAIM: this result is not CI's result, not QA and not governed evidence", flush=True)
    return EXIT_OK if overall == "PASS" else EXIT_REPORT_FAILED


if __name__ == "__main__":
    raise SystemExit(main())
