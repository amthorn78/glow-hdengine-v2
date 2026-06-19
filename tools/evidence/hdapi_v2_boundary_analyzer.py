"""Static boundary analyzer for EPIC034 HDAPI v2 adapter/presenter proof.

This module is intentionally independent from the evidence renderer so boundary
policy can be tested without regenerating governed artifacts.
"""
from __future__ import annotations

import ast
import hashlib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def _python_source(rel: str) -> tuple[Path, str, ast.AST]:
    path = ROOT / rel
    if not path.is_file():
        raise ValueError(f"ADAPTER_BOUNDARY_LOCUS_MISSING:{rel}")
    text = path.read_text(encoding="utf-8")
    return path, text, ast.parse(text, filename=rel)


def _call_names(tree: ast.AST) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name):
                names.add(func.id)
            elif isinstance(func, ast.Attribute):
                parts = [func.attr]
                value = func.value
                while isinstance(value, ast.Attribute):
                    parts.append(value.attr)
                    value = value.value
                if isinstance(value, ast.Name):
                    parts.append(value.id)
                names.add(".".join(reversed(parts)))
    return names


def _import_modules(tree: ast.AST) -> set[str]:
    modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module)
    return modules


def _import_aliases(tree: ast.AST) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                aliases[alias.asname or alias.name.split(".")[0]] = alias.name
        elif isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                aliases[alias.asname or alias.name] = f"{node.module}.{alias.name}"
    return aliases


def _root_name(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, ast.Attribute):
        current = current.value
    if isinstance(current, ast.Call):
        return _root_name(current.func)
    if isinstance(current, ast.Name):
        return current.id
    return None


def _attribute_chain(node: ast.AST) -> str:
    parts: list[str] = []
    current = node
    while isinstance(current, ast.Attribute):
        parts.append(current.attr)
        current = current.value
    if isinstance(current, ast.Name):
        parts.append(current.id)
    elif isinstance(current, ast.Call):
        nested = _attribute_chain(current.func)
        if nested:
            parts.append(nested)
    return ".".join(reversed(parts))


def _adapter_external_io_calls(loci: tuple[str, ...]) -> list[str]:
    findings: list[str] = []
    http_methods = {"request", "get", "post", "put", "patch", "delete", "head", "options", "urlopen", "send", "stream"}
    forbidden_modules = {"requests", "httpx", "urllib.request", "urllib3", "http.client", "aiohttp", "socket", "subprocess"}
    forbidden_calls = {
        "socket.create_connection",
        "create_connection",
        "subprocess.run",
        "subprocess.Popen",
        "subprocess.call",
        "subprocess.check_call",
        "subprocess.check_output",
        "check_call",
        "check_output",
        "os.system",
        "os.popen",
        "system",
        "popen",
    }
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        aliases = _import_aliases(tree)
        client_roots: set[str] = set()
        client_attrs: set[str] = set()
        opener_roots: set[str] = set()

        def remember_client_target(target_node: ast.AST) -> None:
            if isinstance(target_node, ast.Name):
                client_roots.add(target_node.id)
            elif isinstance(target_node, ast.Attribute):
                client_attrs.add(_attribute_chain(target_node))
                client_attrs.add(target_node.attr)

        def remember_opener_target(target_node: ast.AST) -> None:
            if isinstance(target_node, ast.Name):
                opener_roots.add(target_node.id)
            elif isinstance(target_node, ast.Attribute):
                opener_roots.add(_attribute_chain(target_node))

        def call_constructs_client(call: ast.Call) -> bool:
            ctor_chain = _attribute_chain(call.func)
            ctor_root = _root_name(call.func)
            ctor_target = aliases.get(ctor_root or "", ctor_root or "")
            return (
                ctor_target.startswith(("requests", "httpx", "urllib3", "http.client", "aiohttp"))
                and (
                    ctor_chain.endswith((".Session", ".Client", ".AsyncClient", ".PoolManager", ".HTTPConnection", ".HTTPSConnection", ".ClientSession"))
                    or ctor_target.endswith((".Session", ".Client", ".AsyncClient", ".PoolManager", ".HTTPConnection", ".HTTPSConnection", ".ClientSession"))
                )
            )

        def call_constructs_opener(call: ast.Call) -> bool:
            ctor_chain = _attribute_chain(call.func)
            ctor_root = _root_name(call.func)
            ctor_target = aliases.get(ctor_root or "", ctor_root or "")
            return ctor_target == "urllib.request.build_opener" or (ctor_target == "urllib.request" and ctor_chain.endswith(".build_opener")) or ctor_chain == "build_opener"

        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)) or not isinstance(node.value, ast.Call):
                continue
            if call_constructs_client(node.value):
                target_nodes = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target_node in target_nodes:
                    remember_client_target(target_node)
            if call_constructs_opener(node.value):
                target_nodes = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target_node in target_nodes:
                    remember_opener_target(target_node)
        for node in ast.walk(tree):
            if not isinstance(node, (ast.With, ast.AsyncWith)):
                continue
            for item in node.items:
                if isinstance(item.context_expr, ast.Call) and item.optional_vars is not None:
                    if call_constructs_client(item.context_expr):
                        remember_client_target(item.optional_vars)
                    if call_constructs_opener(item.context_expr):
                        remember_opener_target(item.optional_vars)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            chain = _attribute_chain(node.func)
            root = _root_name(node.func)
            target = aliases.get(root or "", root or "")
            attr = chain.rsplit(".", 1)[-1] if chain else ""
            target_attr = target.rsplit(".", 1)[-1] if target and chain == (root or "") else ""
            receiver = chain.rsplit(".", 1)[0] if "." in chain else root or ""
            if (target.startswith("socket") and attr in {"create_connection", "socket"}) or (target.startswith("subprocess") and attr in {"run", "Popen", "call", "check_call", "check_output"}):
                findings.append(f"{rel}:{chain}")
            elif root in client_roots and attr in http_methods:
                findings.append(f"{rel}:{chain}")
            elif (receiver in client_attrs or any(receiver.endswith(f".{client_attr}") for client_attr in client_attrs)) and attr in http_methods:
                findings.append(f"{rel}:{chain}")
            elif (root in opener_roots or receiver in opener_roots) and attr == "open":
                findings.append(f"{rel}:{chain}")
            elif target in forbidden_modules or any(target.startswith(f"{module}.") for module in forbidden_modules):
                if (
                    attr in http_methods
                    or target_attr in http_methods
                    or chain.endswith((".Client", ".AsyncClient", ".PoolManager", ".HTTPConnection", ".HTTPSConnection"))
                    or ".Client." in chain
                    or ".AsyncClient." in chain
                    or ".PoolManager." in chain
                    or ".HTTPConnection." in chain
                    or ".HTTPSConnection." in chain
                    or ".ClientSession." in chain
                ):
                    findings.append(f"{rel}:{chain}")
            elif chain in forbidden_calls or target in forbidden_calls:
                findings.append(f"{rel}:{chain}")
    return sorted(set(findings))


def _ad_hoc_json_serializers(loci: tuple[str, ...]) -> list[str]:
    """Find direct JSON serializers outside known internal vendor request/log helpers."""

    allowed_vendor_funcs = {"_append_retry_log", "_append_jsonl", "build_contract_route_request", "ingest_bodygraph"}
    allowed_log_funcs = {"_keys_only_after", "log_startup_line"}
    findings: list[str] = []
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        aliases = _import_aliases(tree)
        parents = _parent_map(tree)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            chain = _attribute_chain(node.func)
            root = _root_name(node.func)
            target = aliases.get(root or "", root or "")
            attr = chain.rsplit(".", 1)[-1] if chain else ""
            if not (
                (target in {"json", "orjson", "simplejson"} and attr in {"dump", "dumps"})
                or target in {"json.dump", "json.dumps", "orjson.dumps", "simplejson.dump", "simplejson.dumps"}
                or chain in {"json.dump", "json.dumps", "orjson.dumps", "simplejson.dump", "simplejson.dumps", "dump", "dumps"}
            ):
                continue
            func_name = ""
            current = parents.get(node)
            while current is not None:
                if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    func_name = current.name
                    break
                current = parents.get(current)
            if rel.startswith("engine/bodygraph/") and func_name in allowed_vendor_funcs:
                continue
            if rel == "adapter/logging_filter.py" and func_name in allowed_log_funcs:
                continue
            findings.append(f"{rel}:{func_name or '<module>'}:{chain}")
    return sorted(set(findings))


