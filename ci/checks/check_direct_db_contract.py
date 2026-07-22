#!/usr/bin/env python3
"""Fail closed if active source reintroduces a retired DB transport."""
from __future__ import annotations

import ast
import json
import subprocess
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED_PREFIXES = (
    "audit/",
    "artifacts/",
    "docs/crd/",
    "docs/plans/",
    "docs/pfcanon/",
    "docs/design/",
    "docs/adr/",
    "handoff/",
    "tests/",
    "codex/out/",
    "notes/",
    "build/",
    "dist/",
    "*.egg-info/",
)
TEXT_SUFFIXES = {".py", ".md", ".yml", ".yaml", ".sh", ".txt"}
RETIRED_PATHS = (
    "engine/db/providers/bridge_provider.py",
    "scripts/db_bridge/capture_introspection.py",
    "scripts/ops/hde_epic038_ops01r.py",
    "tools/evidence/hde_epic038_ops01_v5.py",
    "tools/evidence/generate_db_bridge_parity.py",
    "ci/checks/check_bridge_consistency.py",
)
FORBIDDEN_SYMBOLS = (
    "BridgeProvider",
    "BridgeUnavailable",
    "BridgeUnsupported",
    "bridge_factory",
    "generate_db_bridge_parity",
    "check_bridge_consistency",
    "hde_epic038_ops01r",
    "hde_epic038_ops01_v5",
)
FORBIDDEN_ACTIVE_PATH_TEXT = (
    "engine.db.providers.bridge_provider",
    "scripts/db_bridge/",
    "artifacts/db_bridge/",
)
RETIRED_KEYS = (
    "DB_ALLOW_BRIDGE_IN_PROD",
    "DB_BRIDGE_URL",
    "DB_FORCE_BRIDGE",
)
_CANONICAL_ADAPTER_MODULE_ALIAS = ("__canonical_engine_db_adapter_module__",)
REFUSAL_CONTEXT_WORDS = (
    "retired",
    "refusal",
    "refuse",
    "absent",
    "deny",
    "deprecated",
    "historical",
    "nonclaim",
    "roster",
    "required_absent",
    "forbid",
    "prohibit",
    "rejected",
    "removed",
    "unset",
)
ACTIVE_GUIDANCE_WORDS = (
    "set ",
    "export ",
    "configure",
    "use ",
    "run ",
    "fallback",
    "endpoint",
    "http",
    "request",
)
EXPLICIT_NEGATION_PHRASES = (
    "must not",
    "do not",
    "shall not",
    "may not",
    "never ",
    "cannot",
    "can't",
    "not set",
    "not export",
    "not configure",
    "not configured",
    "not use",
    "not run",
    "no longer",
    "required_absent",
    "required absent",
    "forbidden",
    "prohibited",
    "rejected",
)
HISTORICAL_ONLY_PHRASES = (
    "historical retained",
    "retained historical",
    "historical evidence",
    "historical record",
    "historical nonclaim",
    "historical non-claim",
    "not current",
)
HTTP_MARKERS = ("requests.", "urllib.request", "httpx.", "urlopen", "http://", "https://")
HISTORICAL_READERS = {
    "tools/evidence/update_evidence_index.py",
    "tools/evidence/run_sanity_pipeline.py",
}
HISTORICAL_REFERENCE_DOCS = {
    "docs/EVIDENCE_INDEX.md",
    "docs/INDEX.md",
}
MANDATORY_MARKERS = {
    "engine/db/adapter.py": (
        "RETIRED_DB_TRANSPORT_KEYS",
        "retired_db_transport_keys_present",
        "def readonly_tx",
    ),
    "engine/db/providers/psycopg_provider.py": (
        "SET TRANSACTION READ ONLY",
        "validate_readonly_statements",
        "conn.rollback()",
    ),
    "scripts/ops/hde_epic038_ops03.py": (
        "ORDERED_QUERY_IDS",
        "expected_argv",
        "authorization_bytes_changed",
    ),
    "tools/evidence/hde_epic038_ops03.py": (
        "Draft202012Validator",
        "validate_retained_text_safety",
        "_checksums_valid",
    ),
    "tools/evidence/generate_hde_epic038_direct_db_selection.py": (
        "hde_epic038.direct_db_selection.v1",
        "validate_contract",
        "retired_keys_fail_before_provider_attempt",
    ),
    "scripts/db/_util.py": ("DBAccess.for_current_env()",),
    "scripts/db/capture_epic011_posture.py": (
        "direct PostgreSQL provider required",
        "artifacts/db/ddl_fingerprint.json",
        "artifacts/db/boundary_view.readonly.proof.txt",
    ),
    "scripts/db_adapter/capture_adapter_introspection.py": (
        "DBAccess.for_current_env()",
        "direct PostgreSQL provider required",
    ),
    "scripts/ops/capture_rails_open_scope.py": (
        "capture_adapter_introspection.py",
        "provider: psycopg",
    ),
}
SCHEMAS = (
    "schemas/hde_epic038_direct_db_selection.v1.json",
    "schemas/hde_epic038_ops03_authorization.v1.json",
    "schemas/hde_epic038_ops03_db_posture_summary.v1.json",
    "schemas/hde_epic038_ops03_env_presence.v1.json",
    "schemas/hde_epic038_ops03_failure_receipt.v1.json",
    "schemas/hde_epic038_ops03_nonclaims.v1.json",
    "schemas/hde_epic038_ops03_result_summary.v1.json",
    "schemas/hde_epic038_ops03_validation_receipt.v1.json",
)



