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
  replayed in a throwaway copy of the head.  It replays only the one workflow
  whose SHA-256 is REPLAY_WORKFLOW_SHA256 and refuses any other, so a PR that
  changes ci.yml updates that value and the replay's model with it.  CI's
  install step needs the package index and is not run: the caller's
  environment holding CI's install is a precondition, checked only for the
  presence of each distribution the step names.

Every write goes under one owner-only temporary directory outside the
repository, removed at exit.  Repository code runs only in a throwaway copy,
never in the caller's checkout: ``lanes`` and ``membership`` load the
classifier in a child process inside a copy of the head, as ``sweep`` and
``replay`` run there.  The tool refuses a dirty tree, acts on committed
revisions only, resolves refs locally, opens no network connection, runs
children under closed rails, and compares the repository's state before and
after as a check.  Its green is not CI's green and not QA; its output is not
governed evidence.

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

# The SHA-256 of the one ci.yml the replay models.  The replay refuses any
# other workflow text before reading it, so its YAML reader and inventory only
# ever see this file; a PR that changes ci.yml updates this value in the same
# PR, which the owner test requires.
REPLAY_WORKFLOW_SHA256 = "d02021f3bbeb22ec569fe6282c046d68468af003f0f0370313c5e76f58b6ab9b"
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
# A requirement as the install step and its -r files write one: a
# distribution name, then optionally extras, version clauses or a marker, none
# of which the presence check reads.  A URL, a path or any other form fails
# closed.
_REQUIREMENT_NAME_RE = re.compile(
    r"([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)\s*(?:\[[^\]]*\])?\s*(?:[<>=!~(;][^@]*)?")

_TESTS_TOKEN_RE = re.compile(r"tests/[A-Za-z0-9_./-]+")
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
    """Digest of git metadata: every file's lstat identity, its bytes outside objects/, and every directory's name.

    Any write to a file changes its st_ctime_ns, which user space cannot set
    back, so a rewrite with the same bytes is seen too; an object is therefore
    not read.  An empty directory holds no file, so without its name its
    creation or removal would go unseen.
    """
    digest = hashlib.sha256()
    for path in sorted(directory.rglob("*")):
        rel = path.relative_to(directory).as_posix()
        if path.is_dir() and not path.is_symlink():
            digest.update(f"{rel}/\0".encode())
            continue
        if not (path.is_file() or path.is_symlink()):
            continue
        info = path.lstat()
        digest.update(f"{rel}\0{info.st_mode}\0{info.st_size}\0{info.st_mtime_ns}\0{info.st_ctime_ns}\0".encode())
        if rel.startswith("objects/"):
            continue
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
    return _lstat_entries(repo, git(repo, "ls-files", "-z", "--others", "--ignored", "--exclude-standard").stdout)


def _tracked_entries(repo: Path) -> tuple[tuple[str, int, int, int, int], ...]:
    """Every tracked file with its lstat identity.

    git status compares content, so a tracked file rewritten with the same
    bytes would otherwise go unseen; the write still changes its st_ctime_ns.
    """
    return _lstat_entries(repo, git(repo, "ls-files", "-z").stdout)