def _string_constant(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _literal_string_list(node: ast.AST) -> tuple[str, ...]:
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        values = [_string_constant(item) for item in node.elts]
        if all(value is not None for value in values):
            return tuple(str(value).upper() for value in values)
    value = _string_constant(node)
    return (value.upper(),) if value is not None else ()


def _route_methods(deco_name: str, deco: ast.AST) -> str:
    method_by_suffix = {
        ".get": ("GET",),
        ".post": ("POST",),
        ".put": ("PUT",),
        ".patch": ("PATCH",),
        ".delete": ("DELETE",),
    }
    for suffix, methods in method_by_suffix.items():
        if deco_name.endswith(suffix):
            return ",".join(methods)
    if isinstance(deco, ast.Call):
        for keyword in deco.keywords:
            if keyword.arg == "methods":
                methods = _literal_string_list(keyword.value)
                if methods:
                    return ",".join(sorted(methods))
    return ""


def _expr_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return _attribute_chain(node)
    if isinstance(node, ast.Call):
        return _attribute_chain(node.func)
    return ""


def _iter_function_defs(tree: ast.AST) -> dict[str, ast.FunctionDef | ast.AsyncFunctionDef]:
    function_defs: dict[str, ast.FunctionDef | ast.AsyncFunctionDef] = {}
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            function_defs[node.name] = node
        elif isinstance(node, ast.ClassDef):
            for child in node.body:
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    function_defs[f"{node.name}.{child.name}"] = child
    return function_defs


def _is_non_public_route_namespace(route: str) -> bool:
    return route in {"/internal", "/ops", "/dev"} or route.startswith(("/internal/", "/ops/", "/dev/"))


def _join_route_prefix(prefix: str, route: str) -> str:
    if not prefix:
        return route
    if not route:
        return prefix
    return f"/{prefix.strip('/')}/{route.strip('/')}"


def _blueprint_prefixes(tree: ast.AST) -> dict[str, str]:
    prefixes: dict[str, str] = {}
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)) or not isinstance(node.value, ast.Call):
            continue
        if _attribute_chain(node.value.func).rsplit(".", 1)[-1] != "Blueprint":
            continue
        url_prefix = ""
        for keyword in node.value.keywords:
            if keyword.arg == "url_prefix":
                url_prefix = _string_constant(keyword.value) or ""
        if not url_prefix:
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        for target in targets:
            if isinstance(target, ast.Name):
                prefixes[target.id] = url_prefix
    return prefixes


def _decorator_route_root(deco_call: ast.AST) -> str:
    if isinstance(deco_call, ast.Attribute):
        value = deco_call.value
        return value.id if isinstance(value, ast.Name) else _attribute_chain(value)
    return ""


def _adapter_public_route_signatures(loci: tuple[str, ...]) -> list[str]:
    """Return stable public adapter route/hook registrations for PR-04 drift checks."""

    signatures: list[str] = []
    route_decorator_suffixes = (
        ".route",
        ".get",
        ".post",
        ".put",
        ".patch",
        ".delete",
        ".before_app_request",
        ".before_request",
        ".after_app_request",
        ".after_request",
        ".errorhandler",
        ".app_errorhandler",
    )
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        blueprint_prefixes = _blueprint_prefixes(tree)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for deco in node.decorator_list:
                    deco_call = deco.func if isinstance(deco, ast.Call) else deco
                    deco_name = _attribute_chain(deco_call)
                    if not deco_name.endswith(route_decorator_suffixes):
                        continue
                    route_arg = ""
                    if isinstance(deco, ast.Call) and deco.args:
                        route_arg = _string_constant(deco.args[0]) or ""
                    route_root = _decorator_route_root(deco_call)
                    full_route_arg = _join_route_prefix(blueprint_prefixes.get(route_root, ""), route_arg)
                    if _is_non_public_route_namespace(full_route_arg):
                        continue
                    methods = _route_methods(deco_name, deco)
                    signatures.append(f"{rel}:{deco_name}:{full_route_arg}:{methods}:{node.name}")
            if isinstance(node, ast.Call) and _attribute_chain(node.func).endswith(".add_url_rule"):
                route_arg = _string_constant(node.args[0]) if node.args else ""
                endpoint = _string_constant(node.args[1]) if len(node.args) > 1 else ""
                view_desc = ""
                methods = ""
                for keyword in node.keywords:
                    if keyword.arg == "view_func":
                        view_desc = _attribute_chain(keyword.value.func) if isinstance(keyword.value, ast.Call) else _attribute_chain(keyword.value)
                    elif keyword.arg == "methods":
                        method_values = _literal_string_list(keyword.value)
                        if method_values:
                            methods = ",".join(sorted(method_values))
                if route_arg and _is_non_public_route_namespace(route_arg):
                    continue
                if not view_desc and len(node.args) >= 3:
                    view_desc = _attribute_chain(node.args[2].func) if isinstance(node.args[2], ast.Call) else _attribute_chain(node.args[2])
                signatures.append(f"{rel}:add_url_rule:{route_arg or ''}:{endpoint or ''}:{methods}:{view_desc}")
            if isinstance(node, ast.Call) and _attribute_chain(node.func).endswith(".register_blueprint"):
                blueprint = _expr_name(node.args[0]) if node.args else ""
                url_prefix = ""
                for keyword in node.keywords:
                    if keyword.arg == "url_prefix":
                        url_prefix = _string_constant(keyword.value) or ""
                signatures.append(f"{rel}:register_blueprint:{blueprint}:{url_prefix}")
    return sorted(set(signatures))


def _is_sanctioned_presenter_call(call: str, aliases: dict[str, str]) -> bool:
    presenter_names = {"emit_public", "emit_public_aux", "emit_public_with_envelope", "emit_reader_public_bytes", "emit_reader_public_envelope"}
    attr = call.rsplit(".", 1)[-1]
    if attr not in presenter_names:
        return False
    root = call.split(".", 1)[0]
    target = aliases.get(root, "")
    if call in presenter_names:
        return aliases.get(call, "") in {
            "engine.presenter.emit_public",
            "engine.presenter.emitter.emit_public",
            "engine.presenter.emitter.emit_public_with_envelope",
            "engine.narratives.emit_public_aux",
            "engine.presenter.emitter.emit_reader_public_bytes",
            "engine.runtime.emit_reader_public_bytes",
            "engine.presenter.emitter.emit_reader_public_envelope",
            "presenter.reader_v1.emitter.emit_public",
            "presenter.reader_v1.emitter.emit_public_with_envelope",
        }
    return target in {"engine.presenter", "engine.presenter.emitter", "presenter.reader_v1.emitter"}


def _adapter_presenter_calls(loci: tuple[str, ...]) -> list[str]:
    calls: list[str] = []
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        aliases = _import_aliases(tree)
        for call in sorted(_call_names(tree)):
            if _is_sanctioned_presenter_call(call, aliases):
                calls.append(f"{rel}:{call}")
    return sorted(set(calls))


