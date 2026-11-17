"""HDE-EPIC043 WU-PR-03: no Type-only, UID-hash or numeric-Gate compromise scorer in production (HDE-CONJ010.5).

Acceptance items 2 and 3 of the work unit (AC-05, Stage A part):

* the Type-only scorers ``engine/compat/ts_v0.py`` and
  ``engine/compat/type_strategy_v0.py``, and the two standalone legacy scripts
  that imported ``ts_v0``, are absent, and no production module imports a
  removed module (predicate 3);
* no production function derives a score or band from a hash of a user, person
  or UID value (predicate 1, the UID-hash negative proof);
* no production module defines a function or class named for the historical
  numeric-Gate compromise helper (predicate 2). ``compromise`` as a Channel-state
  value is data, not the helper.

Scope of "production module": every ``.py`` file under ``adapter/``,
``engine/`` and ``presenter/``, plus every module of the static INV-5 closure
of the three production entry points, which reaches some modules under
``tools/`` and ``scripts/``. The closure is taken from the landed INV-5 test,
loaded read-only. The rest of ``tests/``, ``tools/``, ``scripts/`` and ``ci/``
is outside the scope.

Stated limits: canon names no symbol for either helper, so each proof is as
strong as its predicate. Predicate 1 follows values within one function (or
the module's top-level statements) and through helpers defined in the same
module, not across modules or through containers, and sees a UID value only
under a name its pattern matches. "No fallback and no selector" belongs to the
switch (WU-PR-09). Each guard is shown failing on a constructed positive in a
temporary root and passing a clean one.
"""
from __future__ import annotations

import ast
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCOPE_DIRECTORIES = ("adapter", "engine", "presenter")
REMOVED_FILES = (
    "engine/compat/ts_v0.py",
    "engine/compat/type_strategy_v0.py",
    "scripts/hdctl.clean.py",
    "scripts/hdctl.backup.py",
)
REMOVED_MODULES = ("engine.compat.ts_v0", "engine.compat.type_strategy_v0")

UID_NAME = re.compile(r"(?:^|_)(?:uid|(?:user|person|canonical_person)_?id|person_?uid)(?:_|$)", re.IGNORECASE)
SCORE_NAME = re.compile(r"(?:^|_)(?:score|band)s?(?:_|$)", re.IGNORECASE)
BAND_LITERALS = frozenset({"Cool", "Open", "Warm", "Glow"})
HASH_MODULES = frozenset({"hashlib", "zlib", "binascii"})
HASH_NAMES = frozenset({
    "sha256", "sha1", "md5", "sha512", "sha384", "sha224", "blake2b", "blake2s", "crc32", "adler32", "hash",
})


# --------------------------------------------------------------------------- scope