def _git_tracked_files(root: Path) -> tuple[Path, ...]:
    try:
        result = subprocess.run(["git", "ls-files", "-c", "-m", "-o", "--exclude-standard"], cwd=root, check=True, capture_output=True, text=True)
    except Exception:
        return tuple(path for path in root.rglob("*") if path.is_file())
    return tuple(root / line for line in result.stdout.splitlines() if line.strip())


def _line_refusal_only(line: str) -> bool:
    lowered = line.lower()
    if not any(word in lowered for word in REFUSAL_CONTEXT_WORDS):
        return False
    if not any(word in lowered for word in ACTIVE_GUIDANCE_WORDS):
        return True
    return any(
        phrase in lowered
        for phrase in (*EXPLICIT_NEGATION_PHRASES, *HISTORICAL_ONLY_PHRASES)
    )


def _is_os_module(node: ast.AST, os_names: set[str]) -> bool:
    return isinstance(node, ast.Name) and node.id in os_names


def _is_environ_mapping(
    node: ast.AST, os_names: set[str], environ_names: set[str]
) -> bool:
    return (
        isinstance(node, ast.Name)
        and node.id in environ_names
        or isinstance(node, ast.Attribute)
        and _is_os_module(node.value, os_names)
        and node.attr == "environ"
    )


def _is_environ_source(
    node: ast.AST, os_names: set[str], environ_names: set[str]
) -> bool:
    if _is_environ_mapping(node, os_names, environ_names):
        return True
    if not isinstance(node, ast.Call):
        return False
    func = node.func
    if (
        isinstance(func, ast.Attribute)
        and func.attr == "copy"
        and _is_environ_source(func.value, os_names, environ_names)
    ):
        return True
    return (
        isinstance(func, ast.Name)
        and func.id == "dict"
        and bool(node.args)
        and _is_environ_source(node.args[0], os_names, environ_names)
    )


def _is_getenv_reader(
    node: ast.AST, os_names: set[str], getenv_names: set[str]
) -> bool:
    return (
        isinstance(node, ast.Name)
        and node.id in getenv_names
        or isinstance(node, ast.Attribute)
        and node.attr == "getenv"
        and _is_os_module(node.value, os_names)
    )


def _target_bindings(
    target: ast.AST, value: ast.AST
) -> tuple[tuple[str, ast.AST], ...]:
    if isinstance(target, ast.Name):
        return ((target.id, value),)
    if (
        isinstance(target, (ast.List, ast.Tuple))
        and isinstance(value, (ast.List, ast.Tuple))
        and len(target.elts) == len(value.elts)
    ):
        return tuple(
            binding
            for item_target, item_value in zip(target.elts, value.elts)
            for binding in _target_bindings(item_target, item_value)
        )
    return ()


def _assignment_bindings(node: ast.AST) -> tuple[tuple[str, ast.AST], ...]:
    if isinstance(node, ast.Assign):
        return tuple(
            binding
            for target in node.targets
            for binding in _target_bindings(target, node.value)
        )
    if isinstance(node, ast.AnnAssign) and node.value is not None:
        return _target_bindings(node.target, node.value)
    if isinstance(node, ast.NamedExpr):
        return _target_bindings(node.target, node.value)
    return ()


def _literal_string_tuple(node: ast.AST) -> tuple[str, ...] | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return (node.value,)
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        values: list[str] = []
        for item in node.elts:
            if not isinstance(item, ast.Constant) or not isinstance(item.value, str):
                return None
            values.append(item.value)
        return tuple(values)
    return None


def _retired_roster_import_names(node: ast.AST) -> tuple[str, ...]:
    if not (
        isinstance(node, ast.ImportFrom)
        and node.level == 0
        and node.module == "engine.db.adapter"
    ):
        return ()
    return tuple(
        imported.asname or imported.name
        for imported in node.names
        if imported.name == "RETIRED_DB_TRANSPORT_KEYS"
    )


def _canonical_adapter_import_names(node: ast.AST) -> tuple[str, ...]:
    if isinstance(node, ast.Import):
        return tuple(
            imported.asname
            for imported in node.names
            if imported.name == "engine.db.adapter" and imported.asname is not None
        )
    if not (
        isinstance(node, ast.ImportFrom)
        and node.level == 0
        and node.module == "engine.db"
    ):
        return ()
    return tuple(
        imported.asname or imported.name
        for imported in node.names
        if imported.name == "adapter"
    )


