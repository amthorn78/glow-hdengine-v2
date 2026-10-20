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

Children inherit only HOME, LOGNAME, PATH, SHELL, TERM and USER from the
caller's environment, so no other variable of the caller's, secrets included,
reaches them.  They are not sandboxed: ``sweep`` and ``replay`` execute the
candidate's own tests and workflow steps with the caller's file-system and
network access, and SAFE_MODE and ALLOW_NETWORK are application flags, not
isolation.  Run them only on code you trust.
"""
from __future__ import annotations

import sys

# Importing repository modules must not write __pycache__ into the checkout.
sys.dont_write_bytecode = True

import argparse  # noqa: E402
import ast  # noqa: E402
import fnmatch  # noqa: E402
import hashlib  # noqa: E402
import importlib.machinery  # noqa: E402
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

# The only caller variables a child inherits, as a hosted runner also provides
# them; the tool sets the rest (closed rails, temporary directories, the
# report's own values), so no other variable of the caller's reaches a child.
CHILD_INHERITED_KEYS = ("HOME", "LOGNAME", "PATH", "SHELL", "TERM", "USER")
# Never passed to a child (vendor, database and GitHub keys), and absent on a
# hosted runner unless a step sets them.
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
# GitHub rejects a job whose step ids repeat.  An id outside the form it
# documents for job ids, one beginning with "__", and two ids that differ only
# in case are forms the replay does not model either.
_STEP_ID_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_-]*")
# The keys each excluded step may carry: its substitute models exactly these.
# The checkout has no `if`, because the copy exists before step 1 whatever a
# condition says; no excluded step has `env` or `shell`.
REPLAY_EXCLUDED_STEP_KEYS = {
    "Check out exact candidate head": frozenset({"name", "id", "uses", "with"}),
    "Set up Python 3.12": frozenset({"name", "id", "if", "uses", "with"}),
    "Install applicable validation dependencies": frozenset({"name", "id", "if", "run"}),
}
# The condition each excluded step must carry, exactly ("" for none).  The
# caller's environment holds what the substituted steps provide whether or not
# they run, so a substitute stands in for its step only when it runs exactly
# when CI's does.
REPLAY_EXCLUDED_STEP_CONDITIONS = {
    "Check out exact candidate head": "",
    "Set up Python 3.12": "${{ steps.classify.outputs.needs_python == 'true' }}",
    "Install applicable validation dependencies": "${{ steps.classify.outputs.needs_python == 'true' }}",
}
REPLAY_JOB_KEYS = frozenset({"runs-on", "env", "steps"})
# What the replay stands in for, and the only inputs it models: the workflow's
# keys other than jobs, exactly as ci.yml sets them (GitHub validates them
# before the job runs; the replay does not, so a key, value or scalar type
# other than these is drift), the ubuntu-latest runner (x86_64 Linux, replayed
# on this machine, which must be x86_64 Linux too), and the
# two substituted actions, revision included, with their inputs (None: any
# value; a string: exactly that value, required).  Anything else is inventory
# drift.
_REPLAY_PATHS = ["**", "!docs/crd/**", "!docs/ephemeral/**", "!docs/graph/**", "!docs/pfcanon/**", "!docs/plans/**",
                 "!docs/prompt_ecosystem_management/**", "!docs/qa/**", "!docs/run/**", "**.path_proof.txt",
                 "docs/run/EPIC011_TEST_IDENTITIES.md", "docs/run/PROD_ENDPOINTS.json"]
REPLAY_WORKFLOW_HEADER: dict[str, object] = {
    "name": "ci",
    "on": {"pull_request": {"paths": _REPLAY_PATHS}, "push": {"branches": ["main"], "paths": _REPLAY_PATHS}},
    "permissions": {"contents": "read"},
    "concurrency": {"group": "ci-${{ github.workflow }}-${{ github.event.pull_request.number || github.run_id }}",
                    "cancel-in-progress": "${{ github.event_name == 'pull_request' }}"},
}
REPLAY_RUNNER = "ubuntu-latest"
REPLAY_MACHINES = frozenset({"x86_64", "amd64"})
REPLAY_SUBSTITUTED_INPUTS: dict[str, dict[str, str | None]] = {
    "actions/checkout@v4": {"fetch-depth": "0", "persist-credentials": "false",
                            "ref": "${{ github.event.pull_request.head.sha || github.sha }}"},
    "actions/setup-python@v5": {"python-version": None},
}
# The github context paths the replay models; any other path, and github.sha
# and github.event.before on a pull_request event (the merge commit and the
# payload's before are unknown offline), is refused where its value is used.
REPLAY_GITHUB_PATHS = frozenset({"github.event_name", "github.sha", "github.event.before",
                                 "github.event.pull_request.base.sha", "github.event.pull_request.head.sha"})
# Variables the runner or a substituted action gives run steps.  The replay
# sets REPLAY_RUNNER_VARIABLES, leaves REMOVED_ENV_KEYS absent as a hosted
# runner does (children inherit no other runner variable; CHILD_INHERITED_KEYS),
# and refuses a workflow whose run text or env keys name any other.  Scripts a
# step calls are not scanned; they see the same environment.
REPLAY_RUNNER_VARIABLES = frozenset({"GITHUB_ACTIONS", "GITHUB_EVENT_NAME", "GITHUB_OUTPUT", "RUNNER_TEMP"})
_RUNNER_VARIABLE_RE = re.compile(
    r"(?<![A-Za-z0-9_])(?:(?:GITHUB|RUNNER|ACTIONS)_[A-Za-z0-9_]+|ImageOS|ImageVersion|pythonLocation"
    r"|Python[23]?_ROOT_DIR)(?![A-Za-z0-9_])")
# The one build system the install step's substitute models: pip builds the
# editable project with this backend, whose PEP 660 hooks every setuptools
# from 64 provides, from these requirements in an isolated environment.  Any
# other [build-system] fails closed.
REPLAY_BUILD_SYSTEM: dict[str, object] = {"build-backend": "setuptools.build_meta",
                                          "requires": ["setuptools>=68", "wheel"]}
# The rest of the editable project's configuration the substitute models.
# setuptools validates all of it when CI's install builds the project, so a
# table, [project] key or value outside this model fails closed, as do a
# setup.py, a setup.cfg and a [tool.setuptools] or [tool.distutils] other than
# these.
REPLAY_PYPROJECT_TABLES = frozenset({"build-system", "project", "tool"})
REPLAY_PROJECT_KEYS = frozenset({"name", "version", "description", "readme", "requires-python", "dependencies",
                                 "scripts", "gui-scripts", "entry-points"})
REPLAY_SETUPTOOLS_CONFIG: dict[str, object] = {
    "packages": {"find": {"where": ["."], "include": ["engine*", "adapter*", "presenter*", "catalog*", "math*"]}},
    "package-data": {"catalog": ["*.json"], "math": ["*.json"]},
}
# The files of the editable project's installed .dist-info that pip and the
# wheel writer add and the modelled configuration does not decide.  Every
# other file there is metadata the build backend generates from the candidate,
# which CI's install regenerates.
REPLAY_INSTALLER_FILES = frozenset({"INSTALLER", "RECORD", "REQUESTED", "WHEEL", "direct_url.json"})
_PREPARE_METADATA = ("import importlib, sys; sys.path[:0] = sys.argv[3:]; "
                     "importlib.import_module(sys.argv[1]).prepare_metadata_for_build_editable(sys.argv[2])")
_PROJECT_NAME_RE = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?")
_OBJECT_REFERENCE_RE = re.compile(r"[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*(?:\s*:\s*[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)?")

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


class AmbiguousClause(ValueError):
    """A version clause whose result differs between the pip releases CI may run."""


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
    """Digest of git metadata: file bytes, plus names and sizes under objects/, and every directory's name.

    An empty directory holds no file, so without its name its creation or
    removal would go unseen.
    """
    digest = hashlib.sha256()
    for path in sorted(directory.rglob("*")):
        rel = path.relative_to(directory).as_posix()
        if path.is_dir() and not path.is_symlink():
            digest.update(f"{rel}/\0".encode())
            continue
        if not (path.is_file() or path.is_symlink()):
            continue
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


def _ignored_entries(repo: Path) -> tuple[tuple[str, int, int, int, int], ...]:
    """Every ignored working-tree file with its lstat identity.

    git status lists no ignored file, so creating, deleting or rewriting one
    would otherwise go unseen.  Any write to a file changes its st_ctime_ns,
    which user space cannot set back, so the identity needs no content read.
    """
    listing = git(repo, "ls-files", "-z", "--others", "--ignored", "--exclude-standard").stdout
    entries = []
    for raw in sorted(name for name in listing.split(b"\0") if name):
        name = os.fsdecode(raw)
        try:
            info = os.lstat(repo / name)
        except FileNotFoundError:
            entries.append((name, -1, -1, -1, -1))
            continue
        entries.append((name, info.st_mode, info.st_size, info.st_mtime_ns, info.st_ctime_ns))
    return tuple(entries)


def _directory_entries(repo: Path) -> tuple[tuple[str, int, int, int], ...]:
    """Every working-tree directory outside .git with its lstat identity.

    Neither git status nor the ignored-file listing names a directory, so an
    empty one, ignored or not, could otherwise be created or removed unseen;
    adding or removing any entry changes its parent's mtime and ctime.
    """
    entries = []
    for directory, dirnames, _files in os.walk(repo):
        dirnames[:] = sorted(d for d in dirnames if not (directory == str(repo) and d == ".git"))
        info = os.lstat(directory)
        entries.append((os.path.relpath(directory, repo), info.st_mode, info.st_mtime_ns, info.st_ctime_ns))
    return tuple(entries)


@dataclass(frozen=True)
class RepositoryState:
    head: str
    status: bytes
    ignored: tuple[tuple[str, int, int, int, int], ...]
    directories: tuple[tuple[str, int, int, int], ...]
    metadata: tuple[tuple[str, str], ...]


def repository_state(repo: Path) -> RepositoryState:
    head = git_text(repo, "rev-parse", "--verify", "HEAD")
    status = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all").stdout
    directories = {
        Path(git_text(repo, "rev-parse", "--absolute-git-dir")),
        (repo / git_text(repo, "rev-parse", "--git-common-dir")).resolve(),
    }
    metadata = tuple(sorted((str(d), _metadata_digest(d)) for d in directories))
    return RepositoryState(head=head, status=status, ignored=_ignored_entries(repo),
                           directories=_directory_entries(repo), metadata=metadata)


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


def _spaces_only(line: str, index: int) -> None:
    """YAML forbids tabs in indentation, so a tab in a line's leading whitespace fails closed."""
    if "\t" in line[:len(line) - len(line.lstrip(" \t"))]:
        raise ToolingError(f"a tab in the indentation of line {index + 1}, which YAML forbids")


