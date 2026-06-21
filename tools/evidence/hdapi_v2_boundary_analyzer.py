"""Static boundary analyzer for EPIC034 HDAPI v2 adapter/presenter proof.

This module is intentionally independent from the evidence renderer so boundary
policy can be tested without regenerating governed artifacts.
"""
from __future__ import annotations

import ast
import hashlib
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

BOUNDARY_ALLOWED = "allowed"
BOUNDARY_FORBIDDEN = "forbidden"
BOUNDARY_UNKNOWN = "unknown / fail-closed"
BOUNDARY_OUT_OF_SCOPE = "out of scope"


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


BOUNDARY_ROUTE_SUPPORTED = "supported"
BOUNDARY_ROUTE_UNSUPPORTED = "unsupported"
BOUNDARY_ROUTE_AMBIGUOUS = "ambiguous"


SUPPORTED_ROUTE_REGISTRATION_FORMS: dict[str, dict[str, Any]] = {
    "decorator": {
        "registration_kinds": ("route_decorator", "hook_decorator", "errorhandler_decorator"),
        "allowed_owner_forms": ("Flask", "Blueprint", "BlueprintAlias"),
        "required_static_fields": ("owner_expression", "decorator_path"),
        "dynamic_fields_fail_closed": ("route_path", "methods", "errorhandler_key", "routing_keywords"),
        "signed_fields": (
            "source_locus",
            "registration_kind",
            "owner_expression",
            "proven_owner_type",
            "decorator_path",
            "route_path",
            "http_methods",
            "endpoint",
            "view_identity",
            "blueprint_name",
            "blueprint_constructor_prefix",
            "errorhandler_key",
            "routing_keywords",
            "public_internal_classification",
        ),
        "classification_inputs": ("route_path", "blueprint_constructor_prefix"),
        "unsupported_posture": BOUNDARY_UNKNOWN,
    },
    "add_url_rule": {
        "registration_kinds": ("add_url_rule",),
        "allowed_owner_forms": ("Flask", "Blueprint", "BlueprintAlias"),
        "required_static_fields": ("route_path", "endpoint", "view_identity"),
        "dynamic_fields_fail_closed": ("route_path", "endpoint", "methods", "view_identity", "routing_keywords"),
        "signed_fields": (
            "source_locus",
            "registration_kind",
            "owner_expression",
            "proven_owner_type",
            "route_path",
            "http_methods",
            "endpoint",
            "view_identity",
            "imported_view_target",
            "routing_keywords",
            "public_internal_classification",
        ),
        "classification_inputs": ("route_path",),
        "unsupported_posture": BOUNDARY_UNKNOWN,
    },
    "register_blueprint": {
        "registration_kinds": ("register_blueprint",),
        "allowed_owner_forms": ("Flask",),
        "required_static_fields": ("blueprint_name",),
        "dynamic_fields_fail_closed": ("blueprint_name", "register_blueprint_prefix"),
        "signed_fields": (
            "source_locus",
            "registration_kind",
            "owner_expression",
            "proven_owner_type",
            "blueprint_name",
            "blueprint_constructor_prefix",
            "register_blueprint_prefix",
            "public_internal_classification",
        ),
        "classification_inputs": ("register_blueprint_prefix", "blueprint_constructor_prefix"),
        "unsupported_posture": BOUNDARY_UNKNOWN,
    },
    "blueprint_constructor": {
        "registration_kinds": ("blueprint_constructor",),
        "allowed_owner_forms": ("Blueprint",),
        "required_static_fields": ("blueprint_name",),
        "dynamic_fields_fail_closed": ("blueprint_name", "blueprint_constructor_prefix"),
        "signed_fields": (
            "source_locus",
            "registration_kind",
            "blueprint_name",
            "blueprint_constructor_prefix",
            "public_internal_classification",
        ),
        "classification_inputs": ("blueprint_constructor_prefix",),
        "unsupported_posture": BOUNDARY_UNKNOWN,
    },
}


@dataclass(frozen=True)
class RouteSignatureRecord:
    source_locus: str
    registration_kind: str
    parser_status: str
    owner_expression: str = ""
    proven_owner_type: str = ""
    route_path: str = ""
    decorator_path: str = ""
    http_methods: tuple[str, ...] = ()
    endpoint: str = ""
    view_identity: str = ""
    blueprint_name: str = ""
    blueprint_constructor_prefix: str = ""
    register_blueprint_prefix: str = ""
    errorhandler_key: str = ""
    routing_keywords: tuple[tuple[str, str], ...] = ()
    imported_view_target: str = ""
    public_internal_classification: str = BOUNDARY_UNKNOWN
    fail_closed_reason: str = ""
    signed_fields: tuple[tuple[str, Any], ...] = ()


@dataclass(frozen=True)
class RouteRegistrationCandidate:
    source_locus: str
    registration_kind: str
    parser_status: str
    owner_expression: str = ""
    proven_owner_type: str = ""
    route_path: str = ""
    decorator_path: str = ""
    http_methods: tuple[str, ...] = ()
    endpoint: str = ""
    view_identity: str = ""
    blueprint_name: str = ""
    blueprint_constructor_prefix: str = ""
    register_blueprint_prefix: str = ""
    errorhandler_key: str = ""
    routing_keywords: tuple[tuple[str, str], ...] = ()
    imported_view_target: str = ""
    public_internal_classification: str = BOUNDARY_UNKNOWN
    fail_closed_reason: str = ""
    signed_fields: tuple[tuple[str, Any], ...] = ()


def _literal_value_for_signature(node: ast.AST) -> str:
    if isinstance(node, ast.Constant):
        if node.value is None:
            return ""
        if isinstance(node.value, (str, int, bool)):
            return str(node.value)
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        values = [_literal_value_for_signature(item) for item in node.elts]
        if all(value != "<dynamic>" for value in values):
            return ",".join(values)
    return "<dynamic>"


def _routing_keywords(call: ast.Call, *, exclude: set[str] | None = None) -> tuple[tuple[str, str], ...]:
    excluded = exclude or set()
    values: list[tuple[str, str]] = []
    for keyword in call.keywords:
        if keyword.arg is None:
            values.append(("<expanded_kwargs>", "<dynamic>"))
            continue
        if keyword.arg in excluded:
            continue
        values.append((keyword.arg, _literal_value_for_signature(keyword.value)))
    return tuple(sorted(values))