def _constant_string_bindings(tree: ast.Module) -> dict[str, tuple[str, ...]]:
    """Return module-scope string aliases without leaking nested local bindings."""
    aliases: dict[str, tuple[str, ...]] = {
        name: RETIRED_KEYS
        for node in tree.body
        for name in _retired_roster_import_names(node)
    }
    aliases.update(
        {
            name: _CANONICAL_ADAPTER_MODULE_ALIAS
            for node in tree.body
            for name in _canonical_adapter_import_names(node)
        }
    )
    while True:
        previous = dict(aliases)
        for node in tree.body:
            for local_name, value in _assignment_bindings(node):
                resolved = _resolve_string_values(value, aliases)
                if resolved:
                    aliases[local_name] = resolved
        if aliases == previous:
            return aliases


def _constant_int(node: ast.AST) -> int | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, (ast.UAdd, ast.USub))
        and isinstance(node.operand, ast.Constant)
        and isinstance(node.operand.value, int)
    ):
        value = node.operand.value
        return value if isinstance(node.op, ast.UAdd) else -value
    return None


def _resolve_string_values(
    node: ast.AST, aliases: dict[str, tuple[str, ...]]
) -> tuple[str, ...] | None:
    literal = _literal_string_tuple(node)
    if literal is not None:
        return literal
    if isinstance(node, ast.NamedExpr):
        return _resolve_string_values(node.value, aliases)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _resolve_string_values(node.left, aliases)
        right = _resolve_string_values(node.right, aliases)
        if left is not None and right is not None and len(left) == len(right) == 1:
            return (left[0] + right[0],)
        return None
    if isinstance(node, ast.JoinedStr):
        parts: list[str] = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
                continue
            if not (
                isinstance(value, ast.FormattedValue)
                and value.conversion == -1
                and value.format_spec is None
            ):
                return None
            resolved = _resolve_string_values(value.value, aliases)
            if resolved is None or len(resolved) != 1:
                return None
            parts.append(resolved[0])
        return ("".join(parts),)
    if isinstance(node, ast.Name):
        return aliases.get(node.id)
    if isinstance(node, ast.Attribute) and node.attr == "RETIRED_DB_TRANSPORT_KEYS":
        if _dotted_name(node.value) == "engine.db.adapter":
            return RETIRED_KEYS
        if _resolve_string_values(node.value, aliases) == _CANONICAL_ADAPTER_MODULE_ALIAS:
            return RETIRED_KEYS
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"frozenset", "iter", "list", "reversed", "set", "sorted", "tuple"}
        and len(node.args) == 1
    ):
        return _resolve_string_values(node.args[0], aliases)
    if isinstance(node, ast.Subscript):
        source = _resolve_string_values(node.value, aliases)
        if source is None:
            return None
        index = _constant_int(node.slice)
        if index is not None and -len(source) <= index < len(source):
            return (source[index],)
        if isinstance(node.slice, ast.Slice):
            bounds: list[int | None] = []
            for bound in (node.slice.lower, node.slice.upper, node.slice.step):
                if bound is None:
                    bounds.append(None)
                    continue
                resolved_bound = _constant_int(bound)
                if resolved_bound is None:
                    return tuple(value for value in source if value in RETIRED_KEYS) or None
                bounds.append(resolved_bound)
            try:
                return source[slice(*bounds)]
            except ValueError:
                return tuple(value for value in source if value in RETIRED_KEYS) or None
        return tuple(value for value in source if value in RETIRED_KEYS) or None
    return None


def _contains_retired_key(node: ast.AST, aliases: dict[str, tuple[str, ...]]) -> bool:
    values = _resolve_string_values(node, aliases)
    if values is None:
        return False
    return any(value in RETIRED_KEYS for value in values)


def _target_names(target: ast.AST) -> tuple[str, ...]:
    if isinstance(target, ast.Name):
        return (target.id,)
    if isinstance(target, ast.Starred):
        return _target_names(target.value)
    if isinstance(target, (ast.List, ast.Tuple)):
        return tuple(name for item in target.elts for name in _target_names(item))
    return ()


def _pattern_alias_bindings(
    target: ast.AST,
    value: ast.AST,
    aliases: dict[str, tuple[str, ...]],
) -> dict[str, tuple[str, ...]]:
    if isinstance(target, ast.Name):
        resolved = _resolve_string_values(value, aliases)
        return {target.id: resolved} if resolved else {}
    if isinstance(target, ast.Starred):
        return _pattern_alias_bindings(target.value, value, aliases)
    if (
        isinstance(target, (ast.List, ast.Tuple))
        and isinstance(value, (ast.List, ast.Tuple))
        and len(target.elts) == len(value.elts)
    ):
        bindings: dict[str, tuple[str, ...]] = {}
        for item_target, item_value in zip(target.elts, value.elts):
            bindings.update(_pattern_alias_bindings(item_target, item_value, aliases))
        return bindings
    return {}