def _adapter_presenter_bypass_routes(loci: tuple[str, ...]) -> list[str]:
    """Find registered adapter routes that serialize/respond without a presenter path."""

    findings: list[str] = []
    presenter_calls = {"emit_public", "emit_public_with_envelope", "emit_reader_public_bytes", "emit_reader_public_envelope", "emit_fn"}
    bypass_calls = {"jsonify", "json.dumps", "json.dump", "dumps", "dump", "sercanon", "serialize"}
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        aliases = _import_aliases(tree)
        function_defs = _iter_function_defs(tree)
        class_methods: dict[str, set[str]] = {}
        class_method_names: dict[str, dict[str, set[str]]] = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_methods[node.name] = set()
                class_method_names[node.name] = {}
                for child in node.body:
                    if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name in {"get", "post", "put", "patch", "delete", "head", "options", "dispatch_request"}:
                        key = f"{node.name}.{child.name}"
                        class_methods[node.name].add(key)
                        class_method_names[node.name].setdefault(child.name, set()).add(key)
        function_calls: dict[str, set[str]] = {}
        function_return_calls: dict[str, set[str]] = {}
        direct_presenter: set[str] = set()
        direct_bypass: set[str] = set()
        route_functions: set[str] = set()

        def iter_body_nodes(fn: ast.FunctionDef | ast.AsyncFunctionDef):
            stack = list(fn.body)
            while stack:
                node = stack.pop()
                yield node
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
                    continue
                stack.extend(ast.iter_child_nodes(node))

        def direct_call_names(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> set[str]:
            names: set[str] = set()
            for node in iter_body_nodes(fn):
                if not isinstance(node, ast.Call):
                    continue
                func = node.func
                if isinstance(func, ast.Name):
                    names.add(func.id)
                elif isinstance(func, ast.Attribute):
                    names.add(_attribute_chain(func))
            return names

        def return_call_names(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> set[str]:
            names: set[str] = set()
            assigned_calls: dict[str, set[str]] = {}
            for node in iter_body_nodes(fn):
                if isinstance(node, (ast.Assign, ast.AnnAssign)) and isinstance(node.value, ast.Call):
                    call_name = _attribute_chain(node.value.func)
                    target_nodes = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target_node in target_nodes:
                        if isinstance(target_node, ast.Name):
                            assigned_calls.setdefault(target_node.id, set()).add(call_name)
            for node in iter_body_nodes(fn):
                if not isinstance(node, ast.Return) or node.value is None:
                    continue
                value = node.value
                if isinstance(value, ast.Tuple):
                    value = value.elts[0] if value.elts else value
                if isinstance(value, ast.Await):
                    value = value.value
                if isinstance(value, ast.Call):
                    names.add(_attribute_chain(value.func))
                elif isinstance(value, ast.Name):
                    names.update(assigned_calls.get(value.id, set()))
            return names

        def node_is_jsonish(value: ast.AST) -> bool:
            if isinstance(value, ast.Await):
                return node_is_jsonish(value.value)
            if isinstance(value, ast.Tuple):
                return bool(value.elts) and node_is_jsonish(value.elts[0])
            if isinstance(value, (ast.Dict, ast.List)):
                return True
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                stripped = value.value.lstrip()
                return stripped.startswith("{") or stripped.startswith("[")
            if isinstance(value, ast.Constant) and isinstance(value.value, bytes):
                stripped = value.value.lstrip()
                return stripped.startswith(b"{") or stripped.startswith(b"[")
            if isinstance(value, ast.Call):
                call_name = _attribute_chain(value.func)
                root = _root_name(value.func)
                target = aliases.get(root or "", root or "")
                if call_name == "make_response" or target == "flask.make_response" or call_name.endswith(".make_response"):
                    return any(node_is_jsonish(arg) for arg in value.args) or any(
                        keyword.arg in {"response", "json", "data"} and node_is_jsonish(keyword.value) for keyword in value.keywords
                    )
                if (
                    call_name in {"json.dumps", "dumps", "jsonify", "current_app.json.response", "sercanon", "serialize"}
                    or target in {"flask.jsonify", "json.dumps"}
                    or call_name.endswith((".jsonify", ".json.response", ".dumps", ".sercanon", ".serialize"))
                ):
                    return True
                return False
            return False

        def function_has_bypass(fn: ast.FunctionDef | ast.AsyncFunctionDef, calls: set[str]) -> bool:
            if any(
                call in bypass_calls
                or aliases.get(call, "") in {"flask.jsonify", "json.dumps", "json.dump"}
                or call.endswith((".jsonify", ".json.response", ".dumps", ".dump", ".sercanon", ".serialize"))
                for call in calls
            ):
                return True
            assigned_jsonish: set[str] = set()
            for node in iter_body_nodes(fn):
                if isinstance(node, (ast.Assign, ast.AnnAssign)) and node.value is not None and node_is_jsonish(node.value):
                    target_nodes = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target_node in target_nodes:
                        if isinstance(target_node, ast.Name):
                            assigned_jsonish.add(target_node.id)
            for node in iter_body_nodes(fn):
                if isinstance(node, ast.Return) and node.value is not None:
                    if node_is_jsonish(node.value):
                        return True
                    if isinstance(node.value, ast.Name) and node.value.id in assigned_jsonish:
                        return True
                if isinstance(node, ast.Call):
                    call_name = _attribute_chain(node.func)
                    if call_name.endswith("Response") and (
                        any(node_is_jsonish(arg) or (isinstance(arg, ast.Name) and arg.id in assigned_jsonish) for arg in node.args)
                        or any(
                            keyword.arg in {"response", "json", "data"}
                            and (node_is_jsonish(keyword.value) or (isinstance(keyword.value, ast.Name) and keyword.value.id in assigned_jsonish))
                            for keyword in node.keywords
                        )
                    ):
                        return True
            return False

        imported_adapter_helpers = {
            name
            for name, target in aliases.items()
            if target.startswith(("adapter.", "engine.http."))
        }

        for name, fn in function_defs.items():
            calls = direct_call_names(fn)
            function_calls[name] = calls
            function_return_calls[name] = return_call_names(fn)
            if any(_is_sanctioned_presenter_call(call, aliases) for call in calls):
                direct_presenter.add(name)
            for deco in fn.decorator_list:
                deco_name = _attribute_chain(deco.func if isinstance(deco, ast.Call) else deco)
                if deco_name.endswith(
                    (
                        ".route",
                        ".get",
                        ".post",
                        ".put",
                        ".patch",
                        ".delete",
                        ".before_app_request",
                        ".before_request",
                        ".after_app_request",
                        ".after_request",
                        ".errorhandler",
                        ".app_errorhandler",
                    )
                ):
                    route_functions.add(name)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            call_name = _attribute_chain(node.func)
            if not call_name.endswith(".add_url_rule"):
                continue
            view_func: ast.AST | None = None
            for keyword in node.keywords:
                if keyword.arg == "view_func":
                    view_func = keyword.value
                    break
            if view_func is None and len(node.args) >= 3:
                view_func = node.args[2]
            method_values: set[str] = set()
            for keyword in node.keywords:
                if keyword.arg == "methods":
                    method_values = set(_literal_string_list(keyword.value))
                    break
            if method_values and method_values <= {"HEAD", "OPTIONS"}:
                continue
            if isinstance(view_func, ast.Name) and view_func.id in function_defs:
                route_functions.add(view_func.id)
            elif isinstance(view_func, ast.Call):
                view_chain = _attribute_chain(view_func.func)
                class_name = view_chain.rsplit(".", 1)[0] if view_chain.endswith(".as_view") else ""
                if class_name in class_methods:
                    selected_keys = set(class_methods[class_name])
                    if method_values:
                        selected_keys = set(class_method_names[class_name].get("dispatch_request", set()))
                        for method_value in method_values:
                            selected_keys.update(class_method_names[class_name].get(method_value.lower(), set()))
                    route_functions.update(selected_keys)
        for name, fn in function_defs.items():
            if function_has_bypass(fn, function_calls[name]):
                direct_bypass.add(name)

        def callee_candidates(owner: str, callee: str) -> set[str]:
            candidates = {callee}
            if "." in owner and "." not in callee:
                class_name = owner.split(".", 1)[0]
                candidates.add(f"{class_name}.{callee}")
            return {candidate for candidate in candidates if candidate in function_defs}

        reaches_presenter: dict[str, bool] = {}

        def reaches(name: str, seen: set[str] | None = None) -> bool:
            if name in reaches_presenter:
                return reaches_presenter[name]
            if name in direct_presenter:
                reaches_presenter[name] = True
                return True
            seen = set(seen or set())
            if name in seen:
                reaches_presenter[name] = False
                return False
            seen.add(name)
            result = any(reaches(candidate, seen) for callee in function_calls.get(name, set()) for candidate in callee_candidates(name, callee))
            reaches_presenter[name] = result
            return result

        reaches_bypass: dict[str, bool] = {}

        def reaches_direct_bypass(name: str, seen: set[str] | None = None) -> bool:
            if name in reaches_bypass:
                return reaches_bypass[name]
            if name in direct_bypass:
                reaches_bypass[name] = True
                return True
            seen = set(seen or set())
            if name in seen:
                reaches_bypass[name] = False
                return False
            seen.add(name)
            returned_calls = function_return_calls.get(name, set())
            result = any(reaches_direct_bypass(candidate, seen) for callee in returned_calls for candidate in callee_candidates(name, callee))
            if not result:
                result = any(
                    not callee_candidates(name, callee)
                    and not _is_sanctioned_presenter_call(callee, aliases)
                    and callee.split(".", 1)[0] in imported_adapter_helpers
                    for callee in returned_calls
                )
            reaches_bypass[name] = result
            return result

        for name in sorted(route_functions):
            if reaches_direct_bypass(name):
                findings.append(f"{rel}:{name}")
    return findings


def _adapter_routes_without_presenter(loci: tuple[str, ...]) -> list[str]:
    """Find response-producing adapter hooks/routes whose returns lack presenter provenance."""

    findings: list[str] = []
    route_decorator_suffixes = (
        ".route",
        ".get",
        ".post",
        ".put",
        ".patch",
        ".delete",
        ".errorhandler",
        ".app_errorhandler",
        ".before_request",
        ".before_app_request",
        ".after_request",
        ".after_app_request",
    )
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        blueprint_prefixes = _blueprint_prefixes(tree)
        aliases = _import_aliases(tree)
        function_defs: dict[str, ast.FunctionDef | ast.AsyncFunctionDef] = {}
        simple_names: dict[str, list[str]] = {}

        def add_function(key: str, simple_name: str, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
            function_defs[key] = node
            simple_names.setdefault(simple_name, []).append(key)

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                add_function(f"{node.name}@{node.lineno}", node.name, node)
        class_methods: dict[str, set[str]] = {}
        class_method_names: dict[str, dict[str, set[str]]] = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                method_keys: set[str] = set()
                method_names: dict[str, set[str]] = {}
                for child in node.body:
                    if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        key = f"{node.name}.{child.name}@{child.lineno}"
                        add_function(key, f"{node.name}.{child.name}", child)
                        if child.name in {"get", "post", "put", "patch", "delete", "head", "options", "dispatch_request"}:
                            method_keys.add(key)
                            method_names.setdefault(child.name, set()).add(key)
                class_methods[node.name] = method_keys
                class_method_names[node.name] = method_names

        def iter_body_nodes(fn: ast.FunctionDef | ast.AsyncFunctionDef):
            stack = list(fn.body)
            while stack:
                node = stack.pop()
                yield node
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
                    continue
                stack.extend(ast.iter_child_nodes(node))

        imported_presenter_callable_names: set[str] = {
            alias_name for alias_name in aliases if _is_sanctioned_presenter_call(alias_name, aliases)
        }
        ast_parents: dict[ast.AST, ast.AST] = {}
        for parent in ast.walk(tree):
            for child in ast.iter_child_nodes(parent):
                ast_parents[child] = parent
        key_by_node = {node: key for key, node in function_defs.items()}
        parent_function_by_key: dict[str, str] = {}
        for key, fn in function_defs.items():
            current = ast_parents.get(fn)
            while current is not None:
                if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef)) and current in key_by_node:
                    parent_function_by_key[key] = key_by_node[current]
                    break
                current = ast_parents.get(current)

        def direct_body_nodes(fn: ast.FunctionDef | ast.AsyncFunctionDef):
            for node in fn.body:
                yield node

        def presenter_callable_names_for(owner: str) -> set[str]:
            def is_none_constant(value: ast.AST) -> bool:
                return isinstance(value, ast.Constant) and value.value is None

            def default_none_params(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> set[str]:
                positional = list(fn.args.posonlyargs) + list(fn.args.args)
                defaults = [None] * (len(positional) - len(fn.args.defaults)) + list(fn.args.defaults)
                names = {arg.arg for arg, default in zip(positional, defaults) if default is not None and is_none_constant(default)}
                names.update(arg.arg for arg, default in zip(fn.args.kwonlyargs, fn.args.kw_defaults) if default is not None and is_none_constant(default))
                return names

            def conditional_default_aliases(fn: ast.FunctionDef | ast.AsyncFunctionDef, current_names: set[str]) -> set[str]:
                defaults = default_none_params(fn)
                aliases_from_defaults: set[str] = set()
                for stmt in fn.body:
                    if not isinstance(stmt, ast.If) or len(stmt.body) != 1 or stmt.orelse:
                        continue
                    body_stmt = stmt.body[0]
                    if not isinstance(body_stmt, (ast.Assign, ast.AnnAssign)) or body_stmt.value is None:
                        continue
                    targets = body_stmt.targets if isinstance(body_stmt, ast.Assign) else [body_stmt.target]
                    rhs = _attribute_chain(body_stmt.value)
                    if not (_is_sanctioned_presenter_call(rhs, aliases) or rhs in current_names):
                        continue
                    for target in targets:
                        if not isinstance(target, ast.Name) or target.id not in defaults:
                            continue
                        test = stmt.test
                        if isinstance(test, ast.Compare) and isinstance(test.left, ast.Name) and test.left.id == target.id and len(test.ops) == 1 and len(test.comparators) == 1:
                            if isinstance(test.ops[0], (ast.Is, ast.Eq)) and is_none_constant(test.comparators[0]):
                                aliases_from_defaults.add(target.id)
                return aliases_from_defaults

            def collect_branch_complete_aliases(fn: ast.FunctionDef | ast.AsyncFunctionDef, current_names: set[str]) -> set[str]:
                collected: set[str] = set()
                for stmt in fn.body:
                    if not isinstance(stmt, ast.If) or not stmt.body or not stmt.orelse:
                        continue
                    branch_values: list[dict[str, list[str]]] = []
                    for branch in (stmt.body, stmt.orelse):
                        values: dict[str, list[str]] = {}
                        for child in branch:
                            if not isinstance(child, (ast.Assign, ast.AnnAssign)) or child.value is None:
                                continue
                            rhs = _attribute_chain(child.value)
                            targets = child.targets if isinstance(child, ast.Assign) else [child.target]
                            for target in targets:
                                if isinstance(target, ast.Name):
                                    values.setdefault(target.id, []).append(rhs)
                        branch_values.append(values)
                    for target_name in set(branch_values[0]) & set(branch_values[1]):
                        rhs_values = branch_values[0][target_name] + branch_values[1][target_name]
                        if rhs_values and all(_is_sanctioned_presenter_call(rhs, aliases) or rhs in current_names for rhs in rhs_values):
                            collected.add(target_name)
                return collected

            chain: list[str] = []
            current: str | None = owner
            while current is not None:
                chain.append(current)
                current = parent_function_by_key.get(current)
            names = set(imported_presenter_callable_names)
            for key in reversed(chain):
                fn = function_defs[key]
                for node in direct_body_nodes(fn):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names:
                        names.remove(node.name)
                    if not isinstance(node, (ast.Assign, ast.AnnAssign)) or node.value is None:
                        continue
                    rhs = _attribute_chain(node.value)
                    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target in targets:
                        if not isinstance(target, ast.Name):
                            continue
                        if _is_sanctioned_presenter_call(rhs, aliases) or rhs in names:
                            names.add(target.id)
                        elif target.id in names:
                            names.remove(target.id)
                names.update(collect_branch_complete_aliases(fn, names))
                names.update(conditional_default_aliases(fn, names))
            return names

        route_functions: set[str] = set()
        route_methods_by_key: dict[str, set[str]] = {}
        hook_kind_by_key: dict[str, str] = {}
        for key, fn in function_defs.items():
            for deco in fn.decorator_list:
                deco_name = _attribute_chain(deco.func if isinstance(deco, ast.Call) else deco)
                if deco_name.endswith(route_decorator_suffixes):
                    route_path = (_string_constant(deco.args[0]) or "") if isinstance(deco, ast.Call) and deco.args else ""
                    route_root = _decorator_route_root(deco.func if isinstance(deco, ast.Call) else deco)
                    full_route_path = _join_route_prefix(blueprint_prefixes.get(route_root, ""), route_path)
                    if _is_non_public_route_namespace(full_route_path):
                        continue
                    if deco_name.endswith((".after_request", ".after_app_request")):
                        hook_kind_by_key[key] = "after_request"
                    elif deco_name.endswith((".before_request", ".before_app_request")):
                        hook_kind_by_key[key] = "before_request"
                    elif deco_name.endswith((".errorhandler", ".app_errorhandler")):
                        hook_kind_by_key[key] = "errorhandler"
                    methods = set(filter(None, _route_methods(deco_name, deco).split(",")))
                    if methods and methods <= {"HEAD", "OPTIONS"}:
                        route_functions.add(key)
                        route_methods_by_key.setdefault(key, set()).update(methods)
                        continue
                    route_functions.add(key)
                    route_methods_by_key.setdefault(key, set()).update(methods)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not _attribute_chain(node.func).endswith(".add_url_rule"):
                continue
            view_func: ast.AST | None = None
            for keyword in node.keywords:
                if keyword.arg == "view_func":
                    view_func = keyword.value
                    break
            if view_func is None and len(node.args) >= 3:
                view_func = node.args[2]
            method_values: set[str] = set()
            for keyword in node.keywords:
                if keyword.arg == "methods":
                    method_values = set(_literal_string_list(keyword.value))
                    break
            if isinstance(view_func, ast.Name) and view_func.id in simple_names:
                for key in simple_names[view_func.id]:
                    route_functions.add(key)
                    route_methods_by_key.setdefault(key, set()).update(method_values)
            elif isinstance(view_func, ast.Call):
                view_chain = _attribute_chain(view_func.func)
                class_name = view_chain.rsplit(".", 1)[0] if view_chain.endswith(".as_view") else ""
                if class_name in class_methods:
                    selected_keys = set(class_methods[class_name])
                    if method_values:
                        selected_keys = set(class_method_names[class_name].get("dispatch_request", set()))
                        for method_value in method_values:
                            selected_keys.update(class_method_names[class_name].get(method_value.lower(), set()))
                    for key in selected_keys:
                        route_functions.add(key)
                        route_methods_by_key.setdefault(key, set()).update(method_values)

        proven_cache: dict[str, bool] = {}

        def callee_candidates(owner: str, callee: str) -> set[str]:
            names = {callee, callee.rsplit(".", 1)[-1]}
            if "." in owner.split("@", 1)[0] and "." not in callee:
                names.add(f"{owner.split('@', 1)[0].split('.', 1)[0]}.{callee}")
            candidates: set[str] = set()
            for name in names:
                candidates.update(simple_names.get(name, []))
            return candidates

        def helper_passthrough_params(name: str) -> set[str]:
            fn = function_defs.get(name)
            if fn is None:
                return set()
            params = {arg.arg for arg in fn.args.args + fn.args.posonlyargs + fn.args.kwonlyargs}

            def returns_param_on_all_paths(statements: list[ast.stmt]) -> str | None:
                for index, stmt in enumerate(statements):
                    if isinstance(stmt, ast.Return):
                        if isinstance(stmt.value, ast.Name) and stmt.value.id in params:
                            return stmt.value.id
                        return None
                    if isinstance(stmt, ast.If):
                        body_result = returns_param_on_all_paths(stmt.body)
                        else_result = returns_param_on_all_paths(stmt.orelse)
                        if body_result is not None and body_result == else_result:
                            return body_result
                        tail_result = returns_param_on_all_paths(statements[index + 1 :])
                        if body_result is not None and else_result is None and body_result == tail_result:
                            return tail_result
                        if else_result is not None and body_result is None and else_result == tail_result:
                            return tail_result
                        if body_result is not None or else_result is not None:
                            return None
                return None

            observed_returns: set[str] = set()
            for node in ast.walk(fn):
                if not isinstance(node, ast.Return):
                    continue
                if isinstance(node.value, ast.Name) and node.value.id in params:
                    observed_returns.add(node.value.id)
                else:
                    return set()
            if len(observed_returns) != 1:
                return set()
            returned = returns_param_on_all_paths(fn.body)
            return {returned} if returned is not None and returned in observed_returns else set()


        def response_param_content_status_safe(fn: ast.FunctionDef | ast.AsyncFunctionDef, param_name: str) -> bool:
            unsafe_attrs = {"data", "response", "status", "status_code"}
            unsafe_methods = {"set_data", "set_json"}
            for node in iter_body_nodes(fn):
                if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                    targets = []
                    if isinstance(node, ast.Assign):
                        targets = list(node.targets)
                    elif isinstance(node, ast.AnnAssign):
                        targets = [node.target]
                    else:
                        targets = [node.target]
                    for target in targets:
                        if isinstance(target, ast.Name) and target.id == param_name:
                            return False
                        if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == param_name and target.attr in unsafe_attrs:
                            return False
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                    if node.func.value.id == param_name and node.func.attr in unsafe_methods:
                        return False
            return True

        def _constant_int(node: ast.AST | None) -> int | None:
            return node.value if isinstance(node, ast.Constant) and isinstance(node.value, int) else None

        def _response_status(value: ast.Call) -> int | None:
            if len(value.args) >= 2:
                status = _constant_int(value.args[1])
                if status is not None:
                    return status
            for keyword in value.keywords:
                if keyword.arg == "status":
                    status = _constant_int(keyword.value)
                    if status is not None:
                        return status
            return None

        def function_mentions_head_or_options(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
            for node in ast.walk(fn):
                if isinstance(node, ast.Constant) and node.value in {"HEAD", "OPTIONS"}:
                    return True
            return False

        def function_has_compat_scope_predicate(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
            for node in ast.walk(fn):
                if isinstance(node, ast.Constant) and node.value == "/api/compat/v1":
                    return True
            return False

        def is_empty_transport_response(value: ast.Call, owner: str) -> bool:
            call = _attribute_chain(value.func)
            if not (call == "Response" or call.endswith(".Response") or call.endswith("TransportResponse")):
                return False
            if not value.args:
                return False
            first = value.args[0]
            if not (isinstance(first, ast.Constant) and first.value in {b"", ""}):
                return False
            status = _response_status(value)
            function_name = owner.split("@", 1)[0].lower()
            if status in {204, 304}:
                return True
            if status == 405 and ("head" in function_name or "options" in function_name):
                return True
            methods = route_methods_by_key.get(owner, set())
            fn = function_defs.get(owner)
            if bool(methods) and methods <= {"HEAD", "OPTIONS"}:
                return True
            if status == 200 and fn is not None and function_mentions_head_or_options(fn):
                return True
            if status == 200 and fn is not None:
                return any(isinstance(node, ast.Attribute) and node.attr == "suppressed" for node in ast.walk(fn))
            return False

        def value_has_presenter(value: ast.AST, owner: str, assigned_good: set[str], seen: set[str]) -> bool:
            if isinstance(value, ast.Await):
                return value_has_presenter(value.value, owner, assigned_good, seen)
            if isinstance(value, ast.Tuple):
                return bool(value.elts) and value_has_presenter(value.elts[0], owner, assigned_good, seen)
            if isinstance(value, ast.Name):
                return value.id in assigned_good
            if isinstance(value, ast.Attribute) and isinstance(value.value, ast.Name):
                return value.attr == "body" and value.value.id in assigned_good
            if isinstance(value, ast.Subscript):
                index_value = value.slice.value if isinstance(value.slice, ast.Constant) else None
                if index_value != 0:
                    return False
                if isinstance(value.value, ast.Call):
                    call = _attribute_chain(value.value.func)
                    return _is_sanctioned_presenter_call(call, aliases) or call in presenter_callable_names_for(owner)
                if isinstance(value.value, ast.Name):
                    return value.value.id in assigned_good
                return False
            if isinstance(value, ast.Call):
                call = _attribute_chain(value.func)
                if _is_sanctioned_presenter_call(call, aliases) or call in presenter_callable_names_for(owner):
                    return True
                if call == "make_response" or call.endswith((".make_response", ".Response")) or call == "Response" or call.endswith("TransportResponse"):
                    body_arg = value.args[0] if value.args else None
                    return is_empty_transport_response(value, owner) or (body_arg is not None and value_has_presenter(body_arg, owner, assigned_good, seen)) or any(
                        keyword.arg in {"response", "data"} and value_has_presenter(keyword.value, owner, assigned_good, seen)
                        for keyword in value.keywords
                    )
                candidates = callee_candidates(owner, call)
                if len(candidates) > 1:
                    return False
                for candidate in candidates:
                    passthrough = helper_passthrough_params(candidate)
                    if passthrough:
                        positional_params = [arg.arg for arg in function_defs[candidate].args.args + function_defs[candidate].args.posonlyargs]
                        for index, arg in enumerate(value.args):
                            if index < len(positional_params) and positional_params[index] in passthrough and value_has_presenter(arg, owner, assigned_good, seen):
                                return True
                    if function_returns_presenter(candidate, seen):
                        return True
            return False

        def assigned_presenter_vars(fn: ast.FunctionDef | ast.AsyncFunctionDef, owner: str, seen: set[str]) -> set[str]:
            assignments: dict[str, list[ast.AST]] = {}
            branch_assignments: list[dict[str, list[list[ast.AST]]]] = []

            def collect_direct_assignments(statements: list[ast.stmt]) -> dict[str, list[ast.AST]]:
                found: dict[str, list[ast.AST]] = {}
                for stmt in statements:
                    if not isinstance(stmt, (ast.Assign, ast.AnnAssign)) or stmt.value is None:
                        continue
                    targets = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]
                    for target in targets:
                        if isinstance(target, ast.Name):
                            found.setdefault(target.id, []).append(stmt.value)
                return found

            for node in fn.body:
                if isinstance(node, (ast.Assign, ast.AnnAssign)) and node.value is not None:
                    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target in targets:
                        if isinstance(target, ast.Name):
                            assignments.setdefault(target.id, []).append(node.value)
                elif isinstance(node, ast.If) and node.body and node.orelse:
                    branch_maps = [collect_direct_assignments(node.body), collect_direct_assignments(node.orelse)]
                    complete: dict[str, list[list[ast.AST]]] = {}
                    for target_name in set(branch_maps[0]) & set(branch_maps[1]):
                        complete[target_name] = [branch[target_name] for branch in branch_maps]
                    if complete:
                        branch_assignments.append(complete)

            names: set[str] = set()
            changed = True
            while changed:
                changed = False
                next_names: set[str] = set()
                for target_name, values in assignments.items():
                    if values and all(value_has_presenter(value, owner, names, seen) for value in values):
                        next_names.add(target_name)
                for complete in branch_assignments:
                    for target_name, branch_values in complete.items():
                        if all(values and all(value_has_presenter(value, owner, names, seen) for value in values) for values in branch_values):
                            next_names.add(target_name)
                if next_names != names:
                    names = next_names
                    changed = True
            return names

        def function_returns_presenter(name: str, seen: set[str] | None = None) -> bool:
            if name in proven_cache:
                return proven_cache[name]
            seen = set(seen or set())
            if name in seen:
                proven_cache[name] = False
                return False
            seen.add(name)
            fn = function_defs.get(name)
            if fn is None:
                proven_cache[name] = False
                return False
            assigned_good = assigned_presenter_vars(fn, name, seen)
            saw_response_return = False
            saw_passthrough_return = False
            params = {arg.arg for arg in fn.args.args + fn.args.posonlyargs + fn.args.kwonlyargs}
            for node in iter_body_nodes(fn):
                if isinstance(node, ast.Raise):
                    proven_cache[name] = False
                    return False
                if isinstance(node, ast.Call) and _attribute_chain(node.func).endswith("abort"):
                    proven_cache[name] = False
                    return False
                if not isinstance(node, ast.Return) or node.value is None:
                    continue
                if isinstance(node.value, ast.Constant) and node.value.value is None:
                    if hook_kind_by_key.get(name) == "before_request":
                        continue
                    proven_cache[name] = False
                    return False
                if hook_kind_by_key.get(name) == "errorhandler" and isinstance(node.value, ast.Name) and node.value.id in params and function_has_compat_scope_predicate(fn):
                    continue
                if hook_kind_by_key.get(name) == "after_request":
                    if isinstance(node.value, ast.Name) and node.value.id in params and response_param_content_status_safe(fn, node.value.id):
                        saw_passthrough_return = True
                        continue
                    if isinstance(node.value, ast.Call):
                        call = _attribute_chain(node.value.func)
                        candidates = callee_candidates(name, call)
                        for candidate in candidates:
                            passthrough = helper_passthrough_params(candidate)
                            positional_params = [arg.arg for arg in function_defs[candidate].args.args + function_defs[candidate].args.posonlyargs]
                            for index, arg in enumerate(node.value.args):
                                if (
                                    index < len(positional_params)
                                    and positional_params[index] in passthrough
                                    and isinstance(arg, ast.Name)
                                    and arg.id in params
                                    and response_param_content_status_safe(fn, arg.id)
                                    and response_param_content_status_safe(function_defs[candidate], positional_params[index])
                                ):
                                    saw_passthrough_return = True
                                    break
                            if saw_passthrough_return:
                                break
                        if saw_passthrough_return:
                            continue
                saw_response_return = True
                if not value_has_presenter(node.value, name, assigned_good, seen):
                    proven_cache[name] = False
                    return False
            proven_cache[name] = (
                saw_response_return
                or (hook_kind_by_key.get(name) == "after_request" and saw_passthrough_return)
                or (hook_kind_by_key.get(name) == "before_request" and not saw_response_return)
            )
            return proven_cache[name]

        for name in sorted(route_functions):
            if not function_returns_presenter(name):
                findings.append(f"{rel}:{name.split('@', 1)[0]}")
    return sorted(set(findings))

def _pure_compute_external_io(loci: tuple[str, ...]) -> list[str]:
    findings: list[str] = []
    forbidden_modules = {"requests", "httpx", "urllib", "urllib.request", "urllib3", "http.client", "aiohttp", "socket", "subprocess"}
    forbidden_calls = {
        "socket.create_connection",
        "create_connection",
        "subprocess.run",
        "subprocess.Popen",
        "subprocess.call",
        "subprocess.check_call",
        "subprocess.check_output",
        "check_call",
        "check_output",
        "os.system",
        "os.popen",
        "system",
        "popen",
    }
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        modules = _import_modules(tree)
        calls = _call_names(tree)
        aliases = _import_aliases(tree)
        for module in sorted(modules):
            if module in forbidden_modules or any(module.startswith(f"{forbidden}.") for forbidden in forbidden_modules):
                findings.append(f"{rel}:import:{module}")
        for call in sorted(calls):
            root = call.split(".", 1)[0]
            target = aliases.get(root, root)
            if (
                call in forbidden_calls
                or target in forbidden_calls
                or target in forbidden_modules
                or any(target.startswith(f"{forbidden}.") for forbidden in forbidden_modules)
            ):
                findings.append(f"{rel}:call:{call}")
    return sorted(set(findings))


def _is_http_home_module(module: str) -> bool:
    return module in {"flask", "fastapi", "starlette"} or module.startswith(("flask.", "fastapi.", "starlette."))


def _locus_rows(loci: tuple[str, ...]) -> list[dict[str, str]]:
    rows = []
    module_root = Path(__file__).resolve().parents[2]
    for rel in loci:
        try:
            path, _text, _tree = _python_source(rel)
        except ValueError:
            fallback = module_root / rel
            if not rel.startswith("tools/evidence/") or not fallback.is_file():
                raise
            path = fallback
        rows.append({"path": rel, "sha256": _sha256_path(path)})
    return rows


def _body_without_docstring(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[ast.stmt]:
    body = list(node.body)
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
        return body[1:]
    return body


def _node_mentions_guard_symbol(node: ast.AST, symbol: str) -> bool:
    for child in ast.walk(node):
        if isinstance(child, ast.Constant) and child.value == symbol:
            return True
        if isinstance(child, ast.Name) and child.id == symbol:
            return True
    return False


def _parent_map(tree: ast.AST) -> dict[ast.AST, ast.AST]:
    parents: dict[ast.AST, ast.AST] = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parents[child] = parent
    return parents


def _function_identity(node: ast.FunctionDef | ast.AsyncFunctionDef, parents: dict[ast.AST, ast.AST]) -> str:
    parts = [node.name]
    current = parents.get(node)
    while current is not None:
        if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            parts.append(current.name)
        current = parents.get(current)
    return f"{'.'.join(reversed(parts))}@{node.lineno}"


def _function_node_by_identity(tree: ast.AST, identity: str) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    if "@" not in identity:
        return _function_node_by_name(tree, identity)
    qualname, line_text = identity.rsplit("@", 1)
    try:
        lineno = int(line_text)
    except ValueError:
        return None
    parents = _parent_map(tree)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.lineno == lineno and _function_identity(node, parents).rsplit("@", 1)[0] == qualname:
            return node
    return None


def _vendor_guard_entrypoints(loci: tuple[str, ...]) -> list[str]:
    guarded: list[str] = []
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        parents = _parent_map(tree)
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            guarded_body = ast.Module(body=_body_without_docstring(node), type_ignores=[])
            if (
                _node_mentions_guard_symbol(guarded_body, "SAFE_MODE")
                and _node_mentions_guard_symbol(guarded_body, "ALLOW_NETWORK")
                and any(isinstance(child, ast.Raise) for child in ast.walk(guarded_body))
            ):
                guarded.append(f"{rel}:{_function_identity(node, parents)}")
    return sorted(set(guarded))


def _vendor_external_io_functions(loci: tuple[str, ...]) -> list[str]:
    findings: list[str] = []
    http_methods = {"urlopen", "request", "get", "post", "put", "patch", "delete", "head", "options", "send", "stream"}
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        aliases = _import_aliases(tree)
        opener_roots: set[str] = set()
        client_roots: set[str] = set()
        client_attrs: set[str] = set()

        def remember_client_target(target_node: ast.AST) -> None:
            if isinstance(target_node, ast.Name):
                client_roots.add(target_node.id)
            elif isinstance(target_node, ast.Attribute):
                client_attrs.add(_attribute_chain(target_node))
                client_attrs.add(target_node.attr)

        def remember_opener_target(target_node: ast.AST) -> None:
            if isinstance(target_node, ast.Name):
                opener_roots.add(target_node.id)
            elif isinstance(target_node, ast.Attribute):
                opener_roots.add(_attribute_chain(target_node))

        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)) or not isinstance(node.value, ast.Call):
                continue
            ctor_chain = _attribute_chain(node.value.func)
            ctor_root = _root_name(node.value.func)
            ctor_target = aliases.get(ctor_root or "", ctor_root or "")
            if ctor_target == "urllib.request" and ctor_chain.endswith(".build_opener"):
                target_nodes = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target_node in target_nodes:
                    remember_opener_target(target_node)
            if (
                ctor_target.startswith(("requests", "httpx", "urllib3", "http.client", "aiohttp"))
                and (
                    ctor_chain.endswith((".Session", ".Client", ".AsyncClient", ".PoolManager", ".HTTPConnection", ".HTTPSConnection", ".ClientSession"))
                    or ctor_target.endswith((".Session", ".Client", ".AsyncClient", ".PoolManager", ".HTTPConnection", ".HTTPSConnection", ".ClientSession"))
                )
            ):
                target_nodes = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target_node in target_nodes:
                    remember_client_target(target_node)
        for node in ast.walk(tree):
            if not isinstance(node, (ast.With, ast.AsyncWith)):
                continue
            for item in node.items:
                if not isinstance(item.context_expr, ast.Call) or item.optional_vars is None:
                    continue
                ctor_chain = _attribute_chain(item.context_expr.func)
                ctor_root = _root_name(item.context_expr.func)
                ctor_target = aliases.get(ctor_root or "", ctor_root or "")
                if ctor_target == "urllib.request" and ctor_chain.endswith(".build_opener"):
                    remember_opener_target(item.optional_vars)
                if (
                    ctor_target.startswith(("requests", "httpx", "urllib3", "http.client", "aiohttp"))
                    and (
                        ctor_chain.endswith((".Session", ".Client", ".AsyncClient", ".PoolManager", ".HTTPConnection", ".HTTPSConnection", ".ClientSession"))
                        or ctor_target.endswith((".Session", ".Client", ".AsyncClient", ".PoolManager", ".HTTPConnection", ".HTTPSConnection", ".ClientSession"))
                    )
                ):
                    remember_client_target(item.optional_vars)
        parents: dict[ast.AST, ast.AST] = {}
        for parent in ast.walk(tree):
            for child in ast.iter_child_nodes(parent):
                parents[child] = parent
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            chain = _attribute_chain(node.func)
            root = _root_name(node.func)
            target = aliases.get(root or "", root or "")
            attr = chain.rsplit(".", 1)[-1] if chain else ""
            target_attr = target.rsplit(".", 1)[-1] if target and chain == (root or "") else ""
            receiver = chain.rsplit(".", 1)[0] if "." in chain else root or ""
            shell_or_socket_methods = {"create_connection", "socket", "run", "Popen", "call", "check_call", "check_output", "system", "popen"}
            http_method_names = http_methods | {"build_opener", "ClientSession"}
            is_external = (
                (target.startswith(("urllib.request", "requests", "httpx", "urllib3", "http.client", "aiohttp")) and (attr in http_method_names or target_attr in http_method_names))
                or (root in opener_roots and attr == "open")
                or (receiver in opener_roots and attr == "open")
                or (root in client_roots and attr in http_methods)
                or ((receiver in client_attrs or any(receiver.endswith(f".{client_attr}") for client_attr in client_attrs)) and attr in http_methods)
                or (target.startswith(("socket", "subprocess", "os")) and attr in shell_or_socket_methods)
                or target in {
                    "socket.create_connection",
                    "subprocess.run",
                    "subprocess.Popen",
                    "subprocess.call",
                    "subprocess.check_call",
                    "subprocess.check_output",
                    "os.system",
                    "os.popen",
                }
            )
            if not is_external:
                continue
            func_name = "<module>@0"
            current = parents.get(node)
            while current is not None:
                if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    func_name = _function_identity(current, parents)
                    break
                current = parents.get(current)
            findings.append(f"{rel}:{func_name}:{chain}")
    return sorted(set(findings))


def _function_node_by_name(tree: ast.AST, name: str) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return node
    return None


def _stmt_contains_node(stmt: ast.stmt, target: ast.AST) -> bool:
    return any(child is target for child in ast.walk(stmt))


def _rails_env_axis(node: ast.AST, env_bound_names: dict[str, str]) -> str | None:
    if isinstance(node, ast.Name):
        return env_bound_names.get(node.id)
    if isinstance(node, ast.Subscript):
        chain = _attribute_chain(node.value)
        key = _string_constant(node.slice)
        if chain in {"os.environ", "environ"} and key in {"SAFE_MODE", "ALLOW_NETWORK"}:
            return key
    if isinstance(node, ast.Call):
        call = _attribute_chain(node.func)
        if call in {"os.environ.get", "environ.get", "os.getenv", "getenv"} and node.args:
            key = _string_constant(node.args[0])
            if key in {"SAFE_MODE", "ALLOW_NETWORK"}:
                return key
        for arg in node.args:
            axis = _rails_env_axis(arg, env_bound_names)
            if axis:
                return axis
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.AST):
            axis = _rails_env_axis(node.func.value, env_bound_names)
            if axis:
                return axis
    if isinstance(node, ast.BoolOp):
        axes = {_rails_env_axis(value, env_bound_names) for value in node.values}
        axes.discard(None)
        return next(iter(axes)) if len(axes) == 1 else None
    if isinstance(node, ast.UnaryOp):
        return _rails_env_axis(node.operand, env_bound_names)
    return None


def _rails_env_bound_names(statements: list[ast.stmt]) -> dict[str, str]:
    bound: dict[str, str] = {}
    for stmt in statements:
        if not isinstance(stmt, (ast.Assign, ast.AnnAssign)) or stmt.value is None:
            continue
        axis = _rails_env_axis(stmt.value, bound)
        targets = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]
        for target in targets:
            if isinstance(target, ast.Name):
                if axis is None:
                    bound.pop(target.id, None)
                else:
                    bound[target.id] = axis
    return bound