class _Resolved(str):
    """A plain scalar that YAML 1.2's core schema reads as a null, boolean, integer or float, not a string."""

    kind = ""


# GitHub reads the workflow as YAML 1.2 (its `on:` key would be a boolean under 1.1).
_CORE_SCHEMA = (
    ("null", re.compile(r"~|null|Null|NULL")),
    ("boolean", re.compile(r"true|True|TRUE|false|False|FALSE")),
    ("integer", re.compile(r"[-+]?[0-9]+|0o[0-7]+|0x[0-9a-fA-F]+")),
    ("float", re.compile(r"[-+]?(?:\.[0-9]+|[0-9]+(?:\.[0-9]*)?)(?:[eE][-+]?[0-9]+)?|[-+]?\.(?:inf|Inf|INF)"
                         r"|\.(?:nan|NaN|NAN)")),
)


def _resolve(value: str) -> str:
    for kind, pattern in _CORE_SCHEMA:
        if pattern.fullmatch(value):
            scalar = _Resolved(value)
            scalar.kind = kind
            return scalar
    return value


def _as_string(value: object) -> bool:
    """Whether GitHub reads an env or with value as the very string the replay uses.

    A string is; GitHub writes a boolean as true or false and an integer in
    decimal, so only those spellings of them are; any other non-string is not.
    """
    if not isinstance(value, _Resolved):
        return isinstance(value, str)
    return (value.kind == "boolean" and value in {"true", "false"}) \
        or (value.kind == "integer" and re.fullmatch(r"0|-?[1-9][0-9]*", value) is not None)


