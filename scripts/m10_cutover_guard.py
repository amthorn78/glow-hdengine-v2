#!/usr/bin/env python3
"""Magic10 active-configuration cutover guard (HDE-COAG003.6): a read-only release preflight.

Usage::

    python scripts/m10_cutover_guard.py --candidate <candidate checkout root> --prior <prior release commit>

``--candidate`` is the root of a clean git checkout of the release candidate. ``--prior`` is the
prior release's commit, resolved in the candidate's own repository. The guard proves four things:

* P1 ``one_active_configuration``: the candidate admits; its manifest binds exactly one mechanics
  configuration, ``catalog/magic10_mechanics_v2.json``; the admitted configuration is that file, and
  its ``config_id`` is ``m10-relevance-centers-type-v2.0.0``.
* P2 ``no_reachable_v1_or_fallback``: the static import closure of the production entry points
  reaches no retired v1 scorer, threshold module or Type-only scorer, and no closure module names the
  v1 configuration outside a set display.
* P3 ``release_identity``: the candidate's admitted ``release_id`` differs from the prior's; every
  declared and rebound v2 member is a manifest row, the rebound one with bytes different from the
  prior's row; the candidate's validation pair and attestation contract test pass.
* P4 ``compatible_prior_pack``: the prior commit's tree, extracted read-only from git, admits on its
  own; ``migrations/`` and the two Reader schemas are unchanged; the prior's v1 and the candidate's
  v2 cache namespaces are disjoint.

Every step that executes a tree's code runs in a subprocess rooted at that tree, with an environment
built from scratch under closed rails, because admission binds the executing root. The guard writes
nothing in either tree or in any repository; its one temporary directory, which also holds the
children's temporary files (``TMPDIR``), is removed. The report is canonical JSON on stdout. stderr
is keys-only.

Exit codes: 0 all four proofs PASS; 1 a proof FAILED; 2 usage error; 3 a precondition refused and no
proof was evaluated; 4 the candidate changed during the run; 5 internal error (no report).

Stated limits:

* P2 is static. A dynamic import through a computed string, or a v1 path or selector built at
  runtime, is not seen. A string that is an element of a set display is read as a membership domain,
  not as a read.
* The guard trusts the exit codes of the candidate's own validation pair and contract test; it does
  not interpret their output.
* The candidate's code runs under this interpreter, which must have the candidate's dependencies.
* Ignored files are outside the cleanliness check. No timeout is applied to a child.
* The guard does not compare the candidate's ``release_id`` with the attested v2 ``release_id``.
"""
from __future__ import annotations

import argparse
import ast
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path
from typing import Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.serializer.canon import sercanon  # noqa: E402

REPORT_SCHEMA = "m10_cutover_guard_report.v1"

# HDE Schemas and Artifacts §2.9 identities; Specification R-15.
V1_CONFIGURATION_PATH = "catalog/magic10_mechanics_v1.json"
V2_CONFIGURATION_PATH = "catalog/magic10_mechanics_v2.json"
CONFIGURATION_PATHS = (V1_CONFIGURATION_PATH, V2_CONFIGURATION_PATH)
V1_CONFIG_ID = "m10-channel-state-v1.0.0"
V2_CONFIG_ID = "m10-relevance-centers-type-v2.0.0"
_V1_CONFIGURATION_SUFFIX = "magic10_mechanics_v1.json"

# The INV-5 production entry points and the retired v1 module set (the switch's retirement list,
# plus the two Type-only scorers HDE-EPIC043 WU-PR-03 removed).
ENTRY_POINTS = ("adapter/factory.py", "engine/cli/main.py", "engine/http/compat_handler.py")
RETIRED_MODULES = frozenset({
    "engine.compat.thresholds",
    "engine.compat.ts_v0",
    "engine.compat.type_strategy_v0",
    "engine.magic10.calculators",
    "engine.magic10.composite",
    "engine.magic10.signals",
    "engine.magic10.thresholds",
})

MIGRATIONS_PATH = "migrations"
READER_SCHEMAS = ("schemas/reader.v1.schema.json", "schemas/reader.v2.schema.json")
VALIDATION_PAIR = (
    ("release_id_recompute", ("scripts/release_id_recompute.py", "--check-manifest-only")),
    ("check_release_identity", ("ci/checks/check_release_identity.sh",)),
)
CONTRACT_TEST = "tests/tools/test_magic10_release_attestation_contract.py"