def _stmt_has_guard_refusal(stmt: ast.stmt, env_bound_names: dict[str, str] | None = None) -> bool:
    if not isinstance(stmt, ast.If):
        return False
    env_bound_names = env_bound_names or {}

    def open_compare_axis(node: ast.AST) -> str | None:
        if not isinstance(node, ast.Compare) or len(node.ops) != 1 or len(node.comparators) != 1:
            return None
        left_axis = _rails_env_axis(node.left, env_bound_names)
        right = node.comparators[0]
        right_value = right.value if isinstance(right, ast.Constant) else None
        op = node.ops[0]
        if left_axis == "SAFE_MODE" and isinstance(op, ast.Eq) and right_value == "0":
            return "SAFE_MODE"
        if left_axis == "ALLOW_NETWORK" and isinstance(op, ast.Eq) and right_value == "1":
            return "ALLOW_NETWORK"
        return None

    def refusal_compare_axis(node: ast.AST) -> str | None:
        if not isinstance(node, ast.Compare) or len(node.ops) != 1 or len(node.comparators) != 1:
            return None
        left_axis = _rails_env_axis(node.left, env_bound_names)
        right = node.comparators[0]
        right_value = right.value if isinstance(right, ast.Constant) else None
        op = node.ops[0]
        if left_axis == "SAFE_MODE" and ((isinstance(op, ast.NotEq) and right_value == "0") or (isinstance(op, ast.Eq) and right_value in {"1", "true", "True"})):
            return "SAFE_MODE"
        if left_axis == "ALLOW_NETWORK" and ((isinstance(op, ast.NotEq) and right_value == "1") or (isinstance(op, ast.Eq) and right_value in {"0", "false", "False"})):
            return "ALLOW_NETWORK"
        return None

    def refusal_axes(test: ast.AST) -> set[str]:
        axis = refusal_compare_axis(test)
        if axis:
            return {axis}
        if isinstance(test, ast.BoolOp) and isinstance(test.op, ast.Or):
            axes: set[str] = set()
            for value in test.values:
                axes.update(refusal_axes(value))
            return axes
        if isinstance(test, ast.UnaryOp) and isinstance(test.op, ast.Not):
            operand = test.operand
            if isinstance(operand, ast.BoolOp) and isinstance(operand.op, ast.And):
                axes = {axis for value in operand.values if (axis := open_compare_axis(value))}
                return axes if axes == {"SAFE_MODE", "ALLOW_NETWORK"} else set()
        return set()

    raises = any(isinstance(child, ast.Raise) for child in stmt.body)
    return raises and refusal_axes(stmt.test) == {"SAFE_MODE", "ALLOW_NETWORK"}