_SINGLE_QUOTED_RE = re.compile(r"'((?:[^']|'')*)'(?:\s+#.*)?")
_DOUBLE_QUOTED_RE = re.compile(r'"([^"\\]*)"(?:\s+#.*)?')
_KEY_RE = re.compile(r"[A-Za-z0-9_.-]+")


def _plain(value: str) -> str:
    """A one-line scalar of the subset: plain, single-quoted, or double-quoted without escapes."""
    value = value.strip()
    if value[:1] == "'":
        match = _SINGLE_QUOTED_RE.fullmatch(value)
        if not match:
            raise ToolingError(f"unsupported YAML value {value!r} (a single-quoted scalar must close on its line)")
        return match.group(1).replace("''", "'")
    if value[:1] == '"':
        match = _DOUBLE_QUOTED_RE.fullmatch(value)
        if not match:
            raise ToolingError(f"unsupported YAML value {value!r} (a double-quoted scalar must close on its line, "
                               "and its escape sequences are not modelled)")
        return match.group(1)
    value = re.split(r"\s#", value, maxsplit=1)[0].rstrip()
    # A plain scalar cannot begin with an indicator, except "-", "?" or ":"
    # followed by a non-space (YAML 1.2.2 §7.3.3).  A flow collection, anchor,
    # alias, tag, block-scalar option, comment, sequence entry or other
    # indicator, or a mapping value inside the scalar, would be read as a
    # literal string here; GitHub's parser reads it as YAML or rejects it, so
    # it fails closed.
    if value[:1] in set(",[]{}#&*!|>%@`") or (value[:1] in set("-?:") and value[1:2] in {"", " ", "\t"}) \
            or re.search(r":[ \t]", value) or value.endswith(":"):
        raise ToolingError(f"unsupported YAML value {value!r} (flow indicators, anchors, aliases, tags, "
                           "block-scalar options, sequence entries and nested mapping values are not modelled)")
    return _resolve(value)


def _block(lines: list[str], start: int, parent_indent: int, style: str) -> tuple[str, int]:
    body: list[str] = []
    index = start
    block_indent = None
    while index < len(lines):
        line = lines[index]
        if line.strip() and _indent(line) <= parent_indent:
            break
        # A tab after the block's indentation is content; a line of whitespace with a tab ends the block in YAML.
        if not line.strip() and "\t" in line:
            raise ToolingError(f"block scalar line {index + 1} is whitespace with a tab, which is not modelled")
        if line.strip() and block_indent is None:
            block_indent = _indent(line)
        if line.strip() and block_indent is not None and _indent(line) < block_indent:
            raise ToolingError(f"block scalar line {index + 1} is less indented than the block's first line")
        content = line[block_indent:] if block_indent is not None and line.strip() else ""
        # YAML keeps the line breaks around a more-indented line of a folded
        # block; that rule is not modelled, so such a line fails closed.
        if style.startswith(">") and content[:1] in {" ", "\t"}:
            raise ToolingError(f"folded block scalar line {index + 1} is more indented, which is not modelled")
        body.append(content)
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
        _spaces_only(line, index)
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
        # Keys are plain words followed by ': ' or a line end; GitHub rejects a repeated key.
        if not _KEY_RE.fullmatch(key) or isinstance(_resolve(key), _Resolved) or rest[:1] not in {"", " ", "\t"}:
            raise ToolingError(f"unsupported workflow key at line {index + 1}: {line.strip()!r}")
        if key in result:
            raise ToolingError(f"workflow key {key!r} repeated at line {index + 1}")
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
    item_indent = None
    while index < len(lines):
        line = lines[index]
        _spaces_only(line, index)
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        indent = _indent(line)
        if indent <= parent_indent or not line.lstrip().startswith("- "):
            break
        # YAML rejects a block sequence whose entries are not all at one indentation.
        if item_indent is None:
            item_indent = indent
        if indent != item_indent:
            raise ToolingError(f"sequence entry at line {index + 1} is indented differently from its sequence's "
                               "first entry")
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


def parse_workflow(text: str) -> dict[str, object]:
    """The whole workflow document as one mapping, so a repeated key fails closed at every level."""
    document, _ = _mapping(text.splitlines(), 0, -1)
    return document