PROOFS = (
    ("P1", "one_active_configuration"),
    ("P2", "no_reachable_v1_or_fallback"),
    ("P3", "release_identity"),
    ("P4", "compatible_prior_pack"),
)

EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_USAGE = 2
EXIT_REFUSED = 3
EXIT_CHANGED = 4
EXIT_ERROR = 5

_HEX64 = re.compile(r"[0-9a-f]{64}")

# Probes run as ``python -B -c`` with the working directory at a tree's root. Each prints one JSON
# object as its last stdout line and reports a refusal by token, never by message.
_PROBE_PRELUDE = r'''
import importlib, json, os, re, sys
from pathlib import Path
_root = Path(os.getcwd()).resolve()
class _Refused(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code
def _emit(payload):
    sys.stdout.write("\n" + json.dumps(payload, sort_keys=True) + "\n")
def _code(exc):
    code = getattr(exc, "code", None)
    if isinstance(code, str) and re.fullmatch(r"[A-Z][A-Z0-9_]*", code):
        return code
    return type(exc).__name__
def _load(name):
    module = importlib.import_module(name)
    if not Path(module.__file__).resolve().is_relative_to(_root):
        raise _Refused("IMPORT_OUTSIDE_ROOT")
    return module
'''
_ADMISSION_PROBE = _PROBE_PRELUDE + r'''
try:
    _bundle = _load("engine.config.registry_loader").load_active_mechanics_bundle()
    _emit({"ok": True, "release_id": _bundle.release_id, "config_sha256": _bundle.config_sha256})
except Exception as exc:
    _emit({"ok": False, "code": _code(exc)})
'''
_V2_CONSTANTS_PROBE = _PROBE_PRELUDE + r'''
try:
    _module = _load("engine.config.magic10_v2_loader")
    _emit({
        "ok": True,
        "declared": list(_module.MAGIC10_V2_DECLARED_MEMBERS),
        "rebound": list(_module.MAGIC10_V2_REBOUND_MEMBERS),
        "prefix": _module.MAGIC10_V2_INTRINSIC_CACHE_PREFIX,
    })
except Exception as exc:
    _emit({"ok": False, "code": _code(exc)})
'''
_V1_PREFIX_PROBE = _PROBE_PRELUDE + r'''
try:
    _emit({"ok": True, "prefix": _load("engine.compat.compute").INTRINSIC_CACHE_PREFIX})
except Exception as exc:
    _emit({"ok": False, "code": _code(exc)})
'''


def _child_env(tmp: Path | None = None) -> dict[str, str]:
    """The complete environment of every child: closed rails, nothing inherited but PATH.

    A child that runs a tree's code also gets ``TMPDIR`` inside the guard's temporary directory, so
    the temporary files of that code, pytest's base directory included, are removed with it.
    """
    env = {
        "PATH": os.environ.get("PATH", os.defpath),
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    if tmp is not None:
        env["TMPDIR"] = str(tmp)
    return env


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        env=_child_env(), stdin=subprocess.DEVNULL, capture_output=True, check=False,
    )


def _python(root: Path, tmp: Path, *args: str) -> int:
    done = subprocess.run(
        [sys.executable, "-B", *args],
        cwd=root, env=_child_env(tmp), stdin=subprocess.DEVNULL, capture_output=True, check=False,
    )
    return done.returncode


def _probe(root: Path, tmp: Path, source: str) -> dict:
    done = subprocess.run(
        [sys.executable, "-B", "-c", source],
        cwd=root, env=_child_env(tmp), stdin=subprocess.DEVNULL, capture_output=True, check=False,
    )
    lines = done.stdout.decode("utf-8", "replace").strip().splitlines()
    try:
        payload = json.loads(lines[-1])
    except (IndexError, ValueError):
        return {"ok": False, "code": "PROBE_NO_RESULT"}
    if not isinstance(payload, dict) or not isinstance(payload.get("ok"), bool):
        return {"ok": False, "code": "PROBE_NO_RESULT"}
    if not payload["ok"] and not isinstance(payload.get("code"), str):
        return {"ok": False, "code": "PROBE_NO_RESULT"}
    return payload


def _admission(root: Path, tmp: Path) -> dict:
    payload = _probe(root, tmp, _ADMISSION_PROBE)
    if payload["ok"] and not all(
        isinstance(payload.get(key), str) and _HEX64.fullmatch(payload[key])
        for key in ("release_id", "config_sha256")
    ):
        return {"ok": False, "code": "PROBE_INVALID_RESULT"}
    return payload