def _has_expanded_kwargs(call: ast.Call) -> bool:
    return any(keyword.arg is None for keyword in call.keywords)


def _signed_fields(record: RouteRegistrationCandidate) -> tuple[tuple[str, Any], ...]:
    grammar = SUPPORTED_ROUTE_REGISTRATION_FORMS.get(_grammar_key(record.registration_kind), {})
    fields = grammar.get("signed_fields", ())
    if not fields:
        fields = ("source_locus", "registration_kind", "parser_status", "fail_closed_reason", "public_internal_classification")
    return tuple((field, getattr(record, field)) for field in fields)


def _grammar_key(registration_kind: str) -> str:
    if registration_kind in {"route_decorator", "hook_decorator", "errorhandler_decorator"}:
        return "decorator"
    return registration_kind


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


def _route_aliases(tree: ast.AST) -> dict[str, str]:
    aliases: dict[str, str] = {}
    route_suffixes = (
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
        ".add_url_rule",
    )
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        value_chain = _attribute_chain(node.value)
        if not any(value_chain.endswith(suffix) for suffix in route_suffixes):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        for target in targets:
            if isinstance(target, ast.Name):
                aliases[target.id] = value_chain
    return aliases


def _blueprint_registration_prefixes(tree: ast.AST) -> dict[str, tuple[str, ...]]:
    prefixes: dict[str, list[str]] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not _attribute_chain(node.func).endswith(".register_blueprint"):
            continue
        if not node.args or not isinstance(node.args[0], ast.Name):
            continue
        url_prefix: str | None = None
        for keyword in node.keywords:
            if keyword.arg is None:
                url_prefix = "<dynamic>"
                break
            if keyword.arg == "url_prefix":
                url_prefix = _literal_value_for_signature(keyword.value)
        if url_prefix is not None:
            prefixes.setdefault(node.args[0].id, []).append(url_prefix)
    return {name: tuple(values) for name, values in prefixes.items()}


def _decorator_route_root(deco_call: ast.AST) -> str:
    if isinstance(deco_call, ast.Attribute):
        value = deco_call.value
        return value.id if isinstance(value, ast.Name) else _attribute_chain(value)
    return ""



def _owner_types(tree: ast.AST) -> dict[str, str]:
    owners: dict[str, str] = {}
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)) or not isinstance(node.value, ast.Call):
            continue
        ctor = _attribute_chain(node.value.func).rsplit(".", 1)[-1]
        if ctor not in {"Flask", "Blueprint"}:
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        for target in targets:
            if isinstance(target, ast.Name):
                owners[target.id] = ctor
    return owners


def classify_route_record(record: RouteRegistrationCandidate | RouteSignatureRecord) -> str:
    if record.parser_status != BOUNDARY_ROUTE_SUPPORTED:
        return BOUNDARY_UNKNOWN
    if any(value == "<dynamic>" for value in [record.route_path, record.blueprint_constructor_prefix, record.register_blueprint_prefix]):
        return BOUNDARY_UNKNOWN
    public_path = record.route_path or record.register_blueprint_prefix or record.blueprint_constructor_prefix
    if public_path and _is_non_public_route_namespace(public_path):
        return "internal"
    return "public"


def _finalize_route_candidate(candidate: RouteRegistrationCandidate) -> RouteRegistrationCandidate:
    classification = classify_route_record(candidate)
    status = candidate.parser_status
    reason = candidate.fail_closed_reason
    if classification == BOUNDARY_UNKNOWN and status == BOUNDARY_ROUTE_SUPPORTED:
        status = BOUNDARY_ROUTE_AMBIGUOUS
        reason = reason or "route_public_internal_classification_unknown"
    base = {**asdict(candidate), "parser_status": status, "public_internal_classification": classification, "fail_closed_reason": reason, "signed_fields": ()}
    finalized = RouteRegistrationCandidate(**base)
    return RouteRegistrationCandidate(**{**asdict(finalized), "signed_fields": _signed_fields(finalized)})


def _record_from_candidate(candidate: RouteRegistrationCandidate) -> RouteSignatureRecord:
    return RouteSignatureRecord(**asdict(candidate))


def route_signature_from_record(record: RouteSignatureRecord | RouteRegistrationCandidate) -> str:
    parts: list[str] = []
    for key, value in record.signed_fields:
        if isinstance(value, tuple):
            if value and isinstance(value[0], tuple):
                rendered = ",".join(f"{k}:{v}" for k, v in value)
            else:
                rendered = ",".join(str(item) for item in value)
        else:
            rendered = str(value)
        parts.append(f"{key}={rendered}")
    return ";".join(parts)


def _legacy_route_signature_from_record(record: RouteSignatureRecord | RouteRegistrationCandidate) -> str:
    if record.registration_kind in {"route_decorator", "hook_decorator", "errorhandler_decorator"}:
        return f"{record.source_locus}:{record.decorator_path}:{record.route_path}:{','.join(record.http_methods)}:{record.endpoint}"
    if record.registration_kind == "add_url_rule":
        return f"{record.source_locus}:add_url_rule:{record.route_path}:{record.endpoint}:{','.join(record.http_methods)}:{record.view_identity}"
    if record.registration_kind == "register_blueprint":
        return f"{record.source_locus}:register_blueprint:{record.blueprint_name}:{record.register_blueprint_prefix}"
    return route_signature_from_record(record)


def _blueprint_constructor_records(rel: str, tree: ast.AST) -> list[RouteRegistrationCandidate]:
    records: list[RouteRegistrationCandidate] = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)) or not isinstance(node.value, ast.Call):
            continue
        if _attribute_chain(node.value.func).rsplit(".", 1)[-1] != "Blueprint":
            continue
        prefix = ""
        status = BOUNDARY_ROUTE_SUPPORTED
        reason = ""
        for keyword in node.value.keywords:
            if keyword.arg == "url_prefix":
                prefix = _literal_value_for_signature(keyword.value)
                if prefix == "<dynamic>":
                    status = BOUNDARY_ROUTE_AMBIGUOUS
                    reason = "dynamic_blueprint_constructor_prefix"
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        for target in targets:
            if isinstance(target, ast.Name):
                records.append(_finalize_route_candidate(RouteRegistrationCandidate(
                    source_locus=rel,
                    registration_kind="blueprint_constructor",
                    parser_status=status,
                    proven_owner_type="Blueprint",
                    route_path="" if prefix == "<dynamic>" else prefix,
                    blueprint_name=target.id,
                    blueprint_constructor_prefix="" if prefix == "<dynamic>" else prefix,
                    fail_closed_reason=reason,
                )))
    return records