def _vendor_external_io_guard_dominates(item: str) -> bool:
    parts = item.split(":", 2)
    if len(parts) != 3:
        return False
    rel, func_name, chain = parts
    _path, _text, tree = _python_source(rel)
    fn = _function_node_by_identity(tree, func_name)
    if fn is None:
        return False
    for stmt_index, stmt in enumerate(fn.body):
        for node in ast.walk(stmt):
            if isinstance(node, ast.Call) and _attribute_chain(node.func) == chain:
                prior_statements = fn.body[:stmt_index]
                env_bound_names = _rails_env_bound_names(prior_statements)
                return any(_stmt_has_guard_refusal(prior, env_bound_names) for prior in prior_statements)
    return False

def _vendor_seam_guarded(loci: tuple[str, ...]) -> bool:
    guarded_entrypoints = _vendor_guard_entrypoints(loci)
    external_io_functions = _vendor_external_io_functions(loci)
    if not external_io_functions:
        return True
    allowed_low_level_prefixes = ("engine/bodygraph/vendor_client.py:_default_request@",)
    unguarded_external = [
        finding
        for finding in external_io_functions
        if not any(":".join(finding.split(":", 2)[:2]).startswith(prefix) for prefix in allowed_low_level_prefixes)
    ]
    return bool(guarded_entrypoints) and not unguarded_external