def _v2_constants(root: Path, tmp: Path) -> dict:
    payload = _probe(root, tmp, _V2_CONSTANTS_PROBE)
    if payload["ok"] and not (
        all(
            isinstance(payload.get(key), list) and all(isinstance(item, str) for item in payload[key])
            for key in ("declared", "rebound")
        )
        and isinstance(payload.get("prefix"), str)
    ):
        return {"ok": False, "code": "PROBE_INVALID_RESULT"}
    return payload


def _v1_prefix(root: Path, tmp: Path) -> dict:
    payload = _probe(root, tmp, _V1_PREFIX_PROBE)
    if payload["ok"] and not isinstance(payload.get("prefix"), str):
        return {"ok": False, "code": "PROBE_INVALID_RESULT"}
    return payload


def _rev(root: Path, name: str) -> str | None:
    done = _git(root, "rev-parse", "--verify", "--quiet", name)
    value = done.stdout.decode("ascii", "replace").strip()
    return value if done.returncode == 0 and value else None


def _status(root: Path) -> bytes | None:
    # --no-optional-locks: a plain status may rewrite .git/index; this check must write nothing.
    done = _git(root, "--no-optional-locks", "status", "--porcelain", "--untracked-files=all", "-z")
    return done.stdout if done.returncode == 0 else None


def _read_manifest(root: Path) -> dict[str, Mapping[str, object]] | None:
    """The manifest's rows by path, or None when it is not the release manifest shape."""
    try:
        data = json.loads((root / "catalog/manifest.json").read_bytes())
    except (OSError, ValueError):
        return None
    files = data.get("files") if isinstance(data, dict) else None
    if not isinstance(files, list):
        return None
    rows: dict[str, Mapping[str, object]] = {}
    for row in files:
        if not (isinstance(row, dict) and isinstance(row.get("path"), str) and isinstance(row.get("sha256"), str)):
            return None
        rows[row["path"]] = row
    return rows


def _config_id(root: Path, relative_path: str) -> str | None:
    try:
        data = json.loads((root / relative_path).read_bytes())
    except (OSError, ValueError):
        return None
    value = data.get("config_id") if isinstance(data, dict) else None
    return value if isinstance(value, str) else None


# --- P2: the INV-5 static closure, restated with the root as a parameter --------------------------

def _module_name(root: Path, path: Path) -> str:
    parts = list(path.relative_to(root).with_suffix("").parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _module_file(root: Path, name: str) -> Path | None:
    if not name:
        return None
    base = root.joinpath(*name.split("."))
    if base.with_suffix(".py").is_file():
        return base.with_suffix(".py")
    if (base / "__init__.py").is_file():
        return base / "__init__.py"
    return None


def _imported_names(root: Path, path: Path, tree: ast.AST) -> set[str]:
    own = _module_name(root, path)
    package = own if path.name == "__init__.py" else own.rpartition(".")[0]
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                parts = alias.name.split(".")
                names.update(".".join(parts[:index]) for index in range(1, len(parts) + 1))
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                base = package.split(".") if package else []
                if node.level > 1:
                    base = base[: len(base) - (node.level - 1)]
                module = ".".join(base + ([node.module] if node.module else []))
            else:
                module = node.module or ""
            parts = module.split(".")
            names.update(".".join(parts[:index]) for index in range(1, len(parts) + 1))
            names.update(f"{module}.{alias.name}" for alias in node.names)
    return names


def static_closure(root: Path) -> tuple[dict[str, ast.AST], list[str]]:
    """Return the closure's parsed modules by name, and the paths that could not be read or parsed."""
    seen: dict[str, ast.AST] = {}
    unreadable: list[str] = []
    queue: list[Path] = []
    for entry in ENTRY_POINTS:
        if (root / entry).is_file():
            queue.append(root / entry)
        else:
            unreadable.append(entry)
    while queue:
        path = queue.pop()
        name = _module_name(root, path)
        if name in seen:
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError, ValueError):
            unreadable.append(path.relative_to(root).as_posix())
            continue
        seen[name] = tree
        for imported in _imported_names(root, path, tree):
            target = _module_file(root, imported)
            if target is not None and _module_name(root, target) not in seen:
                queue.append(target)
    return seen, sorted(set(unreadable))


def _names_v1_configuration(tree: ast.AST) -> bool:
    set_elements = {id(element) for node in ast.walk(tree) if isinstance(node, ast.Set) for element in node.elts}
    return any(
        isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and id(node) not in set_elements
        and (node.value.endswith(_V1_CONFIGURATION_SUFFIX) or node.value == V1_CONFIG_ID)
        for node in ast.walk(tree)
    )