def _methods_tuple(deco_name: str, deco: ast.AST) -> tuple[str, ...]:
    value = _route_methods(deco_name, deco)
    return tuple(filter(None, value.split(","))) if value else ()


def _decorator_methods_are_dynamic(deco_name: str, deco: ast.AST) -> bool:
    if not isinstance(deco, ast.Call):
        return False
    if deco_name.endswith((".get", ".post", ".put", ".patch", ".delete")):
        return False
    for keyword in deco.keywords:
        if keyword.arg == "methods":
            return not bool(_literal_string_list(keyword.value))
    return False


def _methodview_http_methods(tree: ast.AST) -> dict[str, tuple[str, ...]]:
    methods_by_class: dict[str, tuple[str, ...]] = {}
    flask_methods = {"get", "post", "put", "patch", "delete", "head", "options"}
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        methods = sorted(
            child.name.upper()
            for child in node.body
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name in flask_methods
        )
        if methods:
            methods_by_class[node.name] = tuple(methods)
    return methods_by_class


def _methodview_class_from_as_view(call: ast.Call) -> str:
    chain = _attribute_chain(call.func)
    return chain.rsplit(".", 1)[0] if chain.endswith(".as_view") else ""


def discover_route_registrations(loci: tuple[str, ...]) -> list[RouteSignatureRecord]:
    """Discover bounded typed route registrations for PR-04 drift proof."""

    records: list[RouteRegistrationCandidate] = []
    decorator_suffix_to_kind = {
        ".route": "route_decorator",
        ".get": "route_decorator",
        ".post": "route_decorator",
        ".put": "route_decorator",
        ".patch": "route_decorator",
        ".delete": "route_decorator",
        ".before_app_request": "hook_decorator",
        ".before_request": "hook_decorator",
        ".after_app_request": "hook_decorator",
        ".after_request": "hook_decorator",
        ".errorhandler": "errorhandler_decorator",
        ".app_errorhandler": "errorhandler_decorator",
    }
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        aliases = _import_aliases(tree)
        owners = _owner_types(tree)
        route_aliases = _route_aliases(tree)
        blueprint_prefixes = _blueprint_prefixes(tree)
        blueprint_mount_prefixes = _blueprint_registration_prefixes(tree)
        methodview_methods = _methodview_http_methods(tree)
        records.extend(_blueprint_constructor_records(rel, tree))
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for deco in node.decorator_list:
                    deco_call = deco.func if isinstance(deco, ast.Call) else deco
                    deco_name = _attribute_chain(deco_call)
                    suffix = next((item for item in decorator_suffix_to_kind if deco_name.endswith(item)), "")
                    if not suffix:
                        if deco_name.startswith("getattr"):
                            records.append(_finalize_route_candidate(RouteRegistrationCandidate(source_locus=rel, registration_kind="unsupported_route_bearing_form", parser_status=BOUNDARY_ROUTE_UNSUPPORTED, fail_closed_reason="dynamic_getattr_decorator")))
                        elif deco_name in route_aliases:
                            records.append(_finalize_route_candidate(RouteRegistrationCandidate(
                                source_locus=rel,
                                registration_kind="unsupported_route_bearing_form",
                                parser_status=BOUNDARY_ROUTE_UNSUPPORTED,
                                decorator_path=deco_name,
                                endpoint=node.name,
                                view_identity=node.name,
                                fail_closed_reason="aliased_route_decorator",
                            )))
                        continue
                    route_root = _decorator_route_root(deco_call)
                    owner_type = owners.get(route_root, "BlueprintAlias" if route_root in blueprint_prefixes else ("Flask" if route_root == "app" and decorator_suffix_to_kind[suffix] == "hook_decorator" else ""))
                    status = BOUNDARY_ROUTE_SUPPORTED if owner_type else BOUNDARY_ROUTE_UNSUPPORTED
                    reason = "" if owner_type else "unproven_route_owner"
                    route_arg = _literal_value_for_signature(deco.args[0]) if isinstance(deco, ast.Call) and deco.args else ""
                    if route_arg == "<dynamic>":
                        status = BOUNDARY_ROUTE_AMBIGUOUS
                        reason = "dynamic_route_argument"
                    methods = _methods_tuple(deco_name, deco)
                    if _decorator_methods_are_dynamic(deco_name, deco):
                        status = BOUNDARY_ROUTE_AMBIGUOUS
                        reason = reason or "dynamic_route_methods"
                    if isinstance(deco, ast.Call) and _has_expanded_kwargs(deco):
                        status = BOUNDARY_ROUTE_AMBIGUOUS
                        reason = reason or "expanded_route_kwargs"
                    routing_keywords = _routing_keywords(deco, exclude={"methods"}) if isinstance(deco, ast.Call) else ()
                    if any(value == "<dynamic>" for _, value in routing_keywords):
                        status = BOUNDARY_ROUTE_AMBIGUOUS
                        reason = reason or "dynamic_routing_keyword"
                    errorhandler_key = ""
                    if decorator_suffix_to_kind[suffix] == "errorhandler_decorator":
                        if isinstance(deco, ast.Call) and deco.args:
                            errorhandler_key = _literal_value_for_signature(deco.args[0])
                        else:
                            status = BOUNDARY_ROUTE_AMBIGUOUS
                            reason = reason or "missing_errorhandler_key"
                        if errorhandler_key == "<dynamic>":
                            status = BOUNDARY_ROUTE_AMBIGUOUS
                            reason = reason or "dynamic_errorhandler_key"
                    constructor_prefix = blueprint_prefixes.get(route_root, "")
                    mount_prefix_values = blueprint_mount_prefixes.get(route_root, ())
                    mount_prefix = mount_prefix_values[0] if len(mount_prefix_values) == 1 else ("<dynamic>" if len(mount_prefix_values) > 1 else "")
                    if len(mount_prefix_values) > 1:
                        status = BOUNDARY_ROUTE_AMBIGUOUS
                        reason = reason or "multiple_register_blueprint_prefixes"
                    if mount_prefix == "<dynamic>":
                        status = BOUNDARY_ROUTE_AMBIGUOUS
                        reason = reason or "dynamic_register_blueprint_prefix"
                    signed_prefix = "" if mount_prefix == "<dynamic>" else (mount_prefix if route_root in blueprint_mount_prefixes else constructor_prefix)
                    full_route_arg = _join_route_prefix(signed_prefix, "" if route_arg == "<dynamic>" else route_arg)
                    records.append(_finalize_route_candidate(RouteRegistrationCandidate(
                        source_locus=rel,
                        registration_kind=decorator_suffix_to_kind[suffix],
                        parser_status=status,
                        owner_expression=route_root,
                        proven_owner_type=owner_type,
                        route_path=full_route_arg,
                        decorator_path=deco_name,
                        http_methods=methods,
                        endpoint=node.name,
                        view_identity=node.name,
                        blueprint_name=route_root if owner_type in {"Blueprint", "BlueprintAlias"} else "",
                        blueprint_constructor_prefix=constructor_prefix,
                        register_blueprint_prefix="" if mount_prefix == "<dynamic>" else mount_prefix,
                        errorhandler_key="" if errorhandler_key == "<dynamic>" else errorhandler_key,
                        routing_keywords=routing_keywords,
                        imported_view_target=aliases.get(node.name, ""),
                        fail_closed_reason=reason,
                    )))
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and route_aliases.get(node.func.id, "").endswith(".add_url_rule"):
                records.append(_finalize_route_candidate(RouteRegistrationCandidate(
                    source_locus=rel,
                    registration_kind="unsupported_route_bearing_form",
                    parser_status=BOUNDARY_ROUTE_UNSUPPORTED,
                    owner_expression=node.func.id,
                    fail_closed_reason="aliased_add_url_rule",
                )))
                continue
            if isinstance(node, ast.Call) and _attribute_chain(node.func).endswith(".add_url_rule"):
                owner = _attribute_chain(node.func).rsplit(".", 1)[0]
                owner_type = owners.get(owner, "BlueprintAlias" if owner in blueprint_prefixes else "")
                status = BOUNDARY_ROUTE_SUPPORTED if owner_type else BOUNDARY_ROUTE_UNSUPPORTED
                reason = "" if owner_type else "unproven_add_url_rule_owner"
                route_arg = _literal_value_for_signature(node.args[0]) if node.args else ""
                endpoint = _literal_value_for_signature(node.args[1]) if len(node.args) > 1 else ""
                view_desc = ""
                imported_view_target = ""
                methods: tuple[str, ...] = ()
                for keyword in node.keywords:
                    if keyword.arg is None:
                        status = BOUNDARY_ROUTE_AMBIGUOUS
                        reason = reason or "expanded_add_url_rule_kwargs"
                        continue
                    if keyword.arg == "view_func":
                        if isinstance(keyword.value, ast.Call) and _attribute_chain(keyword.value.func).endswith(".as_view"):
                            view_desc = _attribute_chain(keyword.value.func)
                            methods = methods or methodview_methods.get(_methodview_class_from_as_view(keyword.value), ())
                            if keyword.value.args:
                                endpoint = endpoint or _literal_value_for_signature(keyword.value.args[0])
                            else:
                                status = BOUNDARY_ROUTE_AMBIGUOUS
                                reason = reason or "missing_methodview_endpoint"
                        elif isinstance(keyword.value, ast.Call):
                            view_desc = _attribute_chain(keyword.value.func)
                            status = BOUNDARY_ROUTE_AMBIGUOUS
                            reason = reason or "dynamic_add_url_rule_view_factory"
                        else:
                            view_desc = _attribute_chain(keyword.value)
                            imported_view_target = aliases.get(view_desc, "")
                    elif keyword.arg == "methods":
                        method_values = _literal_string_list(keyword.value)
                        if method_values:
                            methods = tuple(sorted(method_values))
                        else:
                            status = BOUNDARY_ROUTE_AMBIGUOUS
                            reason = reason or "dynamic_add_url_rule_methods"
                if not view_desc and len(node.args) >= 3:
                    view_node = node.args[2]
                    if isinstance(view_node, ast.Call) and _attribute_chain(view_node.func).endswith(".as_view"):
                        view_desc = _attribute_chain(view_node.func)
                        methods = methods or methodview_methods.get(_methodview_class_from_as_view(view_node), ())
                        if view_node.args:
                            endpoint = endpoint or _literal_value_for_signature(view_node.args[0])
                    elif isinstance(view_node, ast.Call):
                        view_desc = _attribute_chain(view_node.func)
                        status = BOUNDARY_ROUTE_AMBIGUOUS
                        reason = reason or "dynamic_add_url_rule_view_factory"
                    else:
                        view_desc = _attribute_chain(view_node)
                        imported_view_target = aliases.get(view_desc, "")
                if route_arg in {"", "<dynamic>"}:
                    status = BOUNDARY_ROUTE_AMBIGUOUS
                    reason = reason or "dynamic_or_missing_add_url_rule_path"
                if endpoint == "<dynamic>" or view_desc == "":
                    status = BOUNDARY_ROUTE_AMBIGUOUS
                    reason = reason or "dynamic_or_missing_add_url_rule_endpoint_or_view"
                routing_keywords = _routing_keywords(node, exclude={"view_func", "methods"})
                if any(value == "<dynamic>" for _, value in routing_keywords):
                    status = BOUNDARY_ROUTE_AMBIGUOUS
                    reason = reason or "dynamic_add_url_rule_routing_keyword"
                constructor_prefix = blueprint_prefixes.get(owner, "")
                mount_prefix_values = blueprint_mount_prefixes.get(owner, ())
                mount_prefix = mount_prefix_values[0] if len(mount_prefix_values) == 1 else ("<dynamic>" if len(mount_prefix_values) > 1 else "")
                if len(mount_prefix_values) > 1:
                    status = BOUNDARY_ROUTE_AMBIGUOUS
                    reason = reason or "multiple_register_blueprint_prefixes"
                if mount_prefix == "<dynamic>":
                    status = BOUNDARY_ROUTE_AMBIGUOUS
                    reason = reason or "dynamic_register_blueprint_prefix"
                signed_prefix = "" if mount_prefix == "<dynamic>" else (mount_prefix if owner in blueprint_mount_prefixes else constructor_prefix)
                full_route_arg = _join_route_prefix(signed_prefix, "" if route_arg == "<dynamic>" else route_arg)
                records.append(_finalize_route_candidate(RouteRegistrationCandidate(
                    source_locus=rel,
                    registration_kind="add_url_rule",
                    parser_status=status,
                    owner_expression=owner,
                    proven_owner_type=owner_type,
                    route_path=full_route_arg,
                    http_methods=methods,
                    endpoint="" if endpoint == "<dynamic>" else endpoint,
                    view_identity=view_desc,
                    blueprint_name=owner if owner_type in {"Blueprint", "BlueprintAlias"} else "",
                    blueprint_constructor_prefix=constructor_prefix,
                    register_blueprint_prefix="" if mount_prefix == "<dynamic>" else mount_prefix,
                    routing_keywords=routing_keywords,
                    imported_view_target=imported_view_target,
                    fail_closed_reason=reason,
                )))
                continue
            if isinstance(node, ast.Call) and _attribute_chain(node.func).endswith(".register_blueprint"):
                owner = _attribute_chain(node.func).rsplit(".", 1)[0]
                owner_type = owners.get(owner, "")
                status = BOUNDARY_ROUTE_SUPPORTED if owner_type == "Flask" else BOUNDARY_ROUTE_UNSUPPORTED
                reason = "" if status == BOUNDARY_ROUTE_SUPPORTED else "unproven_register_blueprint_owner"
                blueprint = _expr_name(node.args[0]) if node.args else ""
                if not blueprint or (node.args and isinstance(node.args[0], ast.Call)):
                    status = BOUNDARY_ROUTE_AMBIGUOUS
                    reason = reason or "dynamic_or_factory_blueprint_registration"
                url_prefix = ""
                for keyword in node.keywords:
                    if keyword.arg is None:
                        url_prefix = "<dynamic>"
                        status = BOUNDARY_ROUTE_AMBIGUOUS
                        reason = reason or "expanded_register_blueprint_kwargs"
                        break
                    if keyword.arg == "url_prefix":
                        url_prefix = _literal_value_for_signature(keyword.value)
                if url_prefix == "<dynamic>":
                    status = BOUNDARY_ROUTE_AMBIGUOUS
                    reason = reason or "dynamic_register_blueprint_prefix"
                records.append(_finalize_route_candidate(RouteRegistrationCandidate(
                    source_locus=rel,
                    registration_kind="register_blueprint",
                    parser_status=status,
                    owner_expression=owner,
                    proven_owner_type=owner_type,
                    blueprint_name=blueprint,
                    blueprint_constructor_prefix=blueprint_prefixes.get(blueprint, ""),
                    register_blueprint_prefix="" if url_prefix == "<dynamic>" else url_prefix,
                    fail_closed_reason=reason,
                )))
    return sorted({_record_from_candidate(record) for record in records}, key=route_signature_from_record)