def _unsupported_scope_claims(*payloads: dict[str, Any]) -> list[str]:
    unsupported_claim_keys = {
        "ai_scope_claim",
        "live_vendor_call_claim",
        "open_rails_vendor_smoke_claim",
        "public_reader_change_claim",
        "runtime_conformance_claim",
        "normalized_data_path_proof_claim",
        "hde_ferm007_5_claim",
        "hde_ferm008_claim",
    }
    findings: list[str] = []

    def visit(value: Any, path: str) -> None:
        if isinstance(value, dict):
            for key, nested in value.items():
                nested_path = f"{path}.{key}" if path else str(key)
                if key in unsupported_claim_keys and nested != "NONE":
                    findings.append(f"{nested_path}={nested!r}")
                visit(nested, nested_path)
        elif isinstance(value, list):
            for index, nested in enumerate(value):
                visit(nested, f"{path}[{index}]")

    for index, payload in enumerate(payloads):
        visit(payload, f"payload[{index}]")
    return sorted(set(findings))


BOUNDARY_ALLOWED = "allowed"
BOUNDARY_FORBIDDEN = "forbidden"
BOUNDARY_UNKNOWN = "unknown / fail-closed"
BOUNDARY_OUT_OF_SCOPE = "out of scope"
BOUNDARY_PASS_CLASSIFICATIONS = {BOUNDARY_ALLOWED, BOUNDARY_OUT_OF_SCOPE}