def parse_jobs(text: str) -> dict[str, Job]:
    mapping = parse_workflow(text).get("jobs")
    if not isinstance(mapping, dict):
        raise ToolingError(f"{WORKFLOW_PATH} has no jobs mapping")
    jobs: dict[str, Job] = {}
    for name, body in mapping.items():
        if not isinstance(body, dict):
            raise ToolingError(f"job {name!r} is not a mapping")
        steps = body.get("steps", [])
        env = body.get("env", {})
        if not isinstance(steps, list) or not isinstance(env, dict) or not all(isinstance(s, dict) for s in steps) \
                or not all(_as_string(v) for v in env.values()):
            raise ToolingError(f"job {name!r} has an unsupported shape")
        jobs[name] = Job(keys=body, env={k: str(v) for k, v in env.items()}, steps=steps)
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
    env = {k: base[k] for k in CHILD_INHERITED_KEYS if k in base}
    env.update(CLOSED_RAILS)
    interpreter_dir = str(Path(sys.executable).parent)
    env["PATH"] = interpreter_dir + os.pathsep + base.get("PATH", os.defpath)
    for name in ("tmp", "xdg_state"):
        (temporary / name).mkdir(exist_ok=True)
    env["TMPDIR"] = str(temporary / "tmp")
    env["XDG_STATE_HOME"] = str(temporary / "xdg_state")
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


def parse_github_output(data: bytes) -> tuple[dict[str, str], tuple[str, str] | None]:
    """A GITHUB_OUTPUT file's outputs as the Linux runner reads them, and the first record the replay cannot take.

    The runner splits the file at line feeds, skips empty lines and reads
    NAME=VALUE at the first '='.  It rejects a line with neither '=' nor '<<'
    and fails the step, keeping the outputs set before it: a BEHAVIOR problem.
    The heredoc form NAME<<DELIMITER, an empty name, a carriage return and text
    that is not UTF-8 are not modelled: a TOOLING problem.
    """
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return {}, ("TOOLING", "GITHUB_OUTPUT is not UTF-8, which the replay does not model")
    outputs: dict[str, str] = {}
    for line in text.split("\n"):
        if not line:
            continue
        equals, heredoc = line.find("="), line.find("<<")
        if "\r" in line or equals == 0 or (heredoc >= 0 and (equals < 0 or heredoc < equals)):
            return outputs, ("TOOLING", f"GITHUB_OUTPUT record {line[:80]!r} is a form the replay does not model")
        if equals < 0:
            return outputs, ("BEHAVIOR", f"the runner rejects GITHUB_OUTPUT record {line[:80]!r}, "
                                         "which is neither NAME=VALUE nor NAME<<DELIMITER")
        outputs[line[:equals]] = line[equals + 1:]
    return outputs, None


def _print_outputs(report: Report, output: Path, target_file: Path) -> dict[str, str]:
    values, problem = parse_github_output(output.read_bytes())
    for line in output.read_text(encoding="utf-8", errors="replace").split("\n"):
        if line:
            report.out(f"output {line}")
    if problem:
        report.fail(f"classifier output: {problem[1]}", tooling=problem[0] == "TOOLING")
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
    # The sweep environment must provide these (PF10 addendum 2.2) whether or not a file is uncovered.
    missing = [tool for tool in SWEEP_TOOLS if shutil.which(tool, path=env["PATH"]) is None]
    if missing:
        report.fail("missing on PATH: " + ", ".join(missing) + " (the sweep environment must provide them)",
                    tooling=True)
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
            equal = _equal(left, right)
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
        if parts[0] == "github" and dotted not in REPLAY_GITHUB_PATHS:
            return _Unmodelled(dotted)
        value: object = self.contexts
        for part in parts:
            if isinstance(value, dict):
                value = value.get(part, "")
            else:
                return ""
        # GitHub compares objects by reference and treats every object as true; the replay models string values only.
        if isinstance(value, dict):
            return _Unmodelled(dotted, "is an object, which the replay does not model")
        return value


@dataclass(frozen=True)
class _Unmodelled:
    """A context value the replay does not model; using it, not discarding it, is tooling."""

    path: str
    reason: str = "is not modelled for this event"

    def refuse(self) -> ToolingError:
        return ToolingError(f"unsupported context: {self.path} {self.reason}")


def _truthy(value: object) -> bool:
    if isinstance(value, _Unmodelled):
        raise value.refuse()
    return bool(value) and value != 0


def _string(value: object) -> str:
    if isinstance(value, _Unmodelled):
        raise value.refuse()
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _equal(left: object, right: object) -> bool:
    """GitHub's == where it needs no conversion: two booleans, or two strings compared ignoring case.

    GitHub converts operands of different types to numbers, and folds the case of
    non-ASCII letters by its own rules; the replay models neither, so such a
    comparison is tooling."""
    for value in (left, right):
        if isinstance(value, _Unmodelled):
            raise value.refuse()
    if isinstance(left, bool) and isinstance(right, bool):
        return left == right
    if isinstance(left, str) and isinstance(right, str):
        if left == right or (left.isascii() and right.isascii()):
            return left.lower() == right.lower()
        raise ToolingError("unsupported comparison: GitHub ignores the case of non-ASCII letters by rules the "
                           "replay does not model")
    raise ToolingError("unsupported comparison: GitHub converts a boolean and a string to numbers to compare them, "
                       "which the replay does not model")


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