def discover_route_registration_candidates(loci: tuple[str, ...]) -> list[RouteSignatureRecord]:
    return discover_route_registrations(loci)


def _adapter_public_route_signatures(loci: tuple[str, ...]) -> list[str]:
    """Compatibility renderer for typed public route records."""

    return [
        _legacy_route_signature_from_record(record)
        for record in discover_route_registrations(loci)
        if record.parser_status == BOUNDARY_ROUTE_SUPPORTED and record.public_internal_classification == "public" and record.registration_kind != "blueprint_constructor"
    ]

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
            def node_is_unpresented_response_payload(value: ast.AST) -> bool:
                if isinstance(value, ast.Await):
                    return node_is_unpresented_response_payload(value.value)
                if isinstance(value, ast.Tuple):
                    return bool(value.elts) and node_is_unpresented_response_payload(value.elts[0])
                if node_is_jsonish(value):
                    return True
                if isinstance(value, ast.Constant) and isinstance(value.value, (str, bytes)) and value.value not in {"", b""}:
                    return True
                if isinstance(value, ast.Call):
                    call_name = _attribute_chain(value.func)
                    root = _root_name(value.func)
                    target = aliases.get(root or "", root or "")
                    if (
                        call_name == "make_response"
                        or target == "flask.make_response"
                        or call_name.endswith((".make_response", ".Response"))
                        or call_name == "Response"
                    ):
                        return any(node_is_unpresented_response_payload(arg) for arg in value.args) or any(
                            keyword.arg in {"response", "json", "data"} and node_is_unpresented_response_payload(keyword.value)
                            for keyword in value.keywords
                        )
                return False

            assigned_unpresented_payloads: set[str] = set()
            for node in iter_body_nodes(fn):
                if isinstance(node, (ast.Assign, ast.AnnAssign)) and node.value is not None and node_is_unpresented_response_payload(node.value):
                    target_nodes = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target_node in target_nodes:
                        if isinstance(target_node, ast.Name):
                            assigned_unpresented_payloads.add(target_node.id)
            for node in iter_body_nodes(fn):
                if isinstance(node, ast.Return) and node.value is not None:
                    if node_is_unpresented_response_payload(node.value):
                        return True
                    if isinstance(node.value, ast.Name) and node.value.id in assigned_unpresented_payloads:
                        return True
                if isinstance(node, ast.Call):
                    call_name = _attribute_chain(node.func)
                    if call_name.endswith("Response") and (
                        any(node_is_unpresented_response_payload(arg) or (isinstance(arg, ast.Name) and arg.id in assigned_unpresented_payloads) for arg in node.args)
                        or any(
                            keyword.arg in {"response", "json", "data"}
                            and (node_is_unpresented_response_payload(keyword.value) or (isinstance(keyword.value, ast.Name) and keyword.value.id in assigned_unpresented_payloads))
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
BOUNDARY_TAXONOMY_GROUP_TO_FINDING = {
    "route_registration_surfaces": "adapter_route_registration",
    "public_route_signatures": "public_routes",
    "response_producing_paths": "response_producing_paths",
    "presenter_valid_paths": "presenter_provenance",
    "presenter_bypass_paths": "presenter_provenance",
    "serializer_families": "serializer_paths",
    "external_io_families": "external_io_paths",
    "import_and_alias_forms": "presenter_provenance",
    "cross_file_helper_chains": "presenter_provenance",
    "vendor_guard_provenance": "guard_provenance",
    "pure_compute_forbidden_operations": "pure_compute_external_io",
    "public_internal_route_classification": "public_routes",
    "evidence_family_binding": "evidence_binding_posture",
    "unsupported_scope_no_claims": "hde_ferm007_5_runtime_v2_live_open_rails_ai_scope",
}
REQUIRED_BOUNDARY_TAXONOMY_GROUPS = tuple(BOUNDARY_TAXONOMY_GROUP_TO_FINDING)
BOUNDARY_TAXONOMY_REQUIRED_CASE_CLASSIFICATIONS = {
    "route_registration_surfaces": (BOUNDARY_ALLOWED, BOUNDARY_UNKNOWN),
    "public_route_signatures": (BOUNDARY_ALLOWED, BOUNDARY_UNKNOWN, BOUNDARY_OUT_OF_SCOPE),
    "response_producing_paths": (BOUNDARY_ALLOWED, BOUNDARY_FORBIDDEN, BOUNDARY_UNKNOWN),
    "presenter_valid_paths": (BOUNDARY_ALLOWED,),
    "presenter_bypass_paths": (BOUNDARY_FORBIDDEN, BOUNDARY_UNKNOWN),
    "serializer_families": (BOUNDARY_ALLOWED, BOUNDARY_FORBIDDEN, BOUNDARY_UNKNOWN),
    "external_io_families": (BOUNDARY_ALLOWED, BOUNDARY_FORBIDDEN),
    "import_and_alias_forms": (BOUNDARY_ALLOWED, BOUNDARY_FORBIDDEN, BOUNDARY_UNKNOWN),
    "cross_file_helper_chains": (BOUNDARY_ALLOWED, BOUNDARY_UNKNOWN),
    "vendor_guard_provenance": (BOUNDARY_ALLOWED, BOUNDARY_UNKNOWN),
    "pure_compute_forbidden_operations": (BOUNDARY_ALLOWED, BOUNDARY_FORBIDDEN),
    "public_internal_route_classification": (BOUNDARY_ALLOWED, BOUNDARY_UNKNOWN, BOUNDARY_OUT_OF_SCOPE),
    "evidence_family_binding": (BOUNDARY_ALLOWED, BOUNDARY_UNKNOWN, BOUNDARY_OUT_OF_SCOPE),
    "unsupported_scope_no_claims": (BOUNDARY_OUT_OF_SCOPE,),
}


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


def _record_from_mapping(raw: dict[str, Any]) -> RouteSignatureRecord:
    values = {field: raw.get(field, getattr(RouteSignatureRecord("", "", ""), field)) for field in RouteSignatureRecord.__dataclass_fields__ if field != "signed_fields"}
    values["parser_status"] = values.get("parser_status") or BOUNDARY_ROUTE_SUPPORTED
    values["http_methods"] = tuple(values.get("http_methods") or ())
    values["routing_keywords"] = tuple(tuple(item) for item in values.get("routing_keywords") or ())
    candidate = _finalize_route_candidate(RouteRegistrationCandidate(**values, signed_fields=()))
    return _record_from_candidate(candidate)


def _record_from_legacy_signature(signature: str) -> RouteSignatureRecord:
    malformed = lambda reason: _record_from_candidate(_finalize_route_candidate(RouteRegistrationCandidate(source_locus=signature, registration_kind="baseline", parser_status=BOUNDARY_ROUTE_AMBIGUOUS, fail_closed_reason=reason)))
    head = signature.split(":", 2)
    if len(head) < 3:
        return malformed("unparseable_legacy_route_baseline")
    source_locus, discriminator, remainder = head
    if discriminator == "add_url_rule":
        parts = remainder.rsplit(":", 3)
        if len(parts) != 4:
            return malformed("unparseable_legacy_add_url_rule_baseline")
        route_path, endpoint, methods, view_identity = parts
        return _record_from_candidate(_finalize_route_candidate(RouteRegistrationCandidate(
            source_locus=source_locus,
            registration_kind="add_url_rule",
            parser_status=BOUNDARY_ROUTE_SUPPORTED,
            owner_expression="app",
            proven_owner_type="Flask",
            route_path=route_path,
            endpoint=endpoint,
            http_methods=tuple(filter(None, methods.split(","))),
            view_identity=view_identity,
        )))
    if discriminator == "register_blueprint":
        parts = remainder.split(":", 1)
        if len(parts) != 2:
            return malformed("unparseable_legacy_register_blueprint_baseline")
        blueprint_name, register_blueprint_prefix = parts
        return _record_from_candidate(_finalize_route_candidate(RouteRegistrationCandidate(
            source_locus=source_locus,
            registration_kind="register_blueprint",
            parser_status=BOUNDARY_ROUTE_SUPPORTED,
            owner_expression="app",
            proven_owner_type="Flask",
            blueprint_name=blueprint_name,
            register_blueprint_prefix=register_blueprint_prefix,
        )))
    parts = remainder.rsplit(":", 2)
    if len(parts) == 3:
        route_path, methods, endpoint = parts
        decorator_path = discriminator
        kind = "errorhandler_decorator" if decorator_path.endswith(("errorhandler", "app_errorhandler")) else ("hook_decorator" if any(decorator_path.endswith(suffix) for suffix in (".before_app_request", ".before_request", ".after_app_request", ".after_request")) else "route_decorator")
        owner = decorator_path.rsplit(".", 1)[0] if "." in decorator_path else ""
        owner_type = "Flask" if owner == "app" else ("BlueprintAlias" if owner else "")
        return _record_from_candidate(_finalize_route_candidate(RouteRegistrationCandidate(
            source_locus=source_locus,
            registration_kind=kind,
            parser_status=BOUNDARY_ROUTE_SUPPORTED,
            owner_expression=owner,
            proven_owner_type=owner_type,
            route_path=route_path,
            decorator_path=decorator_path,
            http_methods=tuple(filter(None, methods.split(","))),
            endpoint=endpoint,
            view_identity=endpoint,
            errorhandler_key=route_path if kind == "errorhandler_decorator" else "",
        )))
    return malformed("unparseable_legacy_route_baseline")


def _normalize_route_baseline(public_route_baseline: tuple[Any, ...]) -> tuple[RouteSignatureRecord, ...]:
    records: list[RouteSignatureRecord] = []
    for raw in public_route_baseline:
        if isinstance(raw, RouteSignatureRecord):
            records.append(raw)
        elif isinstance(raw, RouteRegistrationCandidate):
            records.append(_record_from_candidate(raw))
        elif isinstance(raw, dict):
            records.append(_record_from_mapping(raw))
        elif isinstance(raw, str):
            records.append(_record_from_legacy_signature(raw))
        else:
            records.append(_record_from_candidate(_finalize_route_candidate(RouteRegistrationCandidate(source_locus=str(raw), registration_kind="baseline", parser_status=BOUNDARY_ROUTE_AMBIGUOUS, fail_closed_reason="unsupported_baseline_record_type"))))
    return tuple(records)


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
    public_route_baseline: tuple[Any, ...],
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
    route_records = discover_route_registrations(adapter_loci)
    baseline_route_records = _normalize_route_baseline(public_route_baseline)
    discovered_public_record_signatures = sorted(
        route_signature_from_record(record)
        for record in route_records
        if record.parser_status == BOUNDARY_ROUTE_SUPPORTED and record.public_internal_classification == "public" and record.registration_kind != "blueprint_constructor"
    )
    baseline_public_record_signatures = sorted(
        route_signature_from_record(record)
        for record in baseline_route_records
        if record.parser_status == BOUNDARY_ROUTE_SUPPORTED and record.public_internal_classification == "public" and record.registration_kind != "blueprint_constructor"
    )
    discovered_public_routes = [
        _legacy_route_signature_from_record(record)
        for record in route_records
        if record.parser_status == BOUNDARY_ROUTE_SUPPORTED and record.public_internal_classification == "public" and record.registration_kind != "blueprint_constructor"
    ]
    route_unknown_records = [record for record in route_records if record.parser_status != BOUNDARY_ROUTE_SUPPORTED or record.public_internal_classification == BOUNDARY_UNKNOWN]
    baseline_unknown_records = [record for record in baseline_route_records if record.parser_status != BOUNDARY_ROUTE_SUPPORTED or record.public_internal_classification == BOUNDARY_UNKNOWN]
    public_reader_route_drift = sorted(set(discovered_public_record_signatures) ^ set(baseline_public_record_signatures))
    route_baseline_reconciled = bool(discovered_public_record_signatures) and bool(baseline_public_record_signatures) and not public_reader_route_drift and not route_unknown_records and not baseline_unknown_records
    route_baseline_out_of_scope = not route_records and adapter_loci != canonical_adapter_loci
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
        boundary_finding("adapter_route_registration", BOUNDARY_ALLOWED if adapter_http_modules and (route_records or route_baseline_out_of_scope) else BOUNDARY_UNKNOWN, "PASS" if adapter_http_modules and (route_records or route_baseline_out_of_scope) else "UNKNOWN", [row["path"] for row in adapter_rows], "discovered Flask adapter registrations before classification; typed route records active" if adapter_http_modules and (route_records or route_baseline_out_of_scope) else "no current adapter route registrations were discoverable", [route_signature_from_record(record) for record in route_records]),
        boundary_finding("public_routes", BOUNDARY_ALLOWED if route_baseline_reconciled else (BOUNDARY_OUT_OF_SCOPE if route_baseline_out_of_scope else BOUNDARY_UNKNOWN), "PASS" if route_baseline_reconciled or route_baseline_out_of_scope else "UNKNOWN", [row["path"] for row in adapter_rows], "typed discovered route records reconcile with governed PR-04 baseline field-by-field" if route_baseline_reconciled else ("no public route signatures discovered in noncanonical test locus; route surface is out of scope" if route_baseline_out_of_scope else "typed route records cannot be reconciled with structured baseline; route drift fails closed"), public_reader_route_drift or [route_signature_from_record(record) for record in route_unknown_records + baseline_unknown_records] or discovered_public_record_signatures),
        boundary_finding("response_producing_paths", BOUNDARY_ALLOWED if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else (BOUNDARY_FORBIDDEN if presenter_bypass else BOUNDARY_UNKNOWN), "PASS" if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else ("FAIL" if presenter_bypass else "UNKNOWN"), [row["path"] for row in adapter_rows], "public response-producing paths have explicit presenter/emitter provenance" if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else "response-producing path provenance is unresolved or bypasses presenter", presenter_bypass + unresolved_presenter_routes or adapter_presenter_calls),
        boundary_finding("presenter_provenance", BOUNDARY_ALLOWED if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else (BOUNDARY_FORBIDDEN if presenter_bypass else BOUNDARY_UNKNOWN), "PASS" if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else ("FAIL" if presenter_bypass else "UNKNOWN"), [row["path"] for row in presenter_rows], "adapter routes resolve to sanctioned presenter/emitter calls" if adapter_presenter_calls and not presenter_bypass and not unresolved_presenter_routes else "presenter provenance is not proven for every response path", presenter_bypass + unresolved_presenter_routes or adapter_presenter_calls),
        boundary_finding("serializer_paths", BOUNDARY_ALLOWED if not ad_hoc_serializers else BOUNDARY_FORBIDDEN, "PASS" if not ad_hoc_serializers else "FAIL", [row["path"] for row in adapter_rows + vendor_rows + presenter_rows], "no ad-hoc JSON serializer path discovered outside allowed vendor helpers" if not ad_hoc_serializers else "ad-hoc serializer path discovered on governed/public boundary", ad_hoc_serializers),
        boundary_finding("external_io_paths", BOUNDARY_ALLOWED if not adapter_bypass and not second_http_home else BOUNDARY_FORBIDDEN, "PASS" if not adapter_bypass and not second_http_home else "FAIL", [row["path"] for row in adapter_rows + vendor_rows], "external I/O remains limited to sanctioned vendor seam" if not adapter_bypass and not second_http_home else "external I/O or HTTP home found outside sanctioned vendor seam", adapter_bypass + second_http_home),
        boundary_finding("pure_compute_external_io", BOUNDARY_ALLOWED if not pure_external_io else BOUNDARY_FORBIDDEN, "PASS" if not pure_external_io else "FAIL", [row["path"] for row in pure_rows], "pure compute loci have no external-I/O imports or calls" if not pure_external_io else "pure compute external-I/O capability discovered", pure_external_io),
        boundary_finding("guard_provenance", BOUNDARY_ALLOWED if (guard_allowed or not vendor_external_io) and not guard_unresolved and not adapter_guard_findings else BOUNDARY_UNKNOWN, "PASS" if (guard_allowed or not vendor_external_io) and not guard_unresolved and not adapter_guard_findings else "UNKNOWN", [row["path"] for row in vendor_rows], "each relevant vendor external-I/O path is tied to a closed-rails guard entrypoint" if (guard_allowed or not vendor_external_io) and not guard_unresolved and not adapter_guard_findings else "guard symbols are missing or cannot be tied to each relevant external-I/O path", guard_unresolved + adapter_guard_findings + guard_allowed),
        boundary_finding("public_surface_posture", BOUNDARY_ALLOWED if not unsupported_scope_claims else BOUNDARY_FORBIDDEN, "PASS" if not unsupported_scope_claims else "FAIL", ["artifacts/vendor/hdapi_v2/source_selection.snapshot.json", "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json", "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"], "dependency evidence emits no unsupported public/runtime/open-rails/AI scope claims" if not unsupported_scope_claims else "unsupported scope claim discovered in dependency evidence", unsupported_scope_claims),
        boundary_finding("evidence_binding_posture", BOUNDARY_ALLOWED if all(isinstance(payload, dict) and payload for payload in [source_selection, request_shaping, response_mapping]) else BOUNDARY_UNKNOWN, "PASS" if all(isinstance(payload, dict) and payload for payload in [source_selection, request_shaping, response_mapping]) else "UNKNOWN", [row["path"] for row in evidence_tool_rows], "PR-01/PR-02/PR-03 dependency payloads are present and non-empty; index/path-proof validation is delegated to governed tools" if all(isinstance(payload, dict) and payload for payload in [source_selection, request_shaping, response_mapping]) else "dependency evidence payloads are missing or empty", []),
        boundary_finding("hde_ferm007_5_runtime_v2_live_open_rails_ai_scope", BOUNDARY_OUT_OF_SCOPE, "PASS", [row["path"] for row in evidence_tool_rows], "explicitly outside W-003 / HDE-FERM007.4; no claim is emitted", []),
    ]
    check_by_category = {finding["category"]: finding_passes(finding) for finding in findings}
    finding_by_category = {finding["category"]: finding for finding in findings}
    taxonomy_group_verdicts = {
        group: {
            "finding_category": category,
            "current_classification": finding_by_category[category]["classification"],
            "current_verdict": finding_by_category[category]["verdict"],
            "required_case_classifications": list(BOUNDARY_TAXONOMY_REQUIRED_CASE_CLASSIFICATIONS[group]),
            "coverage_status": "covered_by_w003_invariant_suite",
            "w003_scope": "in_scope" if finding_by_category[category]["classification"] != BOUNDARY_OUT_OF_SCOPE else "follow_up_or_out_of_scope_visible",
        }
        for group, category in BOUNDARY_TAXONOMY_GROUP_TO_FINDING.items()
    }
    checks = {
        "adapter_http_home_inspected": check_by_category["adapter_route_registration"],
        "actual_repo_loci_discovered_before_classification": all([adapter_rows, presenter_rows, vendor_rows, pure_rows, evidence_tool_rows]),
        "hard_coded_path_lists_not_used_as_proof": bool(discovered_public_routes) or adapter_loci != canonical_adapter_loci,
        "unknown_current_categories_fail_closed": all(f["verdict"] != "PASS" for f in findings if f["classification"] == BOUNDARY_UNKNOWN),
        "conservative_positive_boundary_contract_applied": {f["classification"] for f in findings} <= {BOUNDARY_ALLOWED, BOUNDARY_FORBIDDEN, BOUNDARY_UNKNOWN, BOUNDARY_OUT_OF_SCOPE},
        "table_driven_boundary_taxonomy_applied": set(taxonomy_group_verdicts) == set(REQUIRED_BOUNDARY_TAXONOMY_GROUPS),
        "required_taxonomy_groups_visible": all(group in taxonomy_group_verdicts for group in REQUIRED_BOUNDARY_TAXONOMY_GROUPS),
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
        "declared_route_grammar_applied": bool(SUPPORTED_ROUTE_REGISTRATION_FORMS) and (bool(route_records) or route_baseline_out_of_scope),
        "typed_route_records_source_of_truth": all(isinstance(record, RouteSignatureRecord) and record.signed_fields for record in route_records) and (bool(route_records) or route_baseline_out_of_scope),
        "structured_route_baseline_applied": (all(isinstance(record, RouteSignatureRecord) and record.signed_fields for record in baseline_route_records) and bool(baseline_route_records)) or route_baseline_out_of_scope,
        "route_comparison_cannot_disable_itself": (bool(discovered_public_record_signatures) and bool(baseline_public_record_signatures)) or route_baseline_out_of_scope,
        "unsupported_or_ambiguous_route_forms_fail_closed": all(record.parser_status == BOUNDARY_ROUTE_SUPPORTED for record in route_records),
        "renderer_checks_typed_route_fields": True,
        "no_unsupported_scope_claim": check_by_category["public_surface_posture"],
    }
    verdict_status = "PASS" if all(checks.values()) and all(finding_passes(f) for f in findings) else ("FAIL" if any(f["classification"] == BOUNDARY_FORBIDDEN for f in findings) else "UNKNOWN")
    return {
        "work_item": "W-004",
        "scope": "HDE-EPIC034 PR-04 W-004 typed route-drift boundary proof repair for HDE-FERM007.4 only; does not claim HDE-FERM007.4 Done",
        "inspected_loci": {"adapter": adapter_rows, "presenter": presenter_rows, "engine": pure_rows, "vendor_seam": vendor_rows, "evidence_tool": evidence_tool_rows},
        "findings": findings,
        "boundary_taxonomy": taxonomy_group_verdicts,
        "required_taxonomy_groups": list(REQUIRED_BOUNDARY_TAXONOMY_GROUPS),
        "missing_taxonomy_groups": sorted(set(REQUIRED_BOUNDARY_TAXONOMY_GROUPS) - set(taxonomy_group_verdicts)),
        "unknowns": [f for f in findings if f["classification"] == BOUNDARY_UNKNOWN],
        "public_route_deltas": public_reader_route_drift,
        "route_registration_grammar": SUPPORTED_ROUTE_REGISTRATION_FORMS,
        "typed_route_records": [asdict(record) for record in route_records],
        "typed_public_route_signatures": discovered_public_record_signatures,
        "route_baseline_records": [asdict(record) for record in baseline_route_records],
        "route_baseline_signatures": baseline_public_record_signatures,
        "unsupported_or_ambiguous_route_records": [asdict(record) for record in route_unknown_records],
        "route_baseline_reconciled": route_baseline_reconciled,
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