# --- P4: the prior tree and tree comparisons ------------------------------------------------------

def _extract_prior(root: Path, commit: str, destination: Path) -> bool:
    """Extract the prior commit's tracked tree from git objects; True only when it is complete."""
    archive = _git(root, "archive", "--format=tar", commit)
    listed = _git(root, "ls-tree", "-r", "-z", "--name-only", commit)
    if archive.returncode != 0 or listed.returncode != 0:
        return False
    expected = {item.decode("utf-8", "surrogateescape") for item in listed.stdout.split(b"\0") if item}
    destination.mkdir()
    try:
        with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as tar:
            tar.extractall(destination, filter="data")
    except (tarfile.TarError, OSError, ValueError):
        return False
    found: set[str] = set()
    for current, directories, files in os.walk(destination):
        base = Path(current)
        for name in files:
            found.add((base / name).relative_to(destination).as_posix())
        for name in directories:
            if (base / name).is_symlink():
                found.add((base / name).relative_to(destination).as_posix())
    return found == expected


def _tree_entries(root: Path, revision: str, paths: Sequence[str]) -> dict[str, str] | None:
    done = _git(root, "ls-tree", "-r", "-z", revision, "--", *paths)
    if done.returncode != 0:
        return None
    entries: dict[str, str] = {}
    for item in done.stdout.split(b"\0"):
        if item:
            meta, _, path = item.decode("utf-8", "surrogateescape").partition("\t")
            entries[path] = meta
    return entries


def _changed(root: Path, head: str, prior: str, paths: Sequence[str]) -> list[str] | None:
    candidate = _tree_entries(root, head, paths)
    previous = _tree_entries(root, prior, paths)
    if candidate is None or previous is None:
        return None
    return sorted(path for path in candidate.keys() | previous.keys() if candidate.get(path) != previous.get(path))


def _disjoint(first: str, second: str) -> bool:
    return bool(first) and bool(second) and not first.startswith(second) and not second.startswith(first)


# --- Proof evaluation ------------------------------------------------------------------------------

def _proof(refusals: set[str], subjects: set[str]) -> dict:
    return {"result": "FAIL" if refusals else "PASS", "refusals": sorted(refusals), "subjects": sorted(subjects)}


def _p1(root: Path, admission: dict, manifest: Mapping | None) -> tuple[dict, str | None]:
    refusals: set[str] = set()
    bound: list[str] = []
    admitted_config_id = None
    if not admission["ok"]:
        refusals.add("P1_ADMISSION_REFUSED")
    if manifest is None:
        refusals.add("P1_MANIFEST_UNREADABLE")
    else:
        bound = [path for path in CONFIGURATION_PATHS if path in manifest]
        if V2_CONFIGURATION_PATH not in bound:
            refusals.add("P1_V2_CONFIGURATION_ROW_MISSING")
        if len(bound) > 1:
            refusals.add("P1_MULTIPLE_CONFIGURATIONS")
        if admission["ok"]:
            admitted = [path for path in bound if manifest[path]["sha256"] == admission["config_sha256"]]
            admitted_path = admitted[0] if len(admitted) == 1 else None
            admitted_config_id = _config_id(root, admitted_path) if admitted_path else None
            if admitted_path != V2_CONFIGURATION_PATH or admitted_config_id != V2_CONFIG_ID:
                refusals.add("P1_ADMITTED_CONFIGURATION_NOT_V2")
    return _proof(refusals, set(bound) if refusals else set()), admitted_config_id


def _p2(closure: Mapping[str, ast.AST], unreadable: Sequence[str]) -> dict:
    refusals: set[str] = set()
    subjects: set[str] = set(unreadable)
    if unreadable:
        refusals.add("P2_SOURCE_UNREADABLE")
    reached = RETIRED_MODULES & closure.keys()
    if reached:
        refusals.add("P2_RETIRED_MODULE_REACHABLE")
        subjects.update(reached)
    named = {name for name, tree in closure.items() if _names_v1_configuration(tree)}
    if named:
        refusals.add("P2_V1_CONFIGURATION_NAMED")
        subjects.update(named)
    return _proof(refusals, subjects)