def _identical(left: object, right: object) -> bool:
    """Equal as parsed YAML, scalar types included: a plain scalar YAML reads as a non-string is not a string."""
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(_identical(left[key], right[key]) for key in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(map(_identical, left, right))
    return left == right


def replay_steps(text: str) -> tuple[Job, list[dict[str, object]]]:
    header = {key: value for key, value in parse_workflow(text).items() if key != "jobs"}
    differ = sorted(key for key in header.keys() | REPLAY_WORKFLOW_HEADER.keys()
                    if not _identical(header.get(key), REPLAY_WORKFLOW_HEADER.get(key)))
    if differ:
        raise ToolingError(f"REPLAY_INVENTORY_DRIFT: workflow keys other than jobs differ from the tool's model: "
                           + ", ".join(differ))
    jobs = parse_jobs(text)
    if REPLAY_JOB not in jobs:
        raise ToolingError(f"{WORKFLOW_PATH} has no {REPLAY_JOB!r} job")
    if set(jobs) != {REPLAY_JOB}:
        raise ToolingError(f"REPLAY_INVENTORY_DRIFT: the workflow's jobs {sorted(jobs)} are not exactly [{REPLAY_JOB!r}]")
    job = jobs[REPLAY_JOB]
    unknown_job_keys = set(job.keys) - REPLAY_JOB_KEYS
    if unknown_job_keys:
        raise ToolingError(f"REPLAY_INVENTORY_DRIFT: unsupported job keys {sorted(unknown_job_keys)}")
    runs_on = job.keys.get("runs-on", "")
    if runs_on != REPLAY_RUNNER:
        raise ToolingError(f"REPLAY_INVENTORY_DRIFT: runs-on {runs_on!r} is not the modelled {REPLAY_RUNNER!r}")
    names = [str(step.get("name", "")) for step in job.steps]
    expected = [name for name, _kind, _reason in REPLAY_INVENTORY]
    if names != expected:
        raise ToolingError("REPLAY_INVENTORY_DRIFT: the test job's steps differ from the tool's inventory: "
                           f"workflow={names} tool={expected}")
    modelled_variables = REPLAY_RUNNER_VARIABLES | set(REMOVED_ENV_KEYS)
    job_variables = {key for key in job.env if _RUNNER_VARIABLE_RE.fullmatch(key)}
    if job_variables:
        raise ToolingError(f"REPLAY_INVENTORY_DRIFT: the test job's env sets runner variables {sorted(job_variables)}")
    step_ids: set[str] = set()
    for step, (name, kind, _reason) in zip(job.steps, REPLAY_INVENTORY):
        unknown = set(step) - REPLAY_STEP_KEYS
        if unknown:
            raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} has unsupported keys {sorted(unknown)}")
        if ("uses" in step) != (kind == REPLAY_EXCLUDED and name != "Install applicable validation dependencies"):
            raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} changed between uses: and run:")
        if "uses" not in step and not (isinstance(step.get("run"), str) and step["run"].strip()):
            raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} has neither uses: nor a run: command")
        if kind == REPLAY_EXCLUDED and set(step) - REPLAY_EXCLUDED_STEP_KEYS[name]:
            raise ToolingError(f"REPLAY_INVENTORY_DRIFT: excluded step {name!r} has keys its substitute does not model "
                               f"{sorted(set(step) - REPLAY_EXCLUDED_STEP_KEYS[name])}")
        for key in ("name", "id", "if", "uses", "shell", "run"):
            if key in step and (not isinstance(step[key], str) or isinstance(step[key], _Resolved)):
                raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} has a {key} that is not a string")
        for key in ("env", "with"):
            if key in step and not (isinstance(step[key], dict) and all(_as_string(v) for v in step[key].values())):
                raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} has a {key} that is not a mapping of strings")
        if "id" in step:
            step_id = str(step["id"])
            if not _STEP_ID_RE.fullmatch(step_id) or step_id.startswith("__"):
                raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} has the id {step_id!r}, a form the replay "
                                   "does not model")
            if step_id.lower() in step_ids:
                raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} repeats the id {step_id!r}; GitHub requires "
                                   "step ids to be unique")
            step_ids.add(step_id.lower())
        if kind == REPLAY_EXCLUDED and str(step.get("if", "")).strip() != REPLAY_EXCLUDED_STEP_CONDITIONS[name]:
            raise ToolingError(f"REPLAY_INVENTORY_DRIFT: excluded step {name!r} has the condition {step.get('if')!r}, "
                               f"not the modelled {REPLAY_EXCLUDED_STEP_CONDITIONS[name]!r}")
        step_env = step.get("env", {})
        named = set(_RUNNER_VARIABLE_RE.findall(str(step.get("run", "")))) - modelled_variables
        named |= {str(key) for key in step_env if _RUNNER_VARIABLE_RE.fullmatch(str(key))}
        if named:
            raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} names runner variables the replay does not "
                               f"model: {', '.join(sorted(named))}")
        if "uses" in step:
            action = str(step["uses"]).strip()
            supported = REPLAY_SUBSTITUTED_INPUTS.get(action)
            given = step.get("with", {})
            if supported is None or not isinstance(given, dict):
                raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} uses {action!r}, which the replay does not model")
            unmodelled = sorted(set(given) - set(supported)) + sorted(
                key for key, value in supported.items() if value is not None and str(given.get(key, "")).strip() != value)
            if unmodelled:
                raise ToolingError(f"REPLAY_INVENTORY_DRIFT: step {name!r} has inputs the replay does not model: "
                                   + ", ".join(unmodelled))
    return job, job.steps


def replay_machine() -> str | None:
    """Why this machine cannot stand in for the job's x86_64 Linux runner, or None."""
    if sys.platform != "linux" or platform.machine().lower() not in REPLAY_MACHINES:
        return f"{sys.platform} {platform.machine()}"
    return None


def replay_contexts(event: str, base: str, head: str) -> dict[str, object]:
    """The expression contexts the replay models for one event."""
    pull_request = event == "pull_request"
    return {
        "github": {
            "event_name": event,
            "sha": _Unmodelled("github.sha") if pull_request else head,
            "event": {
                "before": _Unmodelled("github.event.before") if pull_request else base,
                "pull_request": {"base": {"sha": base}, "head": {"sha": head}} if pull_request else {},
            },
        },
        "steps": {},
    }


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