def _inv5_closure() -> set[Path]:
    spec = importlib.util.spec_from_file_location(
        "_hde_epic043_inv5_closure", ROOT / "tests" / "m10_v2" / "test_v2_unreachable_from_production.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return set(module._static_closure().values())


def production_scope(root: Path, closure: set[Path] = frozenset()) -> list[Path]:
    """Every ``.py`` under the three production directories of ``root``, plus ``closure``."""
    files = {
        path
        for directory in SCOPE_DIRECTORIES
        for path in root.joinpath(directory).rglob("*.py")
        if "__pycache__" not in path.parts
    }
    return sorted(files | set(closure))


# --------------------------------------------------------------- predicate 1: UID hash

def _uid_reference(node: ast.AST) -> bool:
    for item in ast.walk(node):
        if isinstance(item, ast.Name):
            name = item.id
        elif isinstance(item, ast.Attribute):
            name = item.attr
        elif isinstance(item, ast.Constant) and isinstance(item.value, str) and item.value.isidentifier():
            name = item.value
        else:
            continue
        if UID_NAME.search(name):
            return True
    return False


def _targets(node: ast.AST) -> list[ast.AST]:
    if isinstance(node, ast.Assign):
        return list(node.targets)
    if isinstance(node, (ast.AugAssign, ast.AnnAssign, ast.NamedExpr)):
        return [node.target]
    return []


class _Unit:
    """UID-derived flow inside one function, lambda or module top level."""

    def __init__(self, node: ast.AST, helpers: frozenset[str]) -> None:
        self.nodes = list(ast.walk(node))
        self.helpers = helpers
        self.tainted: set[str] = set()
        changed = True
        while changed:
            changed = False
            for item in self.nodes:
                value = getattr(item, "value", None)
                if _targets(item) and value is not None and self.derived(value):
                    for target in _targets(item):
                        for name in ast.walk(target):
                            if isinstance(name, ast.Name) and name.id not in self.tainted:
                                self.tainted.add(name.id)
                                changed = True

    def is_hash_call(self, node: ast.AST) -> bool:
        if not isinstance(node, ast.Call):
            return False
        function = node.func
        if isinstance(function, ast.Attribute) and isinstance(function.value, ast.Name):
            return function.value.id in HASH_MODULES
        return isinstance(function, ast.Name) and (function.id in HASH_NAMES or function.id in self.helpers)

    def derived(self, node: ast.AST) -> bool:
        for item in ast.walk(node):
            if self.is_hash_call(item):
                arguments = [*item.args, *(keyword.value for keyword in item.keywords)]
                if any(_uid_reference(argument) for argument in arguments):
                    return True
                if isinstance(item.func, ast.Name) and item.func.id in self.helpers and any(
                    self.derived(argument) for argument in arguments
                ):
                    return True
            if isinstance(item, ast.Name) and item.id in self.tainted:
                return True
        return False

    def has_sink(self, function_name: str) -> bool:
        for item in self.nodes:
            if (
                isinstance(item, ast.BinOp) and isinstance(item.op, ast.Mod)
                and isinstance(item.right, ast.Constant) and type(item.right.value) is int
                and self.derived(item.left)
            ):
                return True
            value = getattr(item, "value", None)
            if _targets(item) and value is not None and self.derived(value):
                for target in _targets(item):
                    for name in ast.walk(target):
                        label = name.id if isinstance(name, ast.Name) else getattr(name, "attr", None)
                        if isinstance(label, str) and SCORE_NAME.search(label):
                            return True
            if isinstance(item, ast.Return) and item.value is not None and SCORE_NAME.search(function_name):
                if self.derived(item.value):
                    return True
            if isinstance(item, ast.keyword) and item.arg and SCORE_NAME.search(item.arg) and self.derived(item.value):
                return True
            if isinstance(item, ast.Dict):
                for key, mapped in zip(item.keys, item.values):
                    if (
                        isinstance(key, ast.Constant) and isinstance(key.value, str)
                        and SCORE_NAME.search(key.value) and self.derived(mapped)
                    ):
                        return True
            if isinstance(item, (ast.If, ast.IfExp)) and self.derived(item.test):
                if any(isinstance(node, ast.Constant) and node.value in BAND_LITERALS for node in ast.walk(item)):
                    return True
        return False

    def returns_derived(self) -> bool:
        return any(
            isinstance(item, ast.Return) and item.value is not None
            and (self.derived(item.value) or any(self.is_hash_call(node) for node in ast.walk(item.value)))
            for item in self.nodes
        )


def _functions(tree: ast.Module) -> list[ast.AST]:
    return [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda))]