def boundary_finding(category: str, classification: str, verdict: str, inspected: list[str], reason: str, details: list[str] | None = None) -> dict[str, Any]:
    return {
        "category": category,
        "classification": classification,
        "verdict": verdict,
        "inspected": inspected,
        "reason": reason,
        "details": sorted(details or []),
    }


def finding_passes(finding: dict[str, Any]) -> bool:
    return finding.get("classification") in BOUNDARY_PASS_CLASSIFICATIONS and finding.get("verdict") == "PASS"


def _is_http_home_module(module: str) -> bool:
    return module in {"flask", "fastapi", "starlette"} or module.startswith(("flask.", "fastapi.", "starlette."))


def vendor_guard_provenance_findings(loci: tuple[str, ...]) -> tuple[list[str], list[str], list[str]]:
    external_io = _vendor_external_io_functions(loci)
    guarded = _vendor_guard_entrypoints(loci)
    guarded_keys = {":".join(item.split(":", 2)[:2]) for item in guarded}
    unresolved: list[str] = []
    allowed: list[str] = []
    for item in external_io:
        key = ":".join(item.split(":", 2)[:2])
        if key in guarded_keys and _vendor_external_io_guard_dominates(item):
            allowed.append(item + " guarded_by=" + key)
        else:
            unresolved.append(item)
    return allowed, unresolved, guarded