def _normalized_version(text: str) -> str:
    """A version's PEP 440 normal form, the string installed metadata records (local label included)."""
    match = _VERSION_RE.fullmatch(text.strip())
    if not match:
        raise ValueError(f"version {text.strip()!r} is not a PEP 440 version")
    epoch, release_text, pre, pre_n, post_implicit, post_n, dev, dev_n, local = match.groups()
    post = post_implicit if post_implicit is not None else post_n
    normal = f"{int(epoch)}!" if epoch and int(epoch) else ""
    normal += ".".join(str(int(part)) for part in release_text.split("."))
    if pre is not None:
        normal += {"alpha": "a", "a": "a", "beta": "b", "b": "b"}.get(pre.lower(), "rc") + str(int(pre_n or 0))
    if post is not None:
        normal += f".post{int(post or 0)}"
    if dev is not None:
        normal += f".dev{int(dev_n or 0)}"
    if local:
        segments = re.split(r"[-_.]", local[1:].lower())
        normal += "+" + ".".join(str(int(part)) if part.isdigit() else part for part in segments)
    return normal


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
    # PEP 508 extras: identifiers separated by commas, an empty list allowed, no empty element.
    names = [extra.strip() for extra in match.group(2).split(",")] if match and (match.group(2) or "").strip() else []
    if not match or clauses is None or not all(_PROJECT_NAME_RE.fullmatch(name) for name in names):
        raise ValueError(f"unsupported requirement {text.strip()!r}")
    extras = frozenset(_canonical(name) for name in names)
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
        except AmbiguousClause:
            raise
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
    # pip up to 25.x (packaging before 26) excludes, for <V and >V, every pre-,
    # post- or local release of V's release; pip 26 (packaging 26) only V's own
    # family.  Where the two disagree the replay cannot tell what CI's pip does.
    if operator == "<":
        base_rule = version.key < spec.key and not (version.prerelease and not spec.prerelease and same_release)
        family = not spec.prerelease and version.prerelease and (
            version.key[:4] == spec.key[:4] if spec.postrelease else same_release)
        family_rule = version.key < spec.key and not family
    else:
        base_rule = version.key > spec.key and not (
            ((version.postrelease and not spec.postrelease) or version.local) and same_release)
        family = (not spec.postrelease and spec.key[4] == (1, 0) and version.postrelease
                  and version.key[:3] == spec.key[:3]) or (version.local and version.key == spec.key)
        family_rule = version.key > spec.key and not family
    if base_rule != family_rule:
        raise AmbiguousClause(f"pip releases decide {installed} against {operator}{text} differently "
                              "(before pip 26 it fails, from pip 26 it holds)")
    return base_rule


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


def _module_locatable(dotted: str, search_path: list[str] | None) -> bool:
    """Whether a module is found on the path, without importing or running it."""
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*", dotted):
        raise ValueError(f"unsupported module name {dotted!r}")
    locations: list[str] = list(search_path or sys.path)
    parts = dotted.split(".")
    for index in range(len(parts)):
        spec = importlib.machinery.PathFinder.find_spec(".".join(parts[:index + 1]), locations)
        if spec is None:
            return False
        locations = list(spec.submodule_search_locations or [])
        if index + 1 < len(parts) and not locations:
            return False
    return True


def _configuration_problems(pyproject: dict[str, object], root: Path) -> list[str]:
    """What in the editable project's configuration the substitute does not model or setuptools would reject."""
    problems = [f"top-level tables {sorted(set(pyproject) - REPLAY_PYPROJECT_TABLES)}"] \
        if set(pyproject) - REPLAY_PYPROJECT_TABLES else []
    problems += [f"{name} (not modelled)" for name in ("setup.py", "setup.cfg") if (root / name).exists()]
    project = pyproject.get("project")
    if not isinstance(project, dict):
        return problems + ["no [project] table"]
    if set(project) - REPLAY_PROJECT_KEYS:
        problems.append(f"[project] keys {sorted(set(project) - REPLAY_PROJECT_KEYS)}")
    for key, pattern in (("name", _PROJECT_NAME_RE), ("version", None), ("requires-python", None),
                         ("description", re.compile(r"[^\r\n]*")), ("readme", None)):
        value = project.get(key, "") if key not in ("name", "version") else project.get(key)
        if not isinstance(value, str) or (pattern is not None and not pattern.fullmatch(value)):
            problems.append(f"[project] {key} {value!r}")
    readme = project.get("readme")
    if isinstance(readme, str) and (Path(readme).suffix.lower() not in {".md", ".rst", ".txt"}
                                    or not (root / readme).is_file()):
        problems.append(f"[project] readme {readme!r} (no such .md, .rst or .txt file)")
    dependencies = project.get("dependencies", [])
    if not isinstance(dependencies, list) or not all(isinstance(entry, str) for entry in dependencies):
        problems.append("[project] dependencies is not a list of strings")
    groups = {key: project.get(key, {}) for key in ("scripts", "gui-scripts")}
    entry_points = project.get("entry-points", {})
    if not isinstance(entry_points, dict) or {"console_scripts", "gui_scripts"} & set(entry_points):
        problems.append("[project] entry-points is not a table of groups other than console_scripts and gui_scripts")
    else:
        groups.update({f"entry-points.{group}": entries for group, entries in entry_points.items()})
    for group, entries in groups.items():
        script = group in ("scripts", "gui-scripts")
        if not isinstance(entries, dict) or not all(
                isinstance(value, str) and _OBJECT_REFERENCE_RE.fullmatch(value.strip()) and (":" in value or not script)
                for value in entries.values()):
            problems.append(f"[project] {group} is not a table of object references")
    tool = pyproject.get("tool", {})
    if not isinstance(tool, dict) or tool.get("setuptools") != REPLAY_SETUPTOOLS_CONFIG or "distutils" in tool:
        problems.append("[tool.setuptools] or [tool.distutils] is not the one the replay models")
    return problems


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


_SHELL_SPECIAL = frozenset(";&|<>()`$*?[]{}~!#\\")