def _lstat_entries(repo: Path, listing: bytes) -> tuple[tuple[str, int, int, int, int], ...]:
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
    tracked: tuple[tuple[str, int, int, int, int], ...]
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
    return RepositoryState(head=head, status=status, tracked=_tracked_entries(repo), ignored=_ignored_entries(repo),
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


def in_copy(copy: Path, temporary: Path, function: str, *args: object) -> dict[str, object]:
    """Call one of this tool's functions in a child whose working directory is the copy; it answers in JSON.

    Repository code (the classifier) is then loaded from the copy and runs
    there, never in the caller's checkout or in this process.
    """
    code = (
        "import importlib.util, json, sys\n"
        "sys.dont_write_bytecode = True\n"
        "spec = importlib.util.spec_from_file_location('_prepush_check_child', sys.argv[1])\n"
        "module = importlib.util.module_from_spec(spec)\n"
        "sys.modules['_prepush_check_child'] = module\n"
        "spec.loader.exec_module(module)\n"
        "print(json.dumps(getattr(module, sys.argv[2])(*json.loads(sys.argv[3]))))\n"
    )
    result = subprocess.run([sys.executable, "-B", "-c", code, str(TOOL_PATH), function, json.dumps(list(args))],
                            cwd=copy, env=child_environment(dict(os.environ), temporary, {"GIT_OPTIONAL_LOCKS": "0"}),
                            capture_output=True, text=True, check=False)
    if result.returncode != 0 or not result.stdout.strip():
        last = result.stderr.strip().splitlines()[-1:] or [f"exit {result.returncode} and no answer"]
        raise ToolingError(f"{function} failed in the throwaway copy: {last[0][:500]}")
    return json.loads(result.stdout.strip().splitlines()[-1])


def normalized_paths(root: str, paths: list[str]) -> dict[str, object]:
    """The classifier's normal form of each path; run by in_copy."""
    classifier = load_classifier(Path(root))
    normalized = []
    for raw in paths:
        try:
            normalized.append(classifier._normalized_path(raw))
        except ValueError as exc:
            return {"error": f"invalid path {raw!r}: {exc}"}
    return {"paths": normalized}


def classify_given_paths(root: str, paths: list[str], output: str, target_file: str) -> dict[str, object]:
    """The classifier's outputs for given paths against the root's files; run by in_copy."""
    classifier = load_classifier(Path(root))
    try:
        governed = classifier._load_governed_primary_paths(Path(root))
        result = classifier.classify_paths(paths, governed_paths=governed)
        targets = result.test_targets or classifier.changed_test_targets(Path(root), paths)
        classification = classifier.Classification(
            flags=result.flags, reason=result.reason, path_count=result.path_count, test_targets=targets)
        classifier.write_github_output(Path(output), classification)
        classifier.write_changed_test_targets(Path(target_file), classification.test_targets)
    except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
        return {"error": f"CI_CHANGE_CLASSIFIER_ERROR:{exc}"}
    return {"reason": classification.reason, "path_count": classification.path_count,
            "lanes": [lane for lane in classifier.LANES if classification.flags[lane]]}


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


def head_copy(context: Context, name: str) -> tuple[str, Path]:
    """The head's commit and a throwaway copy of it: a report runs no repository code in the checkout."""
    head = resolve_commit(context.repo, context.head_ref)
    return head, make_copy(context.repo, head, context.temporary / f"{name}-copy")


# --------------------------------------------------------------------------
# lanes
# --------------------------------------------------------------------------

def report_lanes(context: Context, report: Report) -> None:
    outputs = _lanes_for_given_paths(context, report) if context.paths else _lanes_for_refs(context, report)
    if outputs.get("reason") == "documentation_only":
        report.out("note: reason=documentation_only means the workflow's path filter starts no hosted run")


def _lanes_for_given_paths(context: Context, report: Report) -> dict[str, str]:
    output = context.temporary / "lanes-paths-github-output.txt"
    target_file = context.temporary / "lanes-paths-changed-tests.txt"
    output.unlink(missing_ok=True)
    try:
        head, copy = head_copy(context, "lanes")
        report.out(f"mode=paths head={context.head_ref}->{head} paths={len(context.paths)} "
                   "(classified in a throwaway copy)")
        report.out("note: changed-test targets are computed against the head's files; "
                   "a planned file that does not exist yet selects no target of its own")
        answer = in_copy(copy, context.temporary, "classify_given_paths", str(copy), context.paths,
                         str(output), str(target_file))
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return {}
    if "error" in answer:
        report.fail(str(answer["error"]))
        return {}
    enabled = ",".join(answer["lanes"]) or "none"  # type: ignore[arg-type]
    report.out(f"classification reason={answer['reason']};paths={answer['path_count']};lanes={enabled}")
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
    try:
        root = make_copy(context.repo, head, context.temporary / "lanes-copy")
        if git(root, "cat-file", "-e", f"{base}^{{commit}}", check=False).returncode != 0:
            raise ToolingError(f"base {base} is not available to the throwaway copy")
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return {}
    report.out(f"note: classified in a throwaway copy at {head}")
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
    try:
        head, copy = head_copy(context, "membership")
        answer = in_copy(copy, context.temporary, "normalized_paths", str(copy), context.paths)
        if "error" in answer:
            report.fail(str(answer["error"]))
            return
        version, roster = admitted_release(copy)
    except ToolingError as exc:
        report.fail(str(exc), tooling=True)
        return
    paths = [str(path) for path in answer["paths"]]  # type: ignore[union-attr]
    manifest = copy / MANIFEST_PATH
    release_id = hashlib.sha256(manifest.read_bytes()).hexdigest() if manifest.is_file() else "unavailable"
    report.out(f"admitted release version={version} roster={len(roster)} release_id={release_id} "
               f"head={head} (read in a throwaway copy)")
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


def _distribution(name: str, search_path: list[str] | None) -> importlib.metadata.Distribution | None:
    return next(iter(importlib.metadata.distributions(name=name, path=search_path or sys.path)), None)


def _requirement_name(text: str) -> str:
    match = _REQUIREMENT_NAME_RE.fullmatch(text.strip())
    if not match:
        raise ValueError(f"unsupported requirement {text.strip()!r}")
    return match.group(1)


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


def _install_check(run_text: str, copy: Path, search_path: list[str] | None = None) -> list[str]:
    """The distributions CI's install step names that the caller's environment does not hold.

    The step needs the package index, so the replay does not run it: that the
    caller's environment already holds CI's install is its stated
    precondition (instruction ID-8).  This checks only that each distribution
    the step names is installed: every requirement on its command line and in
    its -r files, and the editable project by its [project] name.  Versions,
    extras, markers, dependencies, the build system and the installed
    project's metadata are the caller's to match; they are not checked.
    """
    words = _simple_command(run_text)
    if "install" not in words or words[:words.index("install")] not in (["pip"], ["python", "-m", "pip"]):
        raise ValueError("the install step is not one 'python -m pip install' command")
    rest = words[words.index("install") + 1:]
    if not rest:
        # pip refuses an install with no requirement, requirements file or project.
        raise ValueError("the install step names nothing to install, which pip refuses")
    names: list[str] = []
    index = 0
    while index < len(rest):
        word = rest[index]
        if word in {"-r", "--requirement", "-e", "--editable"} and index + 1 < len(rest):
            target = copy / rest[index + 1]
            if word in {"-r", "--requirement"}:
                names += [_requirement_name(line) for line in _requirement_lines(target)]
            else:
                project = tomllib.loads((target / "pyproject.toml").read_text(encoding="utf-8")).get("project")
                if not isinstance(project, dict) or not isinstance(project.get("name"), str):
                    raise ValueError("the editable project's pyproject.toml names no [project] name")
                names.append(project["name"])
            index += 2
            continue
        if word.startswith("-"):
            raise ValueError(f"unsupported install option {word!r}")
        names.append(_requirement_name(word))
        index += 1
    return sorted({name for name in names if _distribution(name, search_path) is None})


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
        workflow = (copy / WORKFLOW_PATH).read_bytes()
        workflow_sha256 = hashlib.sha256(workflow).hexdigest()
        if workflow_sha256 != REPLAY_WORKFLOW_SHA256:
            raise ToolingError(f"REPLAY_INVENTORY_DRIFT: the head's {WORKFLOW_PATH} has SHA-256 {workflow_sha256}, "
                               f"not the modelled {REPLAY_WORKFLOW_SHA256}; a PR that changes the workflow updates "
                               "REPLAY_WORKFLOW_SHA256 and the replay's model with it")
        job, steps = replay_steps(workflow.decode("utf-8"))
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
    report.out(f"workflow {WORKFLOW_PATH} sha256={workflow_sha256} (the modelled one)")
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
        missing = _install_check(run, copy)
    except (OSError, KeyError, TypeError, ValueError, tomllib.TOMLDecodeError) as exc:
        return "failure", f"TOOLING cannot read the install step's inputs: {exc}"
    if missing:
        return "failure", ("TOOLING the caller's environment lacks distributions the install step names: "
                           + ", ".join(missing))
    return "success", (f"{reason}: every distribution the step names is installed (versions, dependencies and the "
                       "editable project's metadata are the caller's to match)")


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
    parser.add_argument("--head", default=DEFAULT_HEAD,
                        help="head ref for lanes, membership, sweep and replay (default HEAD)")
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