def _loop_target_alias_bindings(
    target: ast.AST,
    iterable: ast.AST,
    aliases: dict[str, tuple[str, ...]],
) -> dict[str, tuple[str, ...]]:
    if isinstance(iterable, ast.Call) and isinstance(iterable.func, ast.Name):
        if (
            iterable.func.id in {"frozenset", "iter", "list", "reversed", "set", "sorted", "tuple"}
            and len(iterable.args) == 1
        ):
            return _loop_target_alias_bindings(target, iterable.args[0], aliases)
        if (
            iterable.func.id == "enumerate"
            and iterable.args
            and isinstance(target, (ast.List, ast.Tuple))
            and len(target.elts) == 2
        ):
            return _loop_target_alias_bindings(
                target.elts[1], iterable.args[0], aliases
            )
        if (
            iterable.func.id == "zip"
            and isinstance(target, (ast.List, ast.Tuple))
            and len(target.elts) == len(iterable.args)
        ):
            merged: dict[str, tuple[str, ...]] = {}
            for item_target, item_iterable in zip(target.elts, iterable.args):
                bindings = _loop_target_alias_bindings(
                    item_target, item_iterable, aliases
                )
                for name, values in bindings.items():
                    combined = list(merged.get(name, ()))
                    for value in values:
                        if value not in combined:
                            combined.append(value)
                    merged[name] = tuple(combined)
            return merged
    if isinstance(target, ast.Name):
        resolved = _resolve_string_values(iterable, aliases)
        return {target.id: resolved} if resolved else {}
    if not isinstance(iterable, (ast.List, ast.Tuple, ast.Set)):
        return {}
    merged: dict[str, tuple[str, ...]] = {}
    for item in iterable.elts:
        for name, values in _pattern_alias_bindings(target, item, aliases).items():
            combined = list(merged.get(name, ()))
            for value in values:
                if value not in combined:
                    combined.append(value)
            merged[name] = tuple(combined)
    return merged


def _os_symbol_aliases(tree: ast.AST) -> tuple[set[str], set[str], set[str]]:
    """Return local names bound to os, os.environ, and os.getenv."""
    os_names = {"os"}
    environ_names = {"environ"}
    getenv_names = {"getenv"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for imported in node.names:
                if imported.name == "os":
                    os_names.add(imported.asname or imported.name)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module == "os":
            for imported in node.names:
                local_name = imported.asname or imported.name
                if imported.name == "environ":
                    environ_names.add(local_name)
                elif imported.name == "getenv":
                    getenv_names.add(local_name)

    while True:
        previous = (len(os_names), len(environ_names), len(getenv_names))
        for node in ast.walk(tree):
            for local_name, value in _assignment_bindings(node):
                if _is_os_module(value, os_names):
                    os_names.add(local_name)
                elif _is_environ_source(value, os_names, environ_names):
                    environ_names.add(local_name)
                elif _is_getenv_reader(value, os_names, getenv_names):
                    getenv_names.add(local_name)
        if previous == (len(os_names), len(environ_names), len(getenv_names)):
            return os_names, environ_names, getenv_names


def _retired_env_call(
    node: ast.Call,
    os_names: set[str],
    environ_names: set[str],
    getenv_names: set[str],
    aliases: dict[str, tuple[str, ...]],
) -> bool:
    func = node.func
    is_reader = _is_getenv_reader(func, os_names, getenv_names) or (
        isinstance(func, ast.Attribute)
        and func.attr == "get"
        and _is_environ_source(func.value, os_names, environ_names)
    )
    values = [*node.args, *(keyword.value for keyword in node.keywords)]
    return is_reader and any(_contains_retired_key(value, aliases) for value in values)


def _unresolved_retired_key(
    node: ast.AST, aliases: dict[str, tuple[str, ...]]
) -> bool:
    if _contains_retired_key(node, aliases):
        return False
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return False
    if isinstance(node, ast.Name):
        lowered = node.id.lower()
        return "bridge" in lowered or "retired" in lowered
    return False


def _unresolved_env_call(
    node: ast.Call,
    os_names: set[str],
    environ_names: set[str],
    getenv_names: set[str],
    aliases: dict[str, tuple[str, ...]],
) -> bool:
    func = node.func
    is_reader = _is_getenv_reader(func, os_names, getenv_names) or (
        isinstance(func, ast.Attribute)
        and func.attr == "get"
        and _is_environ_source(func.value, os_names, environ_names)
    )
    if not is_reader:
        return False
    values = [*node.args, *(keyword.value for keyword in node.keywords)]
    if not values:
        return False
    return _unresolved_retired_key(values[0], aliases)


def _dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = _dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def _is_http_call(node: ast.Call) -> bool:
    name = _dotted_name(node.func).lower()
    if name in {
        "requests.get",
        "requests.post",
        "requests.request",
        "httpx.get",
        "httpx.post",
        "httpx.request",
        "urllib.request.urlopen",
        "urlopen",
    }:
        return True
    if not isinstance(node.func, ast.Attribute) or node.func.attr.lower() not in {
        "delete",
        "get",
        "head",
        "patch",
        "post",
        "put",
        "request",
    }:
        return False
    owner = _dotted_name(node.func.value).lower()
    return owner in {"client", "http", "http_client", "session"} or owner.startswith(
        ("httpx.", "requests.")
    )


def _retired_environ_subscript(
    node: ast.Subscript,
    os_names: set[str],
    environ_names: set[str],
    aliases: dict[str, tuple[str, ...]],
) -> bool:
    return _is_environ_source(node.value, os_names, environ_names) and _contains_retired_key(
        node.slice, aliases
    )


def _unresolved_environ_subscript(
    node: ast.Subscript,
    os_names: set[str],
    environ_names: set[str],
    aliases: dict[str, tuple[str, ...]],
) -> bool:
    return _is_environ_source(
        node.value, os_names, environ_names
    ) and _unresolved_retired_key(node.slice, aliases)


def _retired_membership_compare(
    node: ast.Compare,
    os_names: set[str],
    environ_names: set[str],
    aliases: dict[str, tuple[str, ...]],
) -> bool:
    left = node.left
    for operator, right in zip(node.ops, node.comparators):
        if (
            isinstance(operator, (ast.In, ast.NotIn))
            and _contains_retired_key(left, aliases)
            and _is_environ_source(right, os_names, environ_names)
        ):
            return True
        left = right
    return False


def _statement_scope_nodes(stmt: ast.stmt) -> tuple[ast.AST, ...]:
    """Walk one statement without descending into nested statement bodies."""
    nodes: list[ast.AST] = []

    def collect(node: ast.AST) -> None:
        if isinstance(node, ast.NamedExpr):
            collect(node.value)
            nodes.append(node)
            return
        nodes.append(node)
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.stmt):
                continue
            collect(child)

    collect(stmt)
    return tuple(nodes)