def _simple_command(text: str) -> list[str]:
    """The words of one bash simple command with nothing for the shell to interpret, or ValueError.

    Outside quotes no operator, expansion, glob, comment or escape is allowed,
    inside double quotes no expansion or escape, and no line break anywhere: the
    substitute stands in for exactly one command, so a second one, a pipeline or
    a redirection would go unrun.
    """
    text = text.strip()
    quote = ""
    for char in text:
        if char in "\n\r":
            raise ValueError("the install step is not one simple command: it has a line break")
        if quote:
            if char == quote:
                quote = ""
            elif quote == '"' and char in "$`\\":
                raise ValueError(f"the install step is not one simple command: {char!r} inside double quotes")
        elif char in "'\"":
            quote = char
        elif char in _SHELL_SPECIAL:
            raise ValueError(f"the install step is not one simple command: {char!r} outside quotes")
    if quote:
        raise ValueError("the install step is not one simple command: an unterminated quote")
    return shlex.split(text)


def _tree_files(root: Path) -> dict[str, bytes]:
    return {path.relative_to(root).as_posix(): path.read_bytes() for path in sorted(root.rglob("*")) if path.is_file()}


def _metadata_differences(name: str, project_dir: Path, distribution: importlib.metadata.Distribution,
                          search_path: list[str] | None, scratch: Path | None) -> list[str]:
    """Where the installed project's metadata differs from what the build backend generates from the candidate.

    The backend's prepare_metadata_for_build_editable hook runs offline in the
    caller's environment, under closed rails, against the candidate's tree;
    its output must equal the installed .dist-info, REPLAY_INSTALLER_FILES
    aside, file for file and byte for byte.
    """
    location = getattr(distribution, "_path", None)  # a PathDistribution's .dist-info; any other fails closed
    if not isinstance(location, Path) or not location.is_dir():
        raise ValueError(f"the installed metadata of {name!r} is not a directory the replay can read")
    with tempfile.TemporaryDirectory(prefix="replay-metadata-", dir=scratch) as work:
        output = Path(work) / "metadata"
        output.mkdir()
        result = subprocess.run(
            [sys.executable, "-I", "-B", "-c", _PREPARE_METADATA, str(REPLAY_BUILD_SYSTEM["build-backend"]),
             str(output), *(search_path or [])],
            cwd=project_dir, env=child_environment(dict(os.environ), Path(work)),
            capture_output=True, text=True, check=False)
        generated = list(output.glob("*.dist-info"))
        if result.returncode != 0 or len(generated) != 1:
            raise ValueError(f"the build backend did not prepare the metadata of {name!r}: "
                             + (result.stderr.strip()[-500:] or f"{len(generated)} .dist-info directories"))
        want = _tree_files(generated[0])
    have = {path: data for path, data in _tree_files(location).items() if path not in REPLAY_INSTALLER_FILES}
    differences = []
    for path in sorted(set(want) | set(have)):
        if path not in have:
            differences.append(f"{name} metadata {path} (not installed; the candidate generates it)")
        elif path not in want:
            differences.append(f"{name} metadata {path} (installed; the candidate generates none)")
        elif have[path] != want[path]:
            old, new = (data.decode("utf-8", "replace").splitlines() for data in (have[path], want[path]))
            line = next((i for i, pair in enumerate(zip(old, new)) if pair[0] != pair[1]), min(len(old), len(new)))
            if old == new:
                differences.append(f"{name} metadata {path} (differs from the candidate's in its line breaks)")
                continue
            differences.append(f"{name} metadata {path} line {line + 1}: installed "
                               f"{old[line][:120] if line < len(old) else 'end of file'!r}, the candidate's "
                               f"{new[line][:120] if line < len(new) else 'end of file'!r}")
    return differences