def _p3(
    candidate: dict, prior: dict | None, constants: dict, manifest: Mapping | None,
    prior_manifest: Mapping | None, pair: Mapping[str, int], contract: int,
) -> dict:
    refusals: set[str] = set()
    subjects: set[str] = set()
    prior_ok = prior is not None and prior["ok"]
    if not candidate["ok"]:
        refusals.add("P3_CANDIDATE_RELEASE_ID_UNAVAILABLE")
    if not prior_ok:
        refusals.add("P3_PRIOR_RELEASE_ID_UNAVAILABLE")
    if candidate["ok"] and prior_ok and candidate["release_id"] == prior["release_id"]:
        refusals.add("P3_RELEASE_ID_UNCHANGED")
    if manifest is None:
        refusals.add("P3_MANIFEST_UNREADABLE")
    if not constants["ok"]:
        refusals.add("P3_DECLARED_MEMBERS_UNAVAILABLE")
    if manifest is not None and constants["ok"]:
        missing = {path for path in (*constants["declared"], *constants["rebound"]) if path not in manifest}
        if missing:
            refusals.add("P3_DECLARED_MEMBER_MISSING")
            subjects.update(missing)
        if prior_manifest is not None:
            unchanged = {
                path for path in constants["rebound"]
                if path in manifest and path in prior_manifest
                and manifest[path]["sha256"] == prior_manifest[path]["sha256"]
            }
            if unchanged:
                refusals.add("P3_REBOUND_MEMBER_UNCHANGED")
                subjects.update(unchanged)
    if any(code != 0 for code in pair.values()):
        refusals.add("P3_VALIDATION_PAIR_FAILED")
    if contract != 0:
        refusals.add("P3_CONTRACT_TEST_FAILED")
    return _proof(refusals, subjects)


def _p4(
    root: Path, head: str, prior: str, extracted: bool, prior_admission: dict | None,
    constants: dict, prior_prefix: dict | None,
) -> dict:
    refusals: set[str] = set()
    subjects: set[str] = set()
    if not extracted:
        refusals.add("P4_PRIOR_TREE_UNAVAILABLE")
    elif prior_admission is None or not prior_admission["ok"]:
        refusals.add("P4_PRIOR_NOT_ADMITTED")
    migrations = _changed(root, head, prior, (MIGRATIONS_PATH,))
    schemas = _changed(root, head, prior, READER_SCHEMAS)
    if migrations is None or schemas is None:
        refusals.add("P4_PRIOR_TREE_UNAVAILABLE")
    else:
        if migrations:
            refusals.add("P4_MIGRATIONS_CHANGED")
            subjects.update(migrations)
        if schemas:
            refusals.add("P4_READER_SCHEMAS_CHANGED")
            subjects.update(schemas)
    if not constants["ok"] or prior_prefix is None or not prior_prefix["ok"]:
        refusals.add("P4_CACHE_PREFIX_UNAVAILABLE")
    elif not _disjoint(prior_prefix["prefix"], constants["prefix"]):
        refusals.add("P4_CACHE_NAMESPACES_NOT_DISJOINT")
    return _proof(refusals, subjects)


# --- The run ---------------------------------------------------------------------------------------

def _report(candidate_arg: str, prior_arg: str) -> dict:
    return {
        "schema": REPORT_SCHEMA,
        "result": "REFUSED",
        "exit_code": EXIT_REFUSED,
        "refusal": None,
        "candidate": {"root": candidate_arg, "head": None},
        "prior": {"commit": prior_arg, "resolved": None},
        "candidate_release_id": None,
        "prior_release_id": None,
        "admitted_config_id": None,
        "admission_codes": {"candidate": None, "prior": None},
        "validation_pair": {name: None for name, _ in VALIDATION_PAIR},
        "contract_test": None,
        "proofs": {
            key: {"name": name, "result": "NOT_EVALUATED", "refusals": [], "subjects": []}
            for key, name in PROOFS
        },
    }


def _refused(report: dict, token: str) -> dict:
    report["refusal"] = token
    return report