def _parameter_names(arguments: ast.arguments) -> set[str]:
    names = {
        argument.arg
        for argument in [
            *arguments.posonlyargs,
            *arguments.args,
            *arguments.kwonlyargs,
        ]
    }
    if arguments.vararg is not None:
        names.add(arguments.vararg.arg)
    if arguments.kwarg is not None:
        names.add(arguments.kwarg.arg)
    return names


def _default_bindings(
    arguments: ast.arguments,
) -> tuple[tuple[str, ast.AST], ...]:
    positional = [*arguments.posonlyargs, *arguments.args]
    positional_bindings = tuple(
        (parameter.arg, default)
        for parameter, default in zip(
            positional[-len(arguments.defaults) :] if arguments.defaults else (),
            arguments.defaults,
        )
    )
    keyword_bindings = tuple(
        (parameter.arg, default)
        for parameter, default in zip(arguments.kwonlyargs, arguments.kw_defaults)
        if default is not None
    )
    return (*positional_bindings, *keyword_bindings)


def _python_retired_consumption(text: str) -> tuple[int, ...]:
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return ()
    os_names, environ_names, getenv_names = _os_symbol_aliases(tree)
    lines: set[int] = set()

    def check_node(
        node: ast.AST,
        aliases: dict[str, tuple[str, ...]],
        tainted_names: set[str],
    ) -> None:
        if isinstance(node, ast.Call):
            if _retired_env_call(node, os_names, environ_names, getenv_names, aliases):
                lines.add(node.lineno)
            if _unresolved_env_call(node, os_names, environ_names, getenv_names, aliases):
                lines.add(node.lineno)
            if _is_http_call(node) and any(
                _contains_retired_key(arg, aliases)
                or (isinstance(arg, ast.Name) and arg.id in tainted_names)
                for arg in [*node.args, *(keyword.value for keyword in node.keywords)]
            ):
                lines.add(node.lineno)
        if isinstance(node, ast.Compare) and _retired_membership_compare(
            node, os_names, environ_names, aliases
        ):
            lines.add(node.lineno)
        if isinstance(node, ast.Subscript) and (
            _retired_environ_subscript(node, os_names, environ_names, aliases)
            or _unresolved_environ_subscript(node, os_names, environ_names, aliases)
        ):
            lines.add(node.lineno)

    def merge_states(
        states: list[tuple[dict[str, tuple[str, ...]], set[str]]],
    ) -> tuple[dict[str, tuple[str, ...]], set[str]]:
        merged_aliases: dict[str, tuple[str, ...]] = {}
        merged_tainted: set[str] = set()
        for state_aliases, state_tainted in states:
            merged_tainted.update(state_tainted)
            for name, values in state_aliases.items():
                combined = list(merged_aliases.get(name, ()))
                for value in values:
                    if value not in combined:
                        combined.append(value)
                merged_aliases[name] = tuple(combined)
        return merged_aliases, merged_tainted

    def replace_state(
        aliases: dict[str, tuple[str, ...]],
        tainted_names: set[str],
        state: tuple[dict[str, tuple[str, ...]], set[str]],
    ) -> None:
        merged_aliases, merged_tainted = state
        aliases.clear()
        aliases.update(merged_aliases)
        tainted_names.clear()
        tainted_names.update(merged_tainted)

    def assignment_value_is_tainted(
        value: ast.AST,
        aliases: dict[str, tuple[str, ...]],
        tainted_names: set[str],
    ) -> bool:
        if isinstance(value, ast.Name) and value.id in tainted_names:
            return True
        if isinstance(value, ast.Call):
            return _retired_env_call(
                value, os_names, environ_names, getenv_names, aliases
            ) or _unresolved_env_call(
                value, os_names, environ_names, getenv_names, aliases
            )
        if isinstance(value, ast.Subscript):
            return _retired_environ_subscript(
                value, os_names, environ_names, aliases
            ) or _unresolved_environ_subscript(
                value, os_names, environ_names, aliases
            )
        return False

    def bind_iteration_target(
        target: ast.AST,
        iterable: ast.AST,
        aliases: dict[str, tuple[str, ...]],
        tainted_names: set[str],
    ) -> None:
        bindings = _loop_target_alias_bindings(target, iterable, aliases)
        for target_name in _target_names(target):
            if target_name in bindings:
                aliases[target_name] = bindings[target_name]
            else:
                aliases.pop(target_name, None)
            tainted_names.discard(target_name)

    def scan_expression(
        node: ast.AST,
        aliases: dict[str, tuple[str, ...]],
        tainted_names: set[str],
        named_expression_updates: list[
            tuple[str, tuple[str, ...] | None, bool]
        ],
    ) -> None:
        if isinstance(node, ast.Lambda):
            for _, default in _default_bindings(node.args):
                scan_expression(
                    default, aliases, tainted_names, named_expression_updates
                )
            lambda_aliases = dict(aliases)
            lambda_tainted = set(tainted_names)
            for parameter_name in _parameter_names(node.args):
                lambda_aliases.pop(parameter_name, None)
                lambda_tainted.discard(parameter_name)
            for parameter_name, default in _default_bindings(node.args):
                resolved = _resolve_string_values(default, aliases)
                if resolved:
                    lambda_aliases[parameter_name] = resolved
                if assignment_value_is_tainted(default, aliases, tainted_names):
                    lambda_tainted.add(parameter_name)
            scan_expression(
                node.body, lambda_aliases, lambda_tainted, []
            )
            return

        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            comprehension_aliases = dict(aliases)
            comprehension_tainted = set(tainted_names)
            for generator in node.generators:
                scan_expression(
                    generator.iter,
                    comprehension_aliases,
                    comprehension_tainted,
                    named_expression_updates,
                )
                bind_iteration_target(
                    generator.target,
                    generator.iter,
                    comprehension_aliases,
                    comprehension_tainted,
                )
                for condition in generator.ifs:
                    scan_expression(
                        condition,
                        comprehension_aliases,
                        comprehension_tainted,
                        named_expression_updates,
                    )
            if isinstance(node, ast.DictComp):
                scan_expression(
                    node.key,
                    comprehension_aliases,
                    comprehension_tainted,
                    named_expression_updates,
                )
                scan_expression(
                    node.value,
                    comprehension_aliases,
                    comprehension_tainted,
                    named_expression_updates,
                )
            else:
                scan_expression(
                    node.elt,
                    comprehension_aliases,
                    comprehension_tainted,
                    named_expression_updates,
                )
            return

        if isinstance(node, ast.NamedExpr):
            scan_expression(
                node.value, aliases, tainted_names, named_expression_updates
            )
            check_node(node, aliases, tainted_names)
            for local_name, value in _assignment_bindings(node):
                value_tainted = assignment_value_is_tainted(
                    value, aliases, tainted_names
                )
                if value_tainted:
                    tainted_names.add(local_name)
                else:
                    tainted_names.discard(local_name)
                resolved = _resolve_string_values(value, aliases)
                if resolved:
                    aliases[local_name] = resolved
                else:
                    aliases.pop(local_name, None)
                named_expression_updates.append(
                    (local_name, resolved, value_tainted)
                )
            return

        check_node(node, aliases, tainted_names)
        for local_name, value in _assignment_bindings(node):
            if assignment_value_is_tainted(value, aliases, tainted_names):
                tainted_names.add(local_name)
            else:
                tainted_names.discard(local_name)
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.stmt):
                continue
            scan_expression(
                child, aliases, tainted_names, named_expression_updates
            )

    def scan_statements(
        statements: list[ast.stmt],
        aliases: dict[str, tuple[str, ...]],
        tainted_names: set[str],
    ) -> None:
        for stmt in statements:
            statement_aliases = dict(aliases)
            statement_tainted = set(tainted_names)
            named_expression_updates: list[
                tuple[str, tuple[str, ...] | None, bool]
            ] = []
            scan_expression(
                stmt,
                statement_aliases,
                statement_tainted,
                named_expression_updates,
            )
            for local_name, value in _assignment_bindings(stmt):
                resolved = _resolve_string_values(value, aliases)
                if resolved:
                    aliases[local_name] = resolved
                else:
                    aliases.pop(local_name, None)
                if local_name in statement_tainted:
                    tainted_names.add(local_name)
                else:
                    tainted_names.discard(local_name)
            for local_name, resolved, value_tainted in named_expression_updates:
                if resolved:
                    aliases[local_name] = resolved
                else:
                    aliases.pop(local_name, None)
                if value_tainted:
                    tainted_names.add(local_name)
                else:
                    tainted_names.discard(local_name)
            for local_name in _retired_roster_import_names(stmt):
                aliases[local_name] = RETIRED_KEYS
                tainted_names.discard(local_name)
            for local_name in _canonical_adapter_import_names(stmt):
                aliases[local_name] = _CANONICAL_ADAPTER_MODULE_ALIAS
                tainted_names.discard(local_name)
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                function_aliases = dict(aliases)
                function_tainted = set(tainted_names)
                for parameter_name in _parameter_names(stmt.args):
                    function_aliases.pop(parameter_name, None)
                    function_tainted.discard(parameter_name)
                for parameter_name, default in _default_bindings(stmt.args):
                    resolved = _resolve_string_values(default, aliases)
                    if resolved:
                        function_aliases[parameter_name] = resolved
                    if assignment_value_is_tainted(default, aliases, tainted_names):
                        function_tainted.add(parameter_name)
                scan_statements(stmt.body, function_aliases, function_tainted)
            elif isinstance(stmt, ast.ClassDef):
                scan_statements(stmt.body, dict(aliases), set(tainted_names))
            elif isinstance(stmt, (ast.For, ast.AsyncFor)):
                entry_state = (dict(aliases), set(tainted_names))
                loop_aliases = dict(aliases)
                loop_tainted = set(tainted_names)
                bind_iteration_target(
                    stmt.target, stmt.iter, loop_aliases, loop_tainted
                )
                scan_statements(stmt.body, loop_aliases, loop_tainted)
                exit_states = [entry_state, (loop_aliases, loop_tainted)]
                if stmt.orelse:
                    orelse_aliases = dict(loop_aliases)
                    orelse_tainted = set(loop_tainted)
                    scan_statements(stmt.orelse, orelse_aliases, orelse_tainted)
                    exit_states.append((orelse_aliases, orelse_tainted))
                replace_state(aliases, tainted_names, merge_states(exit_states))
            elif isinstance(stmt, ast.If):
                entry_state = (dict(aliases), set(tainted_names))
                body_aliases, body_tainted = dict(aliases), set(tainted_names)
                scan_statements(stmt.body, body_aliases, body_tainted)
                exit_states = [(body_aliases, body_tainted)]
                if stmt.orelse:
                    orelse_aliases, orelse_tainted = dict(aliases), set(tainted_names)
                    scan_statements(stmt.orelse, orelse_aliases, orelse_tainted)
                    exit_states.append((orelse_aliases, orelse_tainted))
                else:
                    exit_states.append(entry_state)
                replace_state(aliases, tainted_names, merge_states(exit_states))
            elif isinstance(stmt, ast.While):
                entry_state = (dict(aliases), set(tainted_names))
                body_aliases, body_tainted = dict(aliases), set(tainted_names)
                scan_statements(stmt.body, body_aliases, body_tainted)
                exit_states = [entry_state, (body_aliases, body_tainted)]
                if stmt.orelse:
                    orelse_aliases, orelse_tainted = dict(aliases), set(tainted_names)
                    scan_statements(stmt.orelse, orelse_aliases, orelse_tainted)
                    exit_states.append((orelse_aliases, orelse_tainted))
                replace_state(aliases, tainted_names, merge_states(exit_states))
            elif isinstance(stmt, (ast.With, ast.AsyncWith)):
                body_aliases, body_tainted = dict(aliases), set(tainted_names)
                for item in stmt.items:
                    if item.optional_vars is None:
                        continue
                    for target_name in _target_names(item.optional_vars):
                        body_aliases.pop(target_name, None)
                        body_tainted.discard(target_name)
                scan_statements(stmt.body, body_aliases, body_tainted)
                replace_state(aliases, tainted_names, (body_aliases, body_tainted))
            elif isinstance(stmt, ast.Try):
                entry_aliases, entry_tainted = dict(aliases), set(tainted_names)
                body_aliases, body_tainted = dict(aliases), set(tainted_names)
                scan_statements(stmt.body, body_aliases, body_tainted)
                if stmt.orelse:
                    scan_statements(stmt.orelse, body_aliases, body_tainted)
                exit_states = [(body_aliases, body_tainted)]
                for handler in stmt.handlers:
                    handler_aliases = dict(entry_aliases)
                    handler_tainted = set(entry_tainted)
                    if handler.name is not None:
                        handler_aliases.pop(handler.name, None)
                        handler_tainted.discard(handler.name)
                    scan_statements(handler.body, handler_aliases, handler_tainted)
                    exit_states.append((handler_aliases, handler_tainted))
                merged = merge_states(exit_states)
                if stmt.finalbody:
                    final_aliases, final_tainted = merged
                    scan_statements(stmt.finalbody, final_aliases, final_tainted)
                    merged = (final_aliases, final_tainted)
                replace_state(aliases, tainted_names, merged)
            elif isinstance(stmt, ast.Match):
                entry_state = (dict(aliases), set(tainted_names))
                exit_states = [entry_state]
                for case in stmt.cases:
                    case_aliases, case_tainted = dict(aliases), set(tainted_names)
                    scan_statements(case.body, case_aliases, case_tainted)
                    exit_states.append((case_aliases, case_tainted))
                replace_state(aliases, tainted_names, merge_states(exit_states))

    scan_statements(tree.body, _constant_string_bindings(tree), set())
    return tuple(sorted(lines))