def analyze_adapter_boundary(
    *,
    source_selection: dict[str, Any],
    request_shaping: dict[str, Any],
    response_mapping: dict[str, Any],
    adapter_loci: tuple[str, ...],
    canonical_adapter_loci: tuple[str, ...],
    presenter_loci: tuple[str, ...],
    vendor_seam_loci: tuple[str, ...],
    pure_compute_loci: tuple[str, ...],
    public_route_baseline: tuple[str, ...],
    evidence_tool_loci: tuple[str, ...],
) -> dict[str, Any]:
    """Return analyzer-owned boundary findings, deltas, provenance, and verdict."""
    if source_selection.get("request_shaping_claim") != "NONE":
        raise ValueError("ADAPTER_BOUNDARY_SOURCE_SELECTION_BASELINE_DRIFT")
    if request_shaping.get("route_family") != "recommended_v2_chart":
        raise ValueError("ADAPTER_BOUNDARY_REQUEST_SHAPING_BASELINE_DRIFT")
    if response_mapping.get("response_envelope_mapping_scope") != "HDE-FERM007.3 proof-level v2 StandardResponse envelope mapping only":
        raise ValueError("ADAPTER_BOUNDARY_RESPONSE_MAPPING_BASELINE_DRIFT")

    adapter_rows = _locus_rows(adapter_loci)
    presenter_rows = _locus_rows(presenter_loci)
    vendor_rows = _locus_rows(vendor_seam_loci)
    pure_rows = _locus_rows(pure_compute_loci)
    evidence_tool_rows = _locus_rows(evidence_tool_loci)

    adapter_http_modules: set[str] = set()
    adapter_guard_findings: list[str] = []
    for rel in adapter_loci:
        _path, text, tree = _python_source(rel)
        adapter_http_modules |= {m for m in _import_modules(tree) if m == "flask" or m.startswith("flask")}
        if rel == "adapter/http_reader.py" and "SAFE_MODE" not in text:
            adapter_guard_findings.append(f"{rel}:SAFE_MODE not discovered")

    vendor_modules: set[str] = set()
    vendor_calls: set[str] = set()
    for rel in vendor_seam_loci:
        _path, _text, tree = _python_source(rel)
        vendor_modules |= _import_modules(tree)
        vendor_calls |= _call_names(tree)

    adapter_presenter_calls = _adapter_presenter_calls(adapter_loci)
    presenter_bypass = _adapter_presenter_bypass_routes(adapter_loci)
    unresolved_presenter_routes = _adapter_routes_without_presenter(adapter_loci)
    discovered_public_routes = _adapter_public_route_signatures(adapter_loci)
    public_reader_route_drift = sorted(set(discovered_public_routes) ^ set(public_route_baseline))
    route_baseline_reconciled = bool(discovered_public_routes) and not public_reader_route_drift
    route_baseline_out_of_scope = not discovered_public_routes and adapter_loci != canonical_adapter_loci
    pure_external_io = _pure_compute_external_io(pure_compute_loci)
    second_http_home = sorted(module for module in vendor_modules if _is_http_home_module(module))
    adapter_bypass = _adapter_external_io_calls(adapter_loci)
    ad_hoc_serializers = _ad_hoc_json_serializers(adapter_loci + vendor_seam_loci + presenter_loci)
    unsupported_scope_claims = _unsupported_scope_claims(source_selection, request_shaping, response_mapping)
    guard_allowed, guard_unresolved, guarded_entrypoints = vendor_guard_provenance_findings(vendor_seam_loci)
    vendor_external_io = _vendor_external_io_functions(vendor_seam_loci)
    if guard_unresolved:
        raise ValueError("ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED:" + ",".join(guard_unresolved))

    findings = [
        boundary_finding("adapter_route_registration", BOUNDARY_ALLOWED if adapter_http_modules else BOUNDARY_UNKNOWN, "PASS" if adapter_http_modules else "UNKNOWN", [row["path"] for row in adapter_rows], "discovered Flask adapter registrations before classification" if adapter_http_modules else "no current adapter route registrations were discoverable", discovered_public_routes),
        boundary_finding("public_routes", BOUNDARY_ALLOWED if route_baseline_reconciled else (BOUNDARY_OUT_OF_SCOPE if route_baseline_out_of_scope else BOUNDARY_UNKNOWN), "PASS" if route_baseline_reconciled or route_baseline_out_of_scope else "UNKNOWN", [row["path"] for row in adapter_rows], "discovered current route signatures reconcile with governed PR-04 baseline" if route_baseline_reconciled else ("no public route signatures discovered in noncanonical test locus; route surface is out of scope" if route_baseline_out_of_scope else "discovered current route signatures cannot be reconciled with baseline; route drift fails closed"), public_reader_route_drift or discovered_public_routes),
        boundary_finding("response_producing_paths", BOUNDARY_ALLOWED if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else (BOUNDARY_FORBIDDEN if presenter_bypass else BOUNDARY_UNKNOWN), "PASS" if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else ("FAIL" if presenter_bypass else "UNKNOWN"), [row["path"] for row in adapter_rows], "public response-producing paths have explicit presenter/emitter provenance" if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else "response-producing path provenance is unresolved or bypasses presenter", presenter_bypass + unresolved_presenter_routes or adapter_presenter_calls),
        boundary_finding("presenter_provenance", BOUNDARY_ALLOWED if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else (BOUNDARY_FORBIDDEN if presenter_bypass else BOUNDARY_UNKNOWN), "PASS" if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else ("FAIL" if presenter_bypass else "UNKNOWN"), [row["path"] for row in presenter_rows], "adapter routes resolve to sanctioned presenter/emitter calls" if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else "presenter provenance is not proven for every response path", presenter_bypass + unresolved_presenter_routes or adapter_presenter_calls),
        boundary_finding("serializer_paths", BOUNDARY_ALLOWED if not ad_hoc_serializers else BOUNDARY_FORBIDDEN, "PASS" if not ad_hoc_serializers else "FAIL", [row["path"] for row in adapter_rows + vendor_rows + presenter_rows], "no ad-hoc JSON serializer path discovered outside allowed vendor helpers" if not ad_hoc_serializers else "ad-hoc serializer path discovered on governed/public boundary", ad_hoc_serializers),
        boundary_finding("external_io_paths", BOUNDARY_ALLOWED if not adapter_bypass and not second_http_home else BOUNDARY_FORBIDDEN, "PASS" if not adapter_bypass and not second_http_home else "FAIL", [row["path"] for row in adapter_rows + vendor_rows], "external I/O remains limited to sanctioned vendor seam" if not adapter_bypass and not second_http_home else "external I/O or HTTP home found outside sanctioned vendor seam", adapter_bypass + second_http_home),
        boundary_finding("pure_compute_external_io", BOUNDARY_ALLOWED if not pure_external_io else BOUNDARY_FORBIDDEN, "PASS" if not pure_external_io else "FAIL", [row["path"] for row in pure_rows], "pure compute loci have no external-I/O imports or calls" if not pure_external_io else "pure compute external-I/O capability discovered", pure_external_io),
        boundary_finding("guard_provenance", BOUNDARY_ALLOWED if (guard_allowed or not vendor_external_io) and not guard_unresolved and not adapter_guard_findings else BOUNDARY_UNKNOWN, "PASS" if (guard_allowed or not vendor_external_io) and not guard_unresolved and not adapter_guard_findings else "UNKNOWN", [row["path"] for row in vendor_rows], "each relevant vendor external-I/O path is tied to a closed-rails guard entrypoint" if (guard_allowed or not vendor_external_io) and not guard_unresolved and not adapter_guard_findings else "guard symbols are missing or cannot be tied to each relevant external-I/O path", guard_unresolved + adapter_guard_findings + guard_allowed),
        boundary_finding("public_surface_posture", BOUNDARY_ALLOWED if not unsupported_scope_claims else BOUNDARY_FORBIDDEN, "PASS" if not unsupported_scope_claims else "FAIL", ["artifacts/vendor/hdapi_v2/source_selection.snapshot.json", "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json", "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"], "dependency evidence emits no unsupported public/runtime/open-rails/AI scope claims" if not unsupported_scope_claims else "unsupported scope claim discovered in dependency evidence", unsupported_scope_claims),
        boundary_finding("evidence_binding_posture", BOUNDARY_ALLOWED if all(isinstance(payload, dict) and payload for payload in [source_selection, request_shaping, response_mapping]) else BOUNDARY_UNKNOWN, "PASS" if all(isinstance(payload, dict) and payload for payload in [source_selection, request_shaping, response_mapping]) else "UNKNOWN", [row["path"] for row in evidence_tool_rows], "PR-01/PR-02/PR-03 dependency payloads are present and non-empty; index/path-proof validation is delegated to governed tools" if all(isinstance(payload, dict) and payload for payload in [source_selection, request_shaping, response_mapping]) else "dependency evidence payloads are missing or empty", []),
        boundary_finding("hde_ferm007_5_runtime_v2_live_open_rails_ai_scope", BOUNDARY_OUT_OF_SCOPE, "PASS", [row["path"] for row in evidence_tool_rows], "explicitly outside W-002 / HDE-FERM007.4; no claim is emitted", []),
    ]
    check_by_category = {finding["category"]: finding_passes(finding) for finding in findings}
    checks = {
        "adapter_http_home_inspected": check_by_category["adapter_route_registration"],
        "actual_repo_loci_discovered_before_classification": all([adapter_rows, presenter_rows, vendor_rows, pure_rows, evidence_tool_rows]),
        "hard_coded_path_lists_not_used_as_proof": bool(discovered_public_routes) or adapter_loci != canonical_adapter_loci,
        "unknown_current_categories_fail_closed": all(f["verdict"] != "PASS" for f in findings if f["classification"] == BOUNDARY_UNKNOWN),
        "conservative_positive_boundary_contract_applied": {f["classification"] for f in findings} <= {BOUNDARY_ALLOWED, BOUNDARY_FORBIDDEN, BOUNDARY_UNKNOWN, BOUNDARY_OUT_OF_SCOPE},
        "presenter_emitter_inspected": check_by_category["presenter_provenance"],
        "vendor_seam_inspected": bool(vendor_rows) and ("urllib.request" in vendor_modules or "urllib" in vendor_modules or "urlrequest.urlopen" in vendor_calls),
        "no_second_http_home": not second_http_home,
        "no_adapter_bypass": not adapter_bypass,
        "no_presenter_bypass": not presenter_bypass and not unresolved_presenter_routes and bool(adapter_presenter_calls),
        "no_ad_hoc_serialization": not ad_hoc_serializers,
        "no_pure_compute_external_io": not pure_external_io,
        "guard_provenance_per_relevant_path": check_by_category["guard_provenance"],
        "prior_evidence_families_bound": check_by_category["evidence_binding_posture"],
        "no_public_reader_change": check_by_category["public_routes"],
        "no_unsupported_scope_claim": check_by_category["public_surface_posture"],
    }
    verdict_status = "PASS" if all(checks.values()) and all(finding_passes(f) for f in findings) else ("FAIL" if any(f["classification"] == BOUNDARY_FORBIDDEN for f in findings) else "UNKNOWN")
    return {
        "work_item": "W-002",
        "scope": "HDE-EPIC034 PR-04 analyzer-owned adapter/presenter boundary proof for HDE-FERM007.4 only",
        "inspected_loci": {"adapter": adapter_rows, "presenter": presenter_rows, "engine": pure_rows, "vendor_seam": vendor_rows, "evidence_tool": evidence_tool_rows},
        "findings": findings,
        "unknowns": [f for f in findings if f["classification"] == BOUNDARY_UNKNOWN],
        "public_route_deltas": public_reader_route_drift,
        "public_internal_route_classification_posture": next(f for f in findings if f["category"] == "public_routes"),
        "response_producing_path_findings": next(f for f in findings if f["category"] == "response_producing_paths"),
        "presenter_provenance": next(f for f in findings if f["category"] == "presenter_provenance"),
        "serializer_findings": next(f for f in findings if f["category"] == "serializer_paths"),
        "external_io_findings": next(f for f in findings if f["category"] == "external_io_paths"),
        "pure_compute_external_io_findings": next(f for f in findings if f["category"] == "pure_compute_external_io"),
        "guard_provenance": {"finding": next(f for f in findings if f["category"] == "guard_provenance"), "guarded_entrypoints": guarded_entrypoints, "guarded_external_io": guard_allowed, "unresolved_external_io": guard_unresolved},
        "evidence_family_binding_posture": next(f for f in findings if f["category"] == "evidence_binding_posture"),
        "unsupported_scope_claims": unsupported_scope_claims,
        "discovered_public_route_signatures": discovered_public_routes,
        "discovered_presenter_calls": adapter_presenter_calls,
        "checks": checks,
        "verdict_status": verdict_status,
    }