def run_guard(candidate_arg: str, prior_arg: str) -> dict:
    """Evaluate the four proofs and return the report; the report's exit_code is the exit status."""
    report = _report(candidate_arg, prior_arg)
    if os.environ.get("SAFE_MODE") != "1" or os.environ.get("ALLOW_NETWORK") != "0":
        return _refused(report, "CLOSED_RAILS_REQUIRED")
    given = Path(candidate_arg)
    if not given.is_dir():
        return _refused(report, "CANDIDATE_NOT_A_GIT_WORK_TREE_ROOT")
    root = given.resolve()
    top = _git(root, "rev-parse", "--show-toplevel")
    top_path = top.stdout.decode("utf-8", "surrogateescape").strip()
    if top.returncode != 0 or not top_path or Path(top_path).resolve() != root:
        return _refused(report, "CANDIDATE_NOT_A_GIT_WORK_TREE_ROOT")
    if _status(root) != b"":
        return _refused(report, "CANDIDATE_NOT_CLEAN")
    head = _rev(root, "HEAD")
    if head is None:
        return _refused(report, "CANDIDATE_NOT_A_GIT_WORK_TREE_ROOT")
    prior = None if prior_arg.startswith("-") else _rev(root, f"{prior_arg}^{{commit}}")
    if prior is None:
        return _refused(report, "PRIOR_NOT_RESOLVED")
    report["candidate"]["head"] = head
    report["prior"]["resolved"] = prior

    work = Path(tempfile.mkdtemp(prefix="m10_cutover_guard_"))
    try:
        child_tmp = work / "tmp"
        child_tmp.mkdir()
        candidate_admission = _admission(root, child_tmp)
        constants = _v2_constants(root, child_tmp)
        closure, unreadable = static_closure(root)
        prior_root = work / "prior"
        extracted = _extract_prior(root, prior, prior_root)
        prior_admission = _admission(prior_root, child_tmp) if extracted else None
        prior_prefix = _v1_prefix(prior_root, child_tmp) if extracted else None
        prior_manifest = _read_manifest(prior_root) if extracted else None
        pair = {name: _python(root, child_tmp, *command) for name, command in VALIDATION_PAIR}
        contract = _python(root, child_tmp, "-m", "pytest", "-q", "-p", "no:cacheprovider", CONTRACT_TEST)
        manifest = _read_manifest(root)
        p1, admitted_config_id = _p1(root, candidate_admission, manifest)
        proofs = {
            "P1": p1,
            "P2": _p2(closure, unreadable),
            "P3": _p3(candidate_admission, prior_admission, constants, manifest, prior_manifest, pair, contract),
            "P4": _p4(root, head, prior, extracted, prior_admission, constants, prior_prefix),
        }
    finally:
        shutil.rmtree(work)

    for key, name in PROOFS:
        report["proofs"][key] = {"name": name, **proofs[key]}
    report["candidate_release_id"] = candidate_admission.get("release_id") if candidate_admission["ok"] else None
    if prior_admission is not None and prior_admission["ok"]:
        report["prior_release_id"] = prior_admission["release_id"]
    report["admitted_config_id"] = admitted_config_id
    report["admission_codes"] = {
        "candidate": None if candidate_admission["ok"] else candidate_admission["code"],
        "prior": None if prior_admission is None or prior_admission["ok"] else prior_admission["code"],
    }
    report["validation_pair"] = pair
    report["contract_test"] = contract

    if _rev(root, "HEAD") != head or _status(root) != b"":
        report["result"], report["exit_code"] = "REFUSED", EXIT_CHANGED
        return _refused(report, "CANDIDATE_CHANGED_DURING_RUN")
    passed = all(proof["result"] == "PASS" for proof in proofs.values())
    report["result"], report["exit_code"] = ("PASS", EXIT_PASS) if passed else ("FAIL", EXIT_FAIL)
    return report


def _log(report: dict) -> None:
    for key, _ in PROOFS:
        print(f"M10_CUTOVER_GUARD:{key}={report['proofs'][key]['result']}", file=sys.stderr)
    if report["refusal"] is None:
        print(f"M10_CUTOVER_GUARD_RESULT:{report['result']}", file=sys.stderr)
    else:
        print(f"M10_CUTOVER_GUARD_REFUSED:{report['refusal']}", file=sys.stderr)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="m10_cutover_guard.py",
        description="Read-only Magic10 cutover preflight over a release candidate checkout and the prior release commit.",
    )
    parser.add_argument("--candidate", required=True, help="root of a clean git checkout of the release candidate")
    parser.add_argument("--prior", required=True, help="the prior release's commit, resolved in the candidate's repository")
    args = parser.parse_args(argv)
    try:
        report = run_guard(args.candidate, args.prior)
    except Exception as exc:  # mapped to the documented internal-error exit; no report is written
        print(f"M10_CUTOVER_GUARD_ERROR:{type(exc).__name__}", file=sys.stderr)
        return EXIT_ERROR
    _log(report)
    sys.stdout.buffer.write(sercanon(report))
    sys.stdout.buffer.flush()
    return report["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