def _python_retired_http_use(text: str) -> tuple[int, ...]:
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return ()
    lines: set[int] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not _is_http_call(node):
            continue
        segment = ast.get_source_segment(text, node) or ""
        if any(key in segment for key in RETIRED_KEYS):
            lines.add(node.lineno)
    return tuple(sorted(lines))


def _retired_key_violations(relative: str, text: str) -> list[str]:
    out: list[str] = []
    if relative.endswith(".py"):
        for line_number in _python_retired_consumption(text):
            out.append(f"{relative}:{line_number}:active_retired_key_consumption")
        for line_number in _python_retired_http_use(text):
            out.append(f"{relative}:{line_number}:retired_key_http_bridge_use")
    for line_number, line in enumerate(text.splitlines(), 1):
        if not any(key in line for key in RETIRED_KEYS):
            continue
        if any(marker in line for marker in HTTP_MARKERS):
            out.append(f"{relative}:{line_number}:retired_key_http_bridge_use")
            continue
        if relative.endswith((".md", ".txt", ".yml", ".yaml", ".sh")) and not _line_refusal_only(line):
            out.append(f"{relative}:{line_number}:retired_key_active_guidance")
    return out

def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _active(root: Path, path: Path) -> bool:
    relative = _relative(root, path)
    return (
        path.is_file()
        and path.suffix in TEXT_SUFFIXES
        and relative not in {"CHANGELOG.md", "AGENTS.md"}
        and not any(relative.startswith(prefix) for prefix in EXCLUDED_PREFIXES if not prefix.startswith("*"))
        and ".egg-info/" not in relative
    )