def _install_check(run_text: str, copy: Path, search_path: list[str] | None = None,
                   scratch: Path | None = None) -> list[str]:
    """What the caller's environment lacks for CI's install step to change nothing.

    The step's requirements and their installed dependencies, extras included,
    must be satisfied.  pip reinstalls the editable project, so its installed
    version, entry points and every other metadata file must equal what its
    build backend generates from the candidate, and its requires-python must
    admit this interpreter: the replay never runs against a dependency set,
    metadata or wrapper CI's install would replace, nor passes a candidate CI
    cannot install.  pip builds the project in an isolated environment fetched
    from the package index, which an offline check cannot reproduce; the
    project's build system must be REPLAY_BUILD_SYSTEM, and as a fail-closed
    proxy the caller's environment must satisfy its build requirements and hold
    its backend, which generates the metadata compared.  A backend release
    other than CI's can write metadata its own version decides differently;
    the comparison then fails closed.
    """
    words = _simple_command(run_text)
    if "install" not in words or words[:words.index("install")] not in (["pip"], ["python", "-m", "pip"]):
        raise ValueError("the install step is not one 'python -m pip install' command")
    rest = words[words.index("install") + 1:]
    if not rest:
        # pip refuses an install with no requirement, requirements file or project.
        raise ValueError("the install step names nothing to install, which pip refuses")
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
                pyproject = tomllib.loads((target / "pyproject.toml").read_text(encoding="utf-8"))
                project, build = pyproject.get("project"), pyproject.get("build-system")
                if not isinstance(project, dict):
                    raise ValueError("the editable project's pyproject.toml has no [project] table")
                if build != REPLAY_BUILD_SYSTEM:
                    raise ValueError(f"the editable project {project.get('name')!r} has [build-system] {build!r}, not "
                                     f"the one the replay models, {REPLAY_BUILD_SYSTEM!r}")
                problems = _configuration_problems(pyproject, target)
                if problems:
                    raise ValueError(f"the editable project {project.get('name')!r} has configuration the replay does not "
                                     "model or setuptools would reject: " + "; ".join(problems))
                projects.append((project, target))
                roots.append((str(project["name"]), "the install step"))
                roots += [(str(dependency), str(project["name"])) for dependency in project.get("dependencies", [])]
                roots += [(str(requirement), f"{project['name']}'s build-system") for requirement in build["requires"]]
            index += 2
            continue
        if word.startswith("-"):
            raise ValueError(f"unsupported install option {word!r}")
        roots.append((word, "the install step"))
        index += 1
    unmet = _unmet_requirements(roots, search_path)
    backend = str(REPLAY_BUILD_SYSTEM["build-backend"])
    for project, project_dir in projects:
        name = str(project["name"])
        backend_found = _module_locatable(backend, search_path)
        if not backend_found:
            unmet.append(f"{name} build-backend {backend} (not importable)")
        distribution = _distribution(name, search_path)
        if distribution is None:
            continue  # already reported as not installed
        if "version" not in project:
            raise ValueError(f"the editable project {name!r} declares no static version")
        # pip's reinstall rewrites the installed metadata with the candidate's normalized version string.
        if _normalized_version(distribution.version) != _normalized_version(str(project["version"])):
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
        if backend_found:
            unmet += _metadata_differences(name, project_dir, distribution, search_path, scratch)
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
        machine = replay_machine()
        if machine:
            raise ToolingError(f"the job runs on {job.keys['runs-on']} (x86_64 Linux); this machine is {machine}")
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return
    actual = f"{sys.version_info.major}.{sys.version_info.minor}"
    report.out(f"event={context.event} base={base} head={head}" + (" (full validation)" if context.full else ""))
    report.out(f"copy={copy} interpreter={sys.executable} python={sys.version.split()[0]} workflow_python={python_version}")
    runner_temp = context.temporary / "replay-runner-temp"
    runner_temp.mkdir()
    contexts = replay_contexts(context.event, base, head)
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
            outcome, detail = _substitute(step, reason, copy, python_version, actual, context.temporary)
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
                python_version: str, actual: str, scratch: Path | None = None) -> tuple[str, str]:
    uses = str(step.get("uses", ""))
    if uses.startswith("actions/checkout@"):
        return "success", f"{reason}; copy at {git_text(copy, 'rev-parse', 'HEAD')}"
    if uses.startswith("actions/setup-python@"):
        if actual != python_version:
            return "failure", f"TOOLING interpreter {actual} is not the workflow's python-version {python_version}"
        return "success", f"{reason}: {actual}"
    run = str(step.get("run", ""))
    try:
        unmet = _install_check(run, copy, scratch=scratch)
    except (OSError, KeyError, TypeError, ValueError, tomllib.TOMLDecodeError) as exc:
        return "failure", f"TOOLING cannot read the install step's inputs: {exc}"
    if unmet:
        return "failure", "TOOLING the caller's environment does not satisfy the install step: " + ", ".join(unmet)
    return "success", (f"{reason}: the environment already satisfies every requirement the step names, their "
                       "dependencies and extras, and the editable project's build system and installed metadata")


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
    # The runner reads the step's file commands whatever its exit status, and a record it rejects fails the step.
    outputs, problem = parse_github_output(output_file.read_bytes())
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    if result.returncode == 0 and problem is None:
        return "success", "\n".join(lines[-3:]), outputs
    head = [] if result.returncode == 0 else [
        f"{_classify_failure(result.returncode, result.stdout)} exit {result.returncode}"]
    head += [f"{problem[0]} {problem[1]}"] if problem else []
    return "failure", "\n".join(head + lines[-30:]), outputs


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
    # Chosen before anything is created: tempfile's own search would write a
    # probe file into a TMPDIR inside the repository.
    parent = next((Path(c).resolve() for c in (os.environ.get("TMPDIR"), os.environ.get("TEMP"), os.environ.get("TMP"),
                                               "/tmp", "/var/tmp", "/usr/tmp") if c and os.path.isdir(c)), None)
    if parent is None or parent.is_relative_to(repo):
        print("PREPUSH_CHECK_REFUSED: the temporary directory would be inside the repository or there is none",
              file=sys.stderr)
        return EXIT_REFUSED
    temporary = Path(tempfile.mkdtemp(prefix="prepush-check-", dir=parent)).resolve()
    if temporary.is_relative_to(repo):
        shutil.rmtree(temporary, ignore_errors=True)
        print("PREPUSH_CHECK_REFUSED: the temporary directory would be inside the repository", file=sys.stderr)
        return EXIT_READ_ONLY_VIOLATION if repository_state(repo) != before else EXIT_REFUSED
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
            except Exception as exc:  # noqa: BLE001
                # Keep the post-run read-only check reachable whatever a report raised.
                report.fail(f"{type(exc).__name__}: {exc}", tooling=True)
            duration = time.monotonic() - started
            report.out(f"status={report.status} duration={duration:.1f}s")
            results.append((name, report.status, duration))
    finally:
        shutil.rmtree(temporary, ignore_errors=True)
    after = repository_state(repo)
    if after != before:
        print("PREPUSH_CHECK_READ_ONLY_VIOLATION: the repository's tree, ignored files, directories, HEAD or git "
              "metadata changed", file=sys.stderr)
        return EXIT_READ_ONLY_VIOLATION
    overall = "PASS" if all(status == "PASS" for _n, status, _d in results) else "FAIL"
    print("PREPUSH_CHECK_RESULT: " + overall + " "
          + " ".join(f"{name}={status}" for name, status, _d in results)
          + "; repository unchanged (tree, ignored files, directories, HEAD and git metadata)", flush=True)
    print("PREPUSH_CHECK_NONCLAIM: this result is not CI's result, not QA and not governed evidence", flush=True)
    return EXIT_OK if overall == "PASS" else EXIT_REPORT_FAILED


if __name__ == "__main__":
    raise SystemExit(main())