def _module_level(tree: ast.Module) -> ast.Module:
    body = [node for node in tree.body if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
    return ast.Module(body=body, type_ignores=[])


def uid_hash_helpers(tree: ast.Module) -> frozenset[str]:
    """Module-local functions with a UID-named parameter whose return is UID-derived or a hash."""
    helpers = set()
    for function in _functions(tree):
        if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if any(UID_NAME.search(argument.arg) for argument in ast.walk(function.args) if isinstance(argument, ast.arg)):
            if _Unit(function, frozenset()).returns_derived():
                helpers.add(function.name)
    return frozenset(helpers)


def uid_hash_hits(paths: list[Path], root: Path) -> list[tuple[str, str]]:
    """Predicate 1: units in which a hash of a UID value reaches a score or band."""
    hits = []
    for path in paths:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        helpers = uid_hash_helpers(tree)
        for unit in [_module_level(tree), *_functions(tree)]:
            name = getattr(unit, "name", "<module>" if isinstance(unit, ast.Module) else "<lambda>")
            if _Unit(unit, helpers).has_sink(name):
                hits.append((path.relative_to(root).as_posix(), name))
    return hits


def uid_and_hash_without_flow(path: Path, function_name: str) -> bool:
    """True when the named function holds a UID reference and a hash call but no hit."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    function = next(
        node for node in _functions(tree) if getattr(node, "name", None) == function_name
    )
    unit = _Unit(function, uid_hash_helpers(tree))
    has_uid = _uid_reference(function)
    has_hash = any(unit.is_hash_call(node) for node in ast.walk(function))
    return has_uid and has_hash and not unit.has_sink(function_name)


# ------------------------------------------------------ predicate 2: compromise helper

def compromise_hits(paths: list[Path], root: Path) -> list[tuple[str, str]]:
    """Predicate 2: a ``def`` or ``class`` named with ``compromise``, or a module so named."""
    hits = []
    for path in paths:
        relative = path.relative_to(root).as_posix()
        if "compromise" in path.stem.lower():
            hits.append((relative, "<module>"))
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and "compromise" in node.name.lower():
                hits.append((relative, node.name))
    return hits


# --------------------------------------------------- predicate 3: removed-module imports

def removed_import_hits(paths: list[Path], root: Path) -> list[tuple[str, str]]:
    """Predicate 3: an import of a removed module, relative imports resolved, or its dotted name."""
    hits = []
    for path in paths:
        relative = path.relative_to(root)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            names: list[str] = []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                base = node.module or ""
                if node.level:
                    package = list(relative.with_suffix("").parts[:-1])
                    if node.level > 1:
                        package = package[: len(package) - (node.level - 1)]
                    base = ".".join(package + ([node.module] if node.module else []))
                names = [base, *(f"{base}.{alias.name}" for alias in node.names)]
            elif isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value in REMOVED_MODULES:
                names = [node.value]
            for name in names:
                if any(name == removed or name.startswith(removed + ".") for removed in REMOVED_MODULES):
                    hits.append((relative.as_posix(), name))
    return hits


# --------------------------------------------------------------------------- tests

def test_the_removed_files_are_absent() -> None:
    assert [path for path in REMOVED_FILES if ROOT.joinpath(path).exists()] == []


def test_scope_contains_the_inv5_closure() -> None:
    closure = _inv5_closure()
    files = set(production_scope(ROOT, closure))
    assert closure <= files
    for anchor in (
        "engine/compat/compute.py",
        "engine/compat/ordering.py",
        "adapter/http_reader.py",
        "presenter/reader_v1/emitter.py",
        "tools/config/artifacts.py",
    ):
        assert ROOT / anchor in files, anchor


def test_no_production_module_imports_a_removed_module() -> None:
    assert removed_import_hits(production_scope(ROOT, _inv5_closure()), ROOT) == []


def test_no_uid_hash_scorer_in_production() -> None:
    assert uid_hash_hits(production_scope(ROOT, _inv5_closure()), ROOT) == []
    # A UID-keyed ordering hash is not UID-hash scoring: the predicate keys on a score or band.
    assert uid_and_hash_without_flow(ROOT / "engine" / "compat" / "ordering.py", "normalize_pair")


def test_no_numeric_gate_compromise_helper_in_production() -> None:
    assert compromise_hits(production_scope(ROOT, _inv5_closure()), ROOT) == []


CLEAN_MODULE = """import hashlib


def cache_key(person_uid):
    return "k:" + hashlib.sha256(person_uid.encode()).hexdigest()
"""

POSITIVE_MODULE = """import hashlib
from engine.compat import ts_v0


def score_for(user_id):
    return int(hashlib.sha256(user_id.encode()).hexdigest(), 16) % 100


def _digest(uid):
    return hashlib.sha256(uid.encode()).hexdigest()


def score(person):
    return int(_digest(person["uid"]), 16) % 100


def numeric_gate_compromise(a, b):
    return (a + b) // 2
"""

NEGATIVE_PATTERNS = {
    "ordering_like.py": (
        "import hashlib\n\ndef normalize(a, b):\n"
        "    ha = hashlib.sha256(a['person_uid'].encode()).hexdigest()\n    return (a, b) if ha <= 'm' else (b, a)\n"
    ),
    "golden_like.py": (
        "import hashlib\n\ndef run(result, party):\n    preimage = {'k': result['band']}\n"
        "    return {'person_uid': party.uid, 'score': result['score'],"
        " 'h': hashlib.sha256(repr(preimage).encode()).hexdigest()}\n"
    ),
}


def test_each_guard_fails_on_a_constructed_positive_and_passes_a_clean_root(tmp_path: Path) -> None:
    clean = tmp_path / "clean"
    clean.joinpath("engine").mkdir(parents=True)
    clean.joinpath("engine", "keys.py").write_text(CLEAN_MODULE, encoding="utf-8")
    positive = tmp_path / "positive"
    positive.joinpath("engine").mkdir(parents=True)
    positive.joinpath("engine", "legacy.py").write_text(POSITIVE_MODULE, encoding="utf-8")

    clean_files = production_scope(clean)
    assert removed_import_hits(clean_files, clean) == []
    assert uid_hash_hits(clean_files, clean) == []
    assert compromise_hits(clean_files, clean) == []

    positive_files = production_scope(positive)
    assert removed_import_hits(positive_files, positive) == [("engine/legacy.py", "engine.compat.ts_v0")]
    assert sorted(name for _path, name in uid_hash_hits(positive_files, positive)) == ["score", "score_for"]
    assert compromise_hits(positive_files, positive) == [("engine/legacy.py", "numeric_gate_compromise")]

    negative = tmp_path / "negative"
    negative.joinpath("engine").mkdir(parents=True)
    for name, source in NEGATIVE_PATTERNS.items():
        negative.joinpath("engine", name).write_text(source, encoding="utf-8")
    assert uid_hash_hits(production_scope(negative), negative) == []