def scan(root: Path = ROOT) -> tuple[str, ...]:
    violations: set[str] = set()
    for relative in RETIRED_PATHS:
        if (root / relative).exists():
            violations.add(f"{relative}:retired_path_present")

    for path in _git_tracked_files(root):
        if not _active(root, path):
            continue
        relative = _relative(root, path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        if relative != "ci/checks/check_direct_db_contract.py":
            for symbol in FORBIDDEN_SYMBOLS:
                if symbol in text:
                    violations.add(f"{relative}:forbidden_symbol:{symbol}")
        if relative not in HISTORICAL_READERS and relative != "ci/checks/check_direct_db_contract.py":
            for line_number, line in enumerate(text.splitlines(), 1):
                for marker in FORBIDDEN_ACTIVE_PATH_TEXT:
                    if marker not in line:
                        continue
                    explicitly_historical = (
                        relative in HISTORICAL_REFERENCE_DOCS
                        and "historical" in line.lower()
                    )
                    if not explicitly_historical:
                        violations.add(
                            f"{relative}:{line_number}:active_retired_path:{marker}"
                        )
        if relative != "ci/checks/check_direct_db_contract.py":
            violations.update(_retired_key_violations(relative, text))

    for relative, markers in MANDATORY_MARKERS.items():
        path = root / relative
        if not path.is_file():
            violations.add(f"{relative}:mandatory_file_missing")
            continue
        text = path.read_text(encoding="utf-8", errors="strict")
        for marker in markers:
            if marker not in text:
                violations.add(f"{relative}:mandatory_marker_missing:{marker}")

    for relative in SCHEMAS:
        path = root / relative
        if not path.is_file():
            violations.add(f"{relative}:schema_missing")
            continue
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            violations.add(f"{relative}:schema_unreadable")
            continue
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            violations.add(f"{relative}:draft_2020_12_missing")
        if schema.get("additionalProperties") is not False:
            violations.add(f"{relative}:top_level_unknown_keys_allowed")
    return tuple(sorted(violations))


def main(_argv: Iterable[str] | None = None) -> int:
    violations = scan()
    if violations:
        print("\n".join(violations))
        return 1
    print("DIRECT_DB_CONTRACT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
