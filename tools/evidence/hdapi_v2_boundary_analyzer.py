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
            target_attr = target.rsplit(".", 1)[-1] if target else ""
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
    findings: list[str] = []
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        aliases = _import_aliases(tree)
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
                    methods = _route_methods(deco_name, deco)
                    signatures.append(f"{rel}:{deco_name}:{route_arg}:{methods}:{node.name}")
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
    presenter_names = {"emit_public", "emit_public_with_envelope", "emit_reader_public_bytes", "emit_reader_public_envelope", "emit_fn"}
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
            "engine.presenter.emitter.emit_reader_public_bytes",
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
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_methods[node.name] = {
                    f"{node.name}.{child.name}"
                    for child in node.body
                    if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name in {"get", "post", "put", "patch", "delete", "head", "options", "dispatch_request"}
                }
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
            if isinstance(view_func, ast.Name) and view_func.id in function_defs:
                route_functions.add(view_func.id)
            elif isinstance(view_func, ast.Call):
                view_chain = _attribute_chain(view_func.func)
                class_name = view_chain.rsplit(".", 1)[0] if view_chain.endswith(".as_view") else ""
                if class_name in class_methods:
                    route_functions.update(class_methods[class_name])
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
    for rel in loci:
        path, _text, _tree = _python_source(rel)
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


def _vendor_guard_entrypoints(loci: tuple[str, ...]) -> list[str]:
    guarded: list[str] = []
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            guarded_body = ast.Module(body=_body_without_docstring(node), type_ignores=[])
            if (
                _node_mentions_guard_symbol(guarded_body, "SAFE_MODE")
                and _node_mentions_guard_symbol(guarded_body, "ALLOW_NETWORK")
                and any(isinstance(child, ast.Raise) for child in ast.walk(guarded_body))
            ):
                guarded.append(f"{rel}:{node.name}")
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
            receiver = chain.rsplit(".", 1)[0] if "." in chain else root or ""
            shell_or_socket_methods = {"create_connection", "socket", "run", "Popen", "call", "check_call", "check_output", "system", "popen"}
            is_external = (
                (target.startswith(("urllib.request", "requests", "httpx", "urllib3", "http.client", "aiohttp")) and attr in http_methods | {"build_opener", "ClientSession"})
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
            func_name = "<module>"
            current = parents.get(node)
            while current is not None:
                if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    func_name = current.name
                    break
                current = parents.get(current)
            findings.append(f"{rel}:{func_name}:{chain}")
    return sorted(set(findings))


def _vendor_seam_guarded(loci: tuple[str, ...]) -> bool:
    guarded_entrypoints = _vendor_guard_entrypoints(loci)
    external_io_functions = _vendor_external_io_functions(loci)
    if not external_io_functions:
        return True
    allowed_low_level = {"engine/bodygraph/vendor_client.py:_default_request"}
    unguarded_external = [
        finding
        for finding in external_io_functions
        if ":".join(finding.split(":", 2)[:2]) not in allowed_low_level
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

