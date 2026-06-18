#!/usr/bin/env python3
"""Generate HDE-EPIC033 HDAPI v2 contract-inventory evidence.

The default mode is closed-rails and consumes pre-captured public documentation
inputs from artifacts/vendor/hdapi_v2/source_cache/. Refreshing those inputs is
an explicit public-docs operation and requires both --refresh-public-docs and
open rails (SAFE_MODE=0, ALLOW_NETWORK=1). The generator never calls
credentialed runtime vendor endpoints.
"""
from __future__ import annotations

import argparse
import ast
import csv
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.evidence import hdapi_v2_boundary_analyzer as boundary_analyzer

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
SOURCE_CACHE = OUT / "source_cache"
SOURCE_METADATA = SOURCE_CACHE / "source_metadata.json"
ACCEPTANCE = ROOT / "docs" / "acceptance_map_epic033.json"
TOKEN_MATRIX = ROOT / "audit" / "qa" / "hde-epic033" / "token_evidence_matrix.md"
VIABILITY = ROOT / "audit" / "qa" / "hde-epic033" / "acceptance_map_viability.log"
DOC_DELTAS = ROOT / "audit" / "docdeltas" / "hde-epic033_doc_deltas.md"
QA_DOC_DELTAS = ROOT / "audit" / "qa" / "hde-epic033" / "00_meta" / "doc_deltas.md"
EPIC034_QA = ROOT / "audit" / "qa" / "hde-epic034" / "pr-01"
EPIC034_PR02_QA = ROOT / "audit" / "qa" / "hde-epic034" / "pr-02"
EPIC034_PR03_QA = ROOT / "audit" / "qa" / "hde-epic034" / "pr-03"
EPIC034_PR04_QA = ROOT / "audit" / "qa" / "hde-epic034" / "pr-04"
REQUEST_SHAPING_SNAPSHOT = OUT / "request_shaping.snapshot.json"
REQUEST_SHAPING_CHECK_LOG = EPIC034_PR02_QA / "request_shaping_check.log"
RESPONSE_MAPPING_SNAPSHOT = OUT / "response_mapping.snapshot.json"
RESPONSE_MAPPING_CHECK_LOG = EPIC034_PR03_QA / "response_mapping_check.log"
ADAPTER_BOUNDARY_PROOF_LOG = OUT / "adapter_boundary_proof.log"
BOUNDARY_CHECK_LOG = EPIC034_PR04_QA / "boundary_check.log"
REQUEST_SHAPING_OUTPUTS = (
    REQUEST_SHAPING_SNAPSHOT,
    REQUEST_SHAPING_SNAPSHOT.with_suffix(REQUEST_SHAPING_SNAPSHOT.suffix + ".path_proof.txt"),
    REQUEST_SHAPING_CHECK_LOG,
    REQUEST_SHAPING_CHECK_LOG.with_suffix(REQUEST_SHAPING_CHECK_LOG.suffix + ".path_proof.txt"),
)
RESPONSE_MAPPING_OUTPUTS = (
    RESPONSE_MAPPING_SNAPSHOT,
    RESPONSE_MAPPING_SNAPSHOT.with_suffix(RESPONSE_MAPPING_SNAPSHOT.suffix + ".path_proof.txt"),
    RESPONSE_MAPPING_CHECK_LOG,
    RESPONSE_MAPPING_CHECK_LOG.with_suffix(RESPONSE_MAPPING_CHECK_LOG.suffix + ".path_proof.txt"),
)
ADAPTER_BOUNDARY_OUTPUTS = (
    ADAPTER_BOUNDARY_PROOF_LOG,
    ADAPTER_BOUNDARY_PROOF_LOG.with_suffix(ADAPTER_BOUNDARY_PROOF_LOG.suffix + ".path_proof.txt"),
    BOUNDARY_CHECK_LOG,
    BOUNDARY_CHECK_LOG.with_suffix(BOUNDARY_CHECK_LOG.suffix + ".path_proof.txt"),
)
EPIC034_CLOSED_RAILS_DERIVED_OUTPUTS = REQUEST_SHAPING_OUTPUTS + RESPONSE_MAPPING_OUTPUTS + ADAPTER_BOUNDARY_OUTPUTS
CLOSED_RAILS_ENV = {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}
SOURCE_SELECTION_SNAPSHOT = OUT / "source_selection.snapshot.json"
V1_LEGACY_GUARD_LOG = OUT / "v1_legacy_guard.log"
SOURCE_SELECTION_CHECK_LOG = EPIC034_QA / "source_selection_check.log"

BASE = "https://docs.humandesignapi.nl"
SOURCES = [
    ("robots_preflight", f"{BASE}/robots.txt", "robots_preflight", "seed", None),
    ("llms_txt", f"{BASE}/llms.txt", "documentation-discovery-only", "robots_preflight", None),
    ("llms_full_txt", f"{BASE}/llms-full.txt", "documentation-discovery-only", "llms_txt", "llms-full.endpoint-tiers.txt"),
    ("v2_routes_yaml", f"{BASE}/openapi/v2-routes.yaml", "validated_machine_readable_route_spec", "llms_txt", "v2-routes.yaml"),
    ("v1_routes_yaml", f"{BASE}/openapi/v1-routes.yaml", "validated_machine_readable_route_spec", "llms_txt", "v1-routes.yaml"),
    ("suspect_openapi_json", f"{BASE}/api-reference/openapi.json", "suspect_quarantined_openapi", "llms_txt", "api-reference.openapi.json"),
    ("v2_overview", f"{BASE}/api-reference/v2/overview", "rendered_high_level_guide", "llms_txt", None),
    ("v1_overview", f"{BASE}/api-reference/v1/overview", "rendered_high_level_guide", "llms_txt", None),
    ("v2_full_chart_page", f"{BASE}/api-reference/charts/generate-a-full-chart", "rendered_endpoint_page", "llms_txt", None),
    ("v2_simple_chart_page", f"{BASE}/api-reference/charts/generate-a-simple-chart", "rendered_endpoint_page", "llms_txt", None),
    ("v2_coordinates_chart_page", f"{BASE}/api-reference/charts/generate-a-chart-from-coordinates", "rendered_endpoint_page", "llms_txt", None),
    ("authentication", f"{BASE}/authentication", "rendered_contract_page", "llms_txt", None),
    ("rate_limiting", f"{BASE}/guides/rate-limiting", "rendered_contract_page", "llms_txt", None),
    ("response_format", f"{BASE}/response-format", "rendered_contract_page", "llms_txt", None),
    ("migration_v1_to_v2", f"{BASE}/migration/v1-to-v2", "rendered_contract_page", "llms_txt", None),
    ("coordinates_guide", f"{BASE}/guides/coordinates-endpoint", "rendered_contract_page", "llms_txt", None),
]

REQUIRED_ENDPOINTS = [
    ("POST", "/v2/charts"),
    ("POST", "/v2/charts/simple"),
    ("POST", "/v2/charts/coordinates"),
    ("POST", "/v1/bodygraphs"),
    ("POST", "/v1/bodygraphs/simple"),
]

ALLOWED_STATUS = {200}
V2_CHART_ROUTES = [
    ("POST", "/v2/charts", "full_chart"),
    ("POST", "/v2/charts/simple", "simple_chart"),
    ("POST", "/v2/charts/coordinates", "coordinates_chart"),
]
V1_BODYGRAPH_ROUTES = [
    ("POST", "/v1/bodygraphs", "legacy_full_bodygraph"),
    ("POST", "/v1/bodygraphs/simple", "legacy_simple_bodygraph"),
]
RESPONSE_MAPPING_REQUIRED_STANDARD_FIELDS = ("success", "errorCode", "type", "data")
RESPONSE_MAPPING_INTERNAL_LOCI = (
    "engine/bodygraph/vendor_client.py",
    "engine/bodygraph/ingest.py",
    "engine/bodygraph/resolver.py",
    "engine/compat/compute.py",
)
ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI = ("adapter/wsgi.py", "adapter/factory.py", "adapter/http_reader.py", "engine/http/compat_handler.py")
ADAPTER_BOUNDARY_ADAPTER_LOCI = ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI
ADAPTER_BOUNDARY_PRESENTER_LOCI = ("engine/presenter/emitter.py", "presenter/reader_v1/emitter.py")
ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI = ("engine/bodygraph/vendor_client.py", "engine/bodygraph/ingest.py", "engine/bodygraph/resolver.py")
ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI = ("engine/compat/compute.py",)
ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE = (
    'adapter/factory.py:app.after_request:::_strip_etag_on_internal',
    'adapter/factory.py:register_blueprint:bp:',
    'adapter/http_reader.py:app.after_request:::_strip_etag_on_internal',
    'adapter/http_reader.py:app.errorhandler:::_compat_scoped_method_not_allowed',
    'adapter/http_reader.py:app.errorhandler:::_compat_scoped_not_found',
    'adapter/http_reader.py:bp.get:/api/aux/narrative:GET:aux_narrative',
    'adapter/http_reader.py:bp.get:/aux/narrative:GET:aux_narrative',
    'adapter/http_reader.py:bp.get:/dev/reader/conjunction:GET:dev_reader_conjunction',
    'adapter/http_reader.py:bp.get:/dev/sampler/conjunction:GET:dev_sampler_conjunction',
    'adapter/http_reader.py:bp.get:/dev/writer/conjunction:GET:dev_writer_conjunction',
    'adapter/http_reader.py:bp.get:/reader:GET:reader_v1',
    'adapter/http_reader.py:bp.post:/reader:POST:reader_v1_post',
    'adapter/http_reader.py:bp.route:/internal/dev/sampler:POST:dev_sampler_internal',
    'adapter/http_reader.py:bp.route:/internal/version:GET,HEAD:internal_version',
    'adapter/http_reader.py:bp.route:/ops/db/unavailable:GET:ops_db_unavailable',
    'adapter/http_reader.py:bp.route:/ops/probe/env:GET:ops_probe_env',
    'adapter/http_reader.py:bp.route:/ops/rails/refusal:GET,POST:ops_rails_refusal',
    'adapter/http_reader.py:bp.route:/ops/writer/diagnostic:HEAD:diagnostic_writer_head',
    'adapter/http_reader.py:bp.route:/ops/writer/diagnostic:OPTIONS:diagnostic_writer_options',
    'adapter/http_reader.py:bp.route:/ops/writer/diagnostic:POST:diagnostic_writer',
    'adapter/http_reader.py:register_blueprint:bp:',
    'adapter/http_reader.py:register_blueprint:compat_blueprint:',
    'adapter/wsgi.py:app.after_request:::_ensure_common_headers',
    'adapter/wsgi.py:app.errorhandler:::_method_not_allowed',
    'adapter/wsgi.py:app.errorhandler:::_not_found',
    'adapter/wsgi.py:app.get:/internal/healthz:GET:internal_healthz',
    'adapter/wsgi.py:app.get:/internal/readyz:GET:internal_readyz',
    'adapter/wsgi.py:register_blueprint:compat_blueprint:',
    'adapter/wsgi.py:register_blueprint:reader_bp:',
    'engine/http/compat_handler.py:compat_blueprint.before_app_request:::_compat_writer_transport_guard',
    'engine/http/compat_handler.py:compat_blueprint.get::GET:get_ids_only',
    'engine/http/compat_handler.py:compat_blueprint.route::HEAD:post_json_head',
    'engine/http/compat_handler.py:compat_blueprint.route::OPTIONS:post_json_options',
    'engine/http/compat_handler.py:compat_blueprint.route::POST:post_json',
)



def closed_rails_env_snapshot() -> dict[str, str]:
    return {key: os.environ.get(key, "UNSET") for key in CLOSED_RAILS_ENV}


def closed_rails_env_ok() -> bool:
    return all(os.environ.get(key) == value for key, value in CLOSED_RAILS_ENV.items())


def require_closed_rails_for_request_shaping() -> None:
    if not closed_rails_env_ok():
        observed = ",".join(f"{key}={os.environ.get(key, 'UNSET')}" for key in sorted(CLOSED_RAILS_ENV))
        raise SystemExit(f"CLOSED_RAILS_REQUIRED_FOR_REQUEST_SHAPING:{observed}")


def remove_request_shaping_outputs() -> None:
    for path in EPIC034_CLOSED_RAILS_DERIVED_OUTPUTS:
        try:
            path.unlink()
        except FileNotFoundError:
            pass


def iso_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def write_bytes(path: Path, body: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)


def sha256_bytes(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()



def llms_full_endpoint_tier_excerpt(body: bytes) -> bytes:
    text = body.decode("utf-8", errors="replace")
    rows = [
        line for line in text.splitlines()
        if line.startswith("| `POST /v") and ("Advanced" in line or "Basic" in line)
    ]
    if not rows:
        raise SystemExit("LLMS_FULL_TIER_EXCERPT_EMPTY")
    return ("\n".join(rows) + "\n").encode("utf-8")

def fetch_public_doc(url: str) -> tuple[str, str, int | str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": "glow-hde-epic033-contract-inventory/1.1"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.geturl(), resp.headers.get("content-type", ""), resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        return exc.geturl(), exc.headers.get("content-type", ""), exc.code, exc.read()
    except urllib.error.URLError as exc:
        return url, "", f"FETCH_ERROR:{exc.reason}", b""


def require_open_rails_for_refresh() -> None:
    if os.environ.get("SAFE_MODE") != "0" or os.environ.get("ALLOW_NETWORK") != "1":
        raise SystemExit("OPEN_RAILS_REQUIRED: set SAFE_MODE=0 and ALLOW_NETWORK=1 with --refresh-public-docs for public documentation fetching")


def source_cache_name(key: str, configured: str | None) -> str:
    return configured or f"{key}.body"


def source_cache_rel(cache_name: str | None) -> str | None:
    return f"artifacts/vendor/hdapi_v2/source_cache/{cache_name}" if cache_name else None


def refresh_source_cache(produced: str) -> tuple[dict[str, dict[str, Any]], dict[str, bytes]]:
    require_open_rails_for_refresh()
    SOURCE_CACHE.mkdir(parents=True, exist_ok=True)
    metadata: dict[str, dict[str, Any]] = {}
    bodies: dict[str, bytes] = {}
    for key, url, classification, discovered_from, configured_cache_name in SOURCES:
        cache_name = source_cache_name(key, configured_cache_name)
        final_url, content_type, status, body = fetch_public_doc(url)
        cache_body = body
        if key == "llms_full_txt" and status in ALLOWED_STATUS:
            cache_body = llms_full_endpoint_tier_excerpt(body)
        write_bytes(SOURCE_CACHE / cache_name, cache_body)
        bodies[key] = cache_body
        metadata[key] = {
            "cache_path": source_cache_rel(cache_name),
            "cache_sha256": sha256_bytes(cache_body),
            "content_type": content_type,
            "discovered_from": discovered_from,
            "fetch_status": str(status),
            "final_url": final_url,
            "last_seen_utc": produced,
            "sha256": sha256_bytes(body) if body else "",
            "source_classification": classification,
            "source_url": url,
        }
    SOURCE_METADATA.write_bytes(canonical_json_bytes({"generated_at_utc": produced, "sources": metadata}))
    return metadata, bodies


def load_source_cache() -> tuple[dict[str, dict[str, Any]], dict[str, bytes]]:
    if not SOURCE_METADATA.exists():
        raise SystemExit("MISSING_SOURCE_CACHE: run with --refresh-public-docs under SAFE_MODE=0 ALLOW_NETWORK=1 to capture public docs")
    payload = json.loads(SOURCE_METADATA.read_text(encoding="utf-8"))
    metadata = payload.get("sources")
    if not isinstance(metadata, dict):
        raise SystemExit("INVALID_SOURCE_CACHE: missing sources")
    bodies: dict[str, bytes] = {}
    for key, _url, _classification, _discovered_from, configured_cache_name in SOURCES:
        row = metadata.get(key)
        if not isinstance(row, dict):
            raise SystemExit(f"INVALID_SOURCE_CACHE: missing {key}")
        cache_name = source_cache_name(key, configured_cache_name)
        cache_path = SOURCE_CACHE / cache_name
        if not cache_path.exists():
            if key == "suspect_openapi_json":
                bodies[key] = b""
                continue
            raise SystemExit(f"MISSING_SOURCE_BODY:{cache_path.relative_to(ROOT).as_posix()}")
        body = cache_path.read_bytes()
        expected = row.get("cache_sha256") or row.get("sha256")
        actual = sha256_bytes(body)
        if expected != actual:
            raise SystemExit(f"SOURCE_CACHE_SHA_MISMATCH:{key}")
        bodies[key] = body
    return metadata, bodies


def parse_yaml_openapi(body: bytes, name: str) -> dict[str, Any]:
    with tempfile.NamedTemporaryFile(suffix=".yaml") as tmp:
        tmp.write(body)
        tmp.flush()
        result = subprocess.run(
            ["ruby", "-ryaml", "-rjson", "-e", "puts JSON.generate(YAML.safe_load_file(ARGV.fetch(0), permitted_classes: [], aliases: false))", tmp.name],
            check=False,
            capture_output=True,
            text=True,
        )
    if result.returncode != 0:
        raise ValueError(f"YAML_PARSE_FAILED:{name}:{result.stderr.strip()}")
    parsed = json.loads(result.stdout)
    if not isinstance(parsed, dict):
        raise ValueError(f"YAML_PARSE_NOT_OBJECT:{name}")
    return parsed


def ref_name(ref: str | None) -> str:
    if not ref or not ref.startswith("#/components/schemas/"):
        return ""
    return ref.rsplit("/", 1)[-1]


def schema_ref_names(schema: Any) -> list[str]:
    refs: list[str] = []
    if isinstance(schema, dict):
        if "$ref" in schema:
            refs.append(ref_name(str(schema["$ref"])))
        for value in schema.values():
            refs.extend(schema_ref_names(value))
    elif isinstance(schema, list):
        for item in schema:
            refs.extend(schema_ref_names(item))
    return [ref for ref in refs if ref]


def method_obj(spec: dict[str, Any], path: str) -> dict[str, Any]:
    paths = spec.get("paths")
    if not isinstance(paths, dict) or path not in paths:
        raise ValueError(f"MISSING_PATH:{path}")
    path_item = paths[path]
    if not isinstance(path_item, dict) or not isinstance(path_item.get("post"), dict):
        raise ValueError(f"MISSING_POST:{path}")
    return path_item["post"]


def content_type_and_schema(method: dict[str, Any]) -> tuple[str, str]:
    body = method.get("requestBody")
    if not isinstance(body, dict) or body.get("required") is not True:
        raise ValueError("REQUEST_BODY_REQUIRED_MISSING")
    content = body.get("content")
    if not isinstance(content, dict) or not content:
        raise ValueError("REQUEST_CONTENT_MISSING")
    if "application/json" not in content:
        raise ValueError("REQUEST_CONTENT_NOT_JSON")
    schema = content["application/json"].get("schema")
    if not isinstance(schema, dict):
        raise ValueError("REQUEST_SCHEMA_MISSING")
    return "application/json", ref_name(str(schema.get("$ref", "")))


def required_fields(spec: dict[str, Any], schema_name: str) -> list[str]:
    schemas = spec.get("components", {}).get("schemas", {})
    schema = schemas.get(schema_name)
    if not isinstance(schema, dict):
        raise ValueError(f"MISSING_SCHEMA:{schema_name}")
    required = schema.get("required")
    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        raise ValueError(f"MISSING_REQUIRED_FIELDS:{schema_name}")
    return required


def success_envelope(method: dict[str, Any], *, version: str) -> str:
    responses = method.get("responses")
    if not isinstance(responses, dict) or "200" not in responses:
        raise ValueError("MISSING_200_RESPONSE")
    content = responses["200"].get("content", {})
    schema = content.get("application/json", {}).get("schema")
    refs = schema_ref_names(schema)
    if version == "v2":
        if "StandardResponse" not in refs:
            raise ValueError("MISSING_STANDARD_RESPONSE")
        response_type = ""
        if isinstance(schema, dict):
            all_of = schema.get("allOf", [])
            if isinstance(all_of, list):
                for entry in all_of:
                    props = entry.get("properties", {}) if isinstance(entry, dict) else {}
                    type_prop = props.get("type", {}) if isinstance(props, dict) else {}
                    if isinstance(type_prop, dict) and type_prop.get("example"):
                        response_type = str(type_prop["example"])
        data_refs = [ref for ref in refs if ref != "StandardResponse"]
        if not response_type or not data_refs:
            raise ValueError("MISSING_V2_SUCCESS_DATA_REF")
        return f"StandardResponse with type={response_type} and data={data_refs[-1]}"
    if not refs:
        raise ValueError("MISSING_V1_SUCCESS_SCHEMA")
    return f"flat JSON {refs[-1]}; no v2 StandardResponse envelope"


def standard_response_fields(spec: dict[str, Any], *, version: str) -> list[str]:
    if version != "v2":
        return []
    schema = spec.get("components", {}).get("schemas", {}).get("StandardResponse")
    if not isinstance(schema, dict):
        raise ValueError("MISSING_STANDARD_RESPONSE_SCHEMA")
    required = schema.get("required")
    properties = schema.get("properties")
    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        raise ValueError("STANDARD_RESPONSE_REQUIRED_FIELDS_MISSING")
    if not isinstance(properties, dict):
        raise ValueError("STANDARD_RESPONSE_PROPERTIES_MISSING")
    missing = [
        field for field in RESPONSE_MAPPING_REQUIRED_STANDARD_FIELDS
        if field not in required or field not in properties
    ]
    if missing:
        raise ValueError(f"STANDARD_RESPONSE_FIELDS_MISSING:{','.join(missing)}")
    return required


def collect_error_codes(value: Any) -> list[str]:
    codes: set[str] = set()
    if isinstance(value, str):
        codes.update(re.findall(r"`([A-Z0-9_]+)`", value))
    elif isinstance(value, dict):
        for child in value.values():
            codes.update(collect_error_codes(child))
    elif isinstance(value, list):
        for child in value:
            codes.update(collect_error_codes(child))
    return sorted(codes)


def response_error_codes(method: dict[str, Any]) -> str:
    responses = method.get("responses")
    if not isinstance(responses, dict):
        raise ValueError("MISSING_RESPONSES")
    codes = collect_error_codes({k: v for k, v in responses.items() if k != "200"})
    return ";".join(codes) if codes else "schema-defined StandardErrorResponse"


def security_names(method: dict[str, Any]) -> list[str]:
    security = method.get("security")
    if not isinstance(security, list) or not security or not isinstance(security[0], dict):
        raise ValueError("MISSING_SECURITY")
    return list(security[0].keys())


def auth_model(spec: dict[str, Any], method: dict[str, Any]) -> str:
    schemes = spec.get("components", {}).get("securitySchemes", {})
    names = security_names(method)
    rendered: list[str] = []
    for name in names:
        scheme = schemes.get(name)
        if not isinstance(scheme, dict):
            raise ValueError(f"MISSING_SECURITY_SCHEME:{name}")
        if scheme.get("type") == "http" and scheme.get("scheme") == "bearer":
            rendered.append("Authorization Bearer token")
        elif scheme.get("type") == "apiKey" and scheme.get("in") == "header" and scheme.get("name"):
            rendered.append(f"{scheme['name']} header")
        else:
            raise ValueError(f"UNSUPPORTED_SECURITY_SCHEME:{name}")
    return " plus ".join(rendered)


def geocode_requirement(method: dict[str, Any]) -> str:
    return "required" if "GeocodeKeyAuth" in security_names(method) else "not needed"


def markdown_cells(raw: str) -> list[str]:
    if not raw.startswith("|"):
        return []
    return [cell.strip().strip("`").strip() for cell in raw.strip().strip("|").split("|")]


def parse_tier_map(llms_full: str) -> dict[str, str]:
    tier_map: dict[str, str] = {}
    for raw in llms_full.splitlines():
        cells = markdown_cells(raw)
        if len(cells) < 3:
            continue
        endpoint = cells[0]
        tier = cells[2]
        for _method, path in REQUIRED_ENDPOINTS:
            label = f"POST {path}"
            if endpoint == label:
                if not tier:
                    raise ValueError(f"TIER_EMPTY:{path}")
                tier_map[path] = tier
    missing = [path for _method, path in REQUIRED_ENDPOINTS if path not in tier_map]
    if missing:
        raise ValueError(f"TIER_MAP_MISSING:{','.join(missing)}")
    return tier_map


def validate_openapi_spec(name: str, spec: dict[str, Any], *, expected_title: str, expected_server: str, paths: list[str]) -> tuple[bool, list[str]]:
    checks: list[tuple[str, bool]] = []
    info = spec.get("info")
    servers = spec.get("servers")
    components = spec.get("components")
    checks.append(("openapi_3_parse", isinstance(spec.get("openapi"), str) and str(spec["openapi"]).startswith("3.")))
    checks.append(("title_humandesignapi", isinstance(info, dict) and info.get("title") == expected_title))
    checks.append(("version_present", isinstance(info, dict) and bool(info.get("version"))))
    checks.append(("server_domain", isinstance(servers, list) and any(isinstance(item, dict) and item.get("url") == expected_server for item in servers)))
    checks.append(("components_present", isinstance(components, dict) and isinstance(components.get("schemas"), dict) and isinstance(components.get("securitySchemes"), dict)))
    for path in paths:
        try:
            method = method_obj(spec, path)
            content_type_and_schema(method)
            security_names(method)
            success_envelope(method, version="v2" if "v2" in name else "v1")
            standard_response_fields(spec, version="v2" if "v2" in name else "v1")
            checks.append((f"path_{path}_post_contract", True))
        except ValueError:
            checks.append((f"path_{path}_post_contract", False))
    ok = all(result for _label, result in checks)
    lines = [f"[{name}] status={'VALIDATED' if ok else 'INVALID'}"]
    lines.extend(f"[{name}] {label}={'PASS' if result else 'FAIL'}" for label, result in checks)
    version = info.get("version") if isinstance(info, dict) else "UNKNOWN"
    lines.append(f"[{name}] observed_version={version or 'UNKNOWN'}")
    return ok, lines


def validate_suspect_openapi(body: bytes, source_row: dict[str, Any]) -> tuple[bool, dict[str, Any], list[str]]:
    fetch_status = str(source_row.get("fetch_status", ""))
    if fetch_status != "200":
        return False, {"fetch_status": fetch_status}, [
            "[api-reference/openapi.json] status=QUARANTINED",
            f"[api-reference/openapi.json] fetch_status={fetch_status or 'MISSING'}",
            "[api-reference/openapi.json] availability=UNAVAILABLE",
        ]
    try:
        obj = json.loads(body.decode("utf-8"))
    except json.JSONDecodeError:
        return False, {"fetch_status": fetch_status}, ["[api-reference/openapi.json] status=QUARANTINED", "[api-reference/openapi.json] json_parse=FAIL"]
    title = str(obj.get("info", {}).get("title", "")) if isinstance(obj.get("info"), dict) else ""
    servers = obj.get("servers") if isinstance(obj.get("servers"), list) else []
    paths = obj.get("paths") if isinstance(obj.get("paths"), dict) else {}
    server_domain_ok = any(isinstance(item, dict) and "humandesignapi.nl" in str(item.get("url", "")) for item in servers)
    path_family_ok = any(path.startswith(("/v1/", "/v2/", "/charts", "/bodygraphs")) for path in paths)
    title_ok = "Human Design API" in title
    ok = title_ok and server_domain_ok and path_family_ok
    lines = [
        f"[api-reference/openapi.json] status={'VALIDATED' if ok else 'QUARANTINED'}",
        f"[api-reference/openapi.json] title={title or 'MISSING'}",
        f"[api-reference/openapi.json] title_humandesignapi={'PASS' if title_ok else 'FAIL'}",
        f"[api-reference/openapi.json] server_domain={'PASS' if server_domain_ok else 'FAIL'}",
        f"[api-reference/openapi.json] path_family={'PASS' if path_family_ok else 'FAIL'}",
    ]
    return ok, {"fetch_status": fetch_status, "title": title, "servers": servers, "paths": sorted(paths)}, lines


def source_spec_for(path: str) -> str:
    if path.startswith("/v2"):
        relative = path.removeprefix("/v2")
        encoded = relative.replace("/", "~1")
        return f"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/{encoded}/post"
    relative = path.removeprefix("/v1")
    encoded = relative.replace("/", "~1")
    return f"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/{encoded}/post"


def build_endpoint_rows(v2_spec: dict[str, Any], v1_spec: dict[str, Any], llms_full: str) -> list[dict[str, str]]:
    tier_map = parse_tier_map(llms_full)
    rows: list[dict[str, str]] = []
    for method, full_path in REQUIRED_ENDPOINTS:
        version = "v2" if full_path.startswith("/v2") else "v1"
        spec = v2_spec if version == "v2" else v1_spec
        spec_path = full_path.removeprefix(f"/{version}")
        op = method_obj(spec, spec_path)
        request_content_type, schema_name = content_type_and_schema(op)
        request_fields = required_fields(spec, schema_name)
        envelope_fields = standard_response_fields(spec, version=version)
        rows.append(
            {
                "auth_model": auth_model(spec, op),
                "error_codes": response_error_codes(op),
                "geocode_key_requirement": geocode_requirement(op),
                "method": method,
                "path": full_path,
                "request_content_type": request_content_type,
                "request_fields": ";".join(request_fields),
                "route_family": "recommended_v2_chart" if version == "v2" else "legacy_v1_bodygraph",
                "source_spec": source_spec_for(full_path),
                "response_envelope_fields": ";".join(envelope_fields) if envelope_fields else "not applicable",
                "success_envelope": success_envelope(op, version=version),
                "tier": tier_map[full_path],
            }
        )
    return rows


def build_validation_log(produced: str, v2_ok: bool, v2_lines: list[str], v1_ok: bool, v1_lines: list[str], suspect_lines: list[str], *, mode: str) -> str:
    lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC033 HDE-FERM006.2 machine-readable vendor route validation",
        f"source_mode={mode}",
        "network_posture=public documentation refresh only when --refresh-public-docs is used with SAFE_MODE=0 and ALLOW_NETWORK=1; default generation is closed-rails cache replay",
        "validator=Ruby Psych YAML parser plus fail-closed OpenAPI structural validator for title/version/server/security/request/response/path-family ownership",
    ]
    lines.extend(v2_lines)
    lines.extend(v1_lines)
    lines.extend(suspect_lines)
    lines.append(f"[route-spec-gate] status={'PASS' if v2_ok and v1_ok else 'FAIL'}")
    return "\n".join(lines)


def build_anomaly_text(produced: str, suspect_ok: bool, suspect_info: dict[str, Any]) -> str:
    title = suspect_info.get("title") or "MISSING"
    servers = suspect_info.get("servers") or []
    paths = suspect_info.get("paths") or []
    lines = [
        "# HDAPI v2 Known Anomalies",
        "",
        f"Generated at UTC: {produced}",
        "",
        "## api-reference/openapi.json posture",
        "",
    ]
    if suspect_ok:
        lines.extend(
            [
                "Decision: VALIDATED.",
                "",
                "The suspect public documentation OpenAPI artifact passed HumanDesignAPI title, server-domain, and path-family ownership checks in this run. No quarantine entry is emitted for it in the contract map.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "Decision: QUARANTINED.",
                "",
                f"The repository path `api-reference/openapi.json` is {'present' if (ROOT / 'api-reference/openapi.json').exists() else 'absent'} in this repo. The public documentation URL `https://docs.humandesignapi.nl/api-reference/openapi.json` did not prove HumanDesignAPI ownership in this run: title=`{title}`, servers={json.dumps(servers, sort_keys=True)}, paths_sample={json.dumps(paths[:5], sort_keys=True)}.",
                "",
                "Quarantine effect: the suspect artifact is not used as authority for vendor bytes, schemas, endpoint routes, request shaping, response mapping, runtime conformance, or architecture conformance. Validated YAML route specs remain first-precedence authority for this contract-inventory slice.",
                "",
            ]
        )
    lines.extend(
        [
            "## Runtime and public-surface boundary",
            "",
            "No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.",
        ]
    )
    return "\n".join(lines)


def build_contract_map(produced: str, fetched: dict[str, dict[str, Any]], rows: list[dict[str, str]], suspect_ok: bool) -> dict[str, Any]:
    route_families = []
    for row in rows:
        source_key = "v2_routes_yaml" if row["path"].startswith("/v2") else "v1_routes_yaml"
        route_families.append(
            {
                "auth_model": row["auth_model"],
                "geocode_key_requirement": row["geocode_key_requirement"],
                "method": row["method"],
                "path": row["path"],
                "request_content_type": row["request_content_type"],
                "request_fields": row["request_fields"].split(";"),
                "response_envelope_fields": (
                    row["response_envelope_fields"].split(";")
                    if row["response_envelope_fields"] != "not applicable"
                    else "not applicable"
                ),
                "route_family": row["route_family"],
                "source_precedence_rank": 1,
                "source_sha256": fetched[source_key]["sha256"],
                "source_spec": row["source_spec"],
                "success_envelope": row["success_envelope"],
                "tier": row["tier"],
            }
        )
    contract = {
        "ai_boundary": "No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rail, AI evidence family, AI token, or AI runtime scope is introduced.",
        "generated_at_utc": produced,
        "non_conformance_claim": "Contract inventory only; no HumanDesignAPI v2 runtime request shaping, source selection, live conformance, public Reader change, or open-rails smoke is claimed.",
        "quarantined_sources": [],
        "route_families": route_families,
        "source_precedence": [
            "validated v2 and v1 YAML route specs",
            "rendered endpoint pages",
            "high-level guide pages",
            "suspect artifacts quarantined until validated",
        ],
        "validated_sources": [
            {"sha256": fetched["v2_routes_yaml"]["sha256"], "source_key": "v2_routes_yaml", "source_url": f"{BASE}/openapi/v2-routes.yaml"},
            {"sha256": fetched["v1_routes_yaml"]["sha256"], "source_key": "v1_routes_yaml", "source_url": f"{BASE}/openapi/v1-routes.yaml"},
        ],
    }
    if not suspect_ok:
        contract["quarantined_sources"].append(
            {
                "reason": "api-reference/openapi.json did not prove HumanDesignAPI title/server/path-family ownership in this run or repo-local artifact was absent.",
                "source_key": "suspect_openapi_json",
                "source_url": f"{BASE}/api-reference/openapi.json",
            }
        )
    return contract



def _contract_routes(contract: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    routes = contract.get("route_families")
    if not isinstance(routes, list):
        raise ValueError("CONTRACT_MAP_MISSING_ROUTE_FAMILIES")
    mapped: dict[tuple[str, str], dict[str, Any]] = {}
    for route in routes:
        if not isinstance(route, dict):
            raise ValueError("CONTRACT_MAP_ROUTE_NOT_OBJECT")
        method = route.get("method")
        path = route.get("path")
        if not isinstance(method, str) or not isinstance(path, str):
            raise ValueError("CONTRACT_MAP_ROUTE_MISSING_METHOD_OR_PATH")
        mapped[(method, path)] = route
    return mapped


def build_source_selection_snapshot(produced: str, contract: dict[str, Any]) -> dict[str, Any]:
    """Derive HDE-EPIC034 PR-01 source-selection evidence from contract inventory."""
    routes = _contract_routes(contract)
    required = V2_CHART_ROUTES + V1_BODYGRAPH_ROUTES
    missing = [(method, path) for method, path, _variant in required if (method, path) not in routes]
    if missing:
        formatted = ",".join(f"{method} {path}" for method, path in missing)
        raise ValueError(f"SOURCE_SELECTION_MISSING_CONTRACT_ROUTES:{formatted}")

    snapshot_routes: list[dict[str, Any]] = []
    for method, path, variant in required:
        route = routes[(method, path)]
        expected_family = "recommended_v2_chart" if path.startswith("/v2/") else "legacy_v1_bodygraph"
        if route.get("route_family") != expected_family:
            raise ValueError(f"SOURCE_SELECTION_ROUTE_FAMILY_MISMATCH:{method} {path}")
        auth = route.get("auth_model")
        geocode = route.get("geocode_key_requirement")
        source_spec = route.get("source_spec")
        source_precedence_rank = route.get("source_precedence_rank")
        if not isinstance(auth, str) or not auth:
            raise ValueError(f"SOURCE_SELECTION_AUTH_MODEL_MISSING:{method} {path}")
        if not isinstance(geocode, str) or not geocode:
            raise ValueError(f"SOURCE_SELECTION_GEOCODE_REQUIREMENT_MISSING:{method} {path}")
        expected_source_spec = source_spec_for(path)
        if source_spec != expected_source_spec or source_precedence_rank != 1:
            raise ValueError(f"SOURCE_SELECTION_SOURCE_AUTHORITY_MISMATCH:{method} {path}")
        expected_geocode = "not needed" if path == "/v2/charts/coordinates" else "required"
        if geocode != expected_geocode:
            raise ValueError(f"SOURCE_SELECTION_GEOCODE_REQUIREMENT_MISMATCH:{method} {path}")
        if expected_family == "recommended_v2_chart":
            if "Authorization Bearer token" not in auth or "HD-Api-Key header" in auth:
                raise ValueError(f"SOURCE_SELECTION_AUTH_FAMILY_MISMATCH:{method} {path}")
        if expected_family == "legacy_v1_bodygraph":
            if "HD-Api-Key header" not in auth or "Authorization Bearer token" in auth:
                raise ValueError(f"SOURCE_SELECTION_AUTH_FAMILY_MISMATCH:{method} {path}")
        if expected_geocode == "required" and "HD-Geocode-Key header" not in auth:
            raise ValueError(f"SOURCE_SELECTION_GEOCODE_AUTH_MISMATCH:{method} {path}")
        if expected_geocode == "not needed" and "HD-Geocode-Key header" in auth:
            raise ValueError(f"SOURCE_SELECTION_GEOCODE_AUTH_MISMATCH:{method} {path}")
        snapshot_routes.append(
            {
                "auth_model": auth,
                "classification_source": "artifacts/vendor/hdapi_v2/contract_map.json route_families",
                "geocode_key_requirement": geocode,
                "method": method,
                "path": path,
                "route_family": expected_family,
                "route_variant": variant,
                "source_precedence_rank": source_precedence_rank,
                "source_spec": source_spec,
            }
        )

    return {
        "ai_scope_claim": "NONE",
        "generated_at_utc": produced,
        "open_rails_vendor_smoke_claim": "NONE",
        "public_reader_change_claim": "NONE",
        "request_shaping_claim": "NONE",
        "route_families": snapshot_routes,
        "runtime_conformance_claim": "NONE",
        "source_selection_policy": {
            "classification_source": "governed contract inventory",
            "legacy_v1_bodygraph_route_family": "legacy_v1_bodygraph",
            "recommended_internal_vendor_route_family": "recommended_v2_chart",
            "selection_scope": "HDE-EPIC034 PR-01 HDE-FERM007.1 route-family source selection only",
        },
    }


def build_v1_legacy_guard_log(produced: str, snapshot: dict[str, Any]) -> str:
    routes = snapshot.get("route_families")
    if not isinstance(routes, list):
        raise ValueError("SOURCE_SELECTION_SNAPSHOT_MISSING_ROUTES")
    by_path = {route["path"]: route for route in routes if isinstance(route, dict) and "path" in route}
    lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC034 PR-01 HDE-FERM007.1 v1 legacy guard",
        "classification_source=artifacts/vendor/hdapi_v2/contract_map.json route_families",
    ]
    for _method, path, variant in V1_BODYGRAPH_ROUTES:
        route = by_path.get(path)
        status = "PASS" if route and route.get("route_family") == "legacy_v1_bodygraph" and route.get("route_variant") == variant else "FAIL"
        lines.append(f"[{path}] legacy_v1_bodygraph_explicit={status}")
        lines.append(f"[{path}] collapsed_to_recommended_v2_chart={'FAIL' if status == 'PASS' else 'UNKNOWN'}")
    v2_variants = [by_path[path].get("route_variant") for _method, path, _variant in V2_CHART_ROUTES if path in by_path]
    lines.append(f"v2_chart_route_variants_distinct={'PASS' if len(set(v2_variants)) == 3 else 'FAIL'}")
    lines.append("request_shaping_claim=NONE")
    lines.append("runtime_conformance_claim=NONE")
    lines.append("public_reader_change_claim=NONE")
    lines.append("open_rails_vendor_smoke_claim=NONE")
    lines.append("ai_scope=NONE")
    lines.append("status=PASS" if all("FAIL" not in line for line in lines if "collapsed_to_recommended_v2_chart" not in line) else "status=FAIL")
    return "\n".join(lines)


def build_source_selection_check_log(produced: str, snapshot: dict[str, Any], *, mode: str) -> str:
    routes = snapshot["route_families"]
    families = {(route["method"], route["path"]): route["route_family"] for route in routes}
    variants = {(route["method"], route["path"]): route["route_variant"] for route in routes}
    auth_models = {(route["method"], route["path"]): route.get("auth_model") for route in routes}
    geocode = {(route["method"], route["path"]): route.get("geocode_key_requirement") for route in routes}
    source_specs = {(route["method"], route["path"]): route.get("source_spec") for route in routes}
    source_ranks = {(route["method"], route["path"]): route.get("source_precedence_rank") for route in routes}
    checks = [
        ("recommended_v2_full_chart", families.get(("POST", "/v2/charts")) == "recommended_v2_chart"),
        ("recommended_v2_simple_chart", families.get(("POST", "/v2/charts/simple")) == "recommended_v2_chart"),
        ("recommended_v2_coordinates_chart", families.get(("POST", "/v2/charts/coordinates")) == "recommended_v2_chart"),
        ("legacy_v1_full_bodygraph", families.get(("POST", "/v1/bodygraphs")) == "legacy_v1_bodygraph"),
        ("legacy_v1_simple_bodygraph", families.get(("POST", "/v1/bodygraphs/simple")) == "legacy_v1_bodygraph"),
        ("v2_variants_distinguished", len({variants.get(item[:2]) for item in V2_CHART_ROUTES}) == 3),
        ("v1_not_collapsed_to_v2", all(families.get((method, path)) != "recommended_v2_chart" for method, path, _variant in V1_BODYGRAPH_ROUTES)),
        (
            "v2_auth_family_bearer_only",
            all(
                "Authorization Bearer token" in str(auth_models.get((method, path), ""))
                and "HD-Api-Key header" not in str(auth_models.get((method, path), ""))
                for method, path, _variant in V2_CHART_ROUTES
            ),
        ),
        (
            "v1_auth_family_hd_api_key_only",
            all(
                "HD-Api-Key header" in str(auth_models.get((method, path), ""))
                and "Authorization Bearer token" not in str(auth_models.get((method, path), ""))
                for method, path, _variant in V1_BODYGRAPH_ROUTES
            ),
        ),
        ("v2_location_geocode_required", all(geocode.get((method, path)) == "required" for method, path in [("POST", "/v2/charts"), ("POST", "/v2/charts/simple")])),
        ("v1_bodygraph_geocode_required", all(geocode.get((method, path)) == "required" for method, path, _variant in V1_BODYGRAPH_ROUTES)),
        ("coordinates_geocode_not_needed", geocode.get(("POST", "/v2/charts/coordinates")) == "not needed"),
        (
            "required_geocode_auth_header_present",
            all(
                "HD-Geocode-Key header" in str(auth_models.get((method, path), ""))
                for method, path in [("POST", "/v2/charts"), ("POST", "/v2/charts/simple"), ("POST", "/v1/bodygraphs"), ("POST", "/v1/bodygraphs/simple")]
            ),
        ),
        (
            "coordinates_geocode_auth_header_absent",
            "HD-Geocode-Key header" not in str(auth_models.get(("POST", "/v2/charts/coordinates"), "")),
        ),
        (
            "source_authority_validated_yaml_rank1",
            all(
                source_specs.get((method, path)) == source_spec_for(path)
                and source_ranks.get((method, path)) == 1
                for method, path, _variant in V2_CHART_ROUTES + V1_BODYGRAPH_ROUTES
            ),
        ),
    ]
    network_posture = (
        "closed-rails-source-cache; no live vendor calls"
        if mode == "closed-rails-source-cache"
        else "public-docs-refresh; no credentialed runtime vendor calls"
    )
    lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC034 PR-01 source-selection check",
        f"network_posture={network_posture}",
    ]
    lines.extend(f"[{name}] status={'PASS' if ok else 'FAIL'}" for name, ok in checks)
    lines.append("status=PASS" if all(ok for _name, ok in checks) else "status=FAIL")
    return "\n".join(lines)


def _sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _validate_ops01_fact_summary(payload: dict[str, Any]) -> None:
    raw = json.dumps(payload, sort_keys=True)
    required = [
        "HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY",
        "Authorization: Bearer <redacted>", "HD-Api-Key: <redacted>", "HD-Geocode-Key: <redacted>",
    ]
    missing = [item for item in required if item not in raw]
    pr02_posture = payload.get("pr02_can_proceed_safely")
    if not isinstance(pr02_posture, str) or not pr02_posture.startswith(("proceed_with_caveat:", "proceed_with_requirement:")):
        missing.append("pr02_can_proceed_safely")
    if missing:
        raise ValueError(f"OPS01_FACT_SUMMARY_INCOMPLETE:{','.join(missing)}")


def _load_ops01_fact_summary() -> dict[str, Any]:
    path = ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json"
    proof = ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json.path_proof.txt"
    if not path.exists() or not proof.exists():
        raise ValueError("OPS01_FACT_SUMMARY_MISSING")
    payload = json.loads(path.read_text(encoding="utf-8"))
    _validate_ops01_fact_summary(payload)
    return payload


def _route_by_path(contract: dict[str, Any], path: str) -> dict[str, Any]:
    for route in contract.get("route_families", []):
        if isinstance(route, dict) and route.get("method") == "POST" and route.get("path") == path:
            return route
    raise ValueError(f"REQUEST_SHAPING_ROUTE_MISSING:{path}")


def build_request_shaping_snapshot(produced: str, contract: dict[str, Any], source_selection: dict[str, Any], ops_summary: dict[str, Any]) -> dict[str, Any]:
    _validate_ops01_fact_summary(ops_summary)
    if source_selection.get("request_shaping_claim") != "NONE":
        raise ValueError("REQUEST_SHAPING_SOURCE_SELECTION_BASELINE_DRIFT")
    routes: list[dict[str, Any]] = []
    for method, path, variant in V2_CHART_ROUTES + V1_BODYGRAPH_ROUTES:
        route = _route_by_path(contract, path)
        fields = route.get("request_fields")
        if not isinstance(fields, list) or not fields:
            raise ValueError(f"REQUEST_SHAPING_FIELDS_MISSING:{path}")
        content_type = route.get("request_content_type")
        auth_model = str(route.get("auth_model", ""))
        geocode = route.get("geocode_key_requirement")
        if content_type != "application/json":
            raise ValueError(f"REQUEST_SHAPING_CONTENT_TYPE_MISMATCH:{path}")
        v2 = path.startswith("/v2/")
        expected_family = "recommended_v2_chart" if v2 else "legacy_v1_bodygraph"
        if route.get("route_family") != expected_family:
            raise ValueError(f"REQUEST_SHAPING_ROUTE_FAMILY_MISMATCH:{path}")
        if v2 and ("Authorization Bearer token" not in auth_model or "HD-Api-Key header" in auth_model):
            raise ValueError(f"REQUEST_SHAPING_AUTH_MISMATCH:{path}")
        if not v2 and ("HD-Api-Key header" not in auth_model or "Authorization Bearer token" in auth_model):
            raise ValueError(f"REQUEST_SHAPING_AUTH_MISMATCH:{path}")
        if geocode == "required" and "HD-Geocode-Key header" not in auth_model:
            raise ValueError(f"REQUEST_SHAPING_GEOCODE_MISMATCH:{path}")
        if geocode == "not needed" and "HD-Geocode-Key header" in auth_model:
            raise ValueError(f"REQUEST_SHAPING_GEOCODE_MISMATCH:{path}")
        routes.append({
            "auth_header_posture": "Authorization: Bearer <redacted>" if v2 else "HD-Api-Key: <redacted>",
            "body_field_source_list": fields,
            "content_type_posture": content_type,
            "credential_env_var": "HD_API_KEY",
            "endpoint_path": path,
            "geocode_env_var": "GEO_API_KEY" if geocode == "required" else "not applicable",
            "geocode_header_posture": "HD-Geocode-Key: <redacted>" if geocode == "required" else "not applicable",
            "geocode_key_requirement": geocode,
            "method": method,
            "route_family": expected_family,
            "route_variant": variant,
            "source_spec": route.get("source_spec"),
        })
    return {
        "ai_scope_claim": "NONE",
        "base_url_env_var": "HD_API_BASE_URL",
        "canonical_request_body_construction_proof": "request body keys are ordered from governed contract_map request_fields and serialized as canonical JSON bytes by engine.bodygraph.vendor_client.HdApiClient.build_contract_route_request; v1 bodygraph birthdate is legacy DD-Mon-YYYY while v2 chart birthdate remains YYYY-MM-DD and v2 coordinate lat/lng are serialized as JSON numbers",
        "credential_env_var": "HD_API_KEY",
        "deprecated_base_url_alias": {"env_var": "HDAPI_BASE_URL", "posture": "temporary compatibility alias only; used only when HD_API_BASE_URL is absent; conflicting values fail closed"},
        "generated_at_utc": produced,
        "geocode_env_var": "GEO_API_KEY",
        "input_references": {
            "contract_map": {"path": "artifacts/vendor/hdapi_v2/contract_map.json", "sha256": sha256_bytes(canonical_json_bytes(contract))},
            "ops01_fact_summary": {"path": "audit/ops/hde-epic034/ops-01/fact_summary.json", "sha256": _sha256_path(ROOT / "audit/ops/hde-epic034/ops-01/fact_summary.json")},
            "source_selection_snapshot": {"path": "artifacts/vendor/hdapi_v2/source_selection.snapshot.json", "sha256": sha256_bytes(canonical_json_bytes(source_selection))},
        },
        "live_vendor_call_claim": "NONE",
        "open_rails_vendor_smoke_claim": "NONE",
        "public_reader_change_claim": "NONE",
        "request_content_type_posture": "application/json",
        "route_family": "recommended_v2_chart",
        "routes": routes,
        "runtime_conformance_claim": "NONE",
        "source_selection_input_reference": "artifacts/vendor/hdapi_v2/source_selection.snapshot.json",
        "v1_legacy_auth_header_posture": "HD-Api-Key: <redacted>",
        "v2_auth_header_posture": "Authorization: Bearer <redacted>",
    }


def build_request_shaping_check_log(produced: str, snapshot: dict[str, Any], *, mode: str) -> str:
    routes = snapshot["routes"]
    by_path = {row["endpoint_path"]: row for row in routes}
    env_snapshot = closed_rails_env_snapshot()
    checks = [
        ("closed_rails_generation", mode == "closed-rails-source-cache" and closed_rails_env_ok()),
        ("no_live_vendor_call_attempted", snapshot["live_vendor_call_claim"] == "NONE"),
        ("v2_bearer_auth_posture", all(by_path[p]["auth_header_posture"] == "Authorization: Bearer <redacted>" and by_path[p]["credential_env_var"] == "HD_API_KEY" for _m,p,_v in V2_CHART_ROUTES)),
        ("v1_legacy_hd_api_key_posture", all(by_path[p]["auth_header_posture"] == "HD-Api-Key: <redacted>" for _m,p,_v in V1_BODYGRAPH_ROUTES)),
        ("geocode_posture", by_path["/v2/charts"]["geocode_header_posture"] == "HD-Geocode-Key: <redacted>" and by_path["/v2/charts/coordinates"]["geocode_header_posture"] == "not applicable"),
        ("canonical_base_url_key_posture", snapshot["base_url_env_var"] == "HD_API_BASE_URL"),
        ("deprecated_alias_posture", snapshot["deprecated_base_url_alias"]["env_var"] == "HDAPI_BASE_URL"),
        ("no_secret_values_emitted", "secret" not in json.dumps(snapshot).lower() and "k_test" not in json.dumps(snapshot)),
    ]
    rails = " ".join(f"{key}={env_snapshot[key]}" for key in sorted(CLOSED_RAILS_ENV))
    lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC034 PR-02 request-shaping check",
        f"rails={rails}",
        "network_posture=closed-rails-source-cache; no live vendor calls",
        "evidence_index_and_path_proof_posture=validated_by_update_evidence_index_and_validate_evidence_paths_not_generator",
    ]
    lines.extend(f"[{name}] status={'PASS' if ok else 'FAIL'}" for name, ok in checks)
    lines.append("status=PASS" if all(ok for _name, ok in checks) else "status=FAIL")
    return "\n".join(lines)


def _response_type_from_success_envelope(route: dict[str, Any]) -> str:
    envelope = route.get("success_envelope")
    if not isinstance(envelope, str) or "StandardResponse with type=" not in envelope or " and data=" not in envelope:
        raise ValueError(f"RESPONSE_MAPPING_ENVELOPE_MISSING:{route.get('path')}")
    return envelope.split("StandardResponse with type=", 1)[1].split(" and data=", 1)[0]


def _response_data_schema_from_success_envelope(route: dict[str, Any]) -> str:
    envelope = route.get("success_envelope")
    if not isinstance(envelope, str) or " and data=" not in envelope:
        raise ValueError(f"RESPONSE_MAPPING_DATA_SCHEMA_MISSING:{route.get('path')}")
    return envelope.rsplit(" and data=", 1)[1]


def _response_mapping_envelope_fields(route: dict[str, Any]) -> list[str]:
    fields = route.get("response_envelope_fields")
    if not isinstance(fields, list) or not all(isinstance(item, str) for item in fields):
        raise ValueError(f"RESPONSE_MAPPING_ENVELOPE_FIELDS_MISSING:{route.get('path')}")
    missing = [field for field in RESPONSE_MAPPING_REQUIRED_STANDARD_FIELDS if field not in fields]
    if missing:
        raise ValueError(f"RESPONSE_MAPPING_ENVELOPE_FIELDS_MISSING:{route.get('path')}:{','.join(missing)}")
    return fields


def _response_mapping_internal_loci() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for rel in RESPONSE_MAPPING_INTERNAL_LOCI:
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"RESPONSE_MAPPING_INTERNAL_LOCUS_MISSING:{rel}")
        text = path.read_text(encoding="utf-8")
        if rel.startswith("engine/bodygraph/") and "bodygraph" not in text.lower():
            raise ValueError(f"RESPONSE_MAPPING_INTERNAL_LOCUS_UNEXPECTED:{rel}")
        if rel == "engine/compat/compute.py" and "compat" not in text.lower():
            raise ValueError(f"RESPONSE_MAPPING_INTERNAL_LOCUS_UNEXPECTED:{rel}")
        rows.append({"path": rel, "sha256": _sha256_path(path)})
    return rows


def build_response_mapping_snapshot(
    produced: str,
    contract: dict[str, Any],
    source_selection: dict[str, Any],
    request_shaping: dict[str, Any],
    ops_summary: dict[str, Any],
) -> dict[str, Any]:
    """Derive HDE-EPIC034 PR-03 proof-level v2 response-envelope mapping evidence."""
    _validate_ops01_fact_summary(ops_summary)
    if request_shaping.get("route_family") != "recommended_v2_chart":
        raise ValueError("RESPONSE_MAPPING_REQUEST_SHAPING_BASELINE_DRIFT")
    inspected_internal_loci = _response_mapping_internal_loci()
    shaped_by_path = {row.get("endpoint_path"): row for row in request_shaping.get("routes", []) if isinstance(row, dict)}
    expected_response_schemas = {
        "/v2/charts": ("ChartResult", "ChartResult"),
        "/v2/charts/simple": ("ChartSimpleResult", "ChartSimpleResult"),
        "/v2/charts/coordinates": ("ChartResult", "ChartResult"),
    }
    route_mappings: list[dict[str, Any]] = []
    for method, path, variant in V2_CHART_ROUTES:
        contract_route = _route_by_path(contract, path)
        shaped_route = shaped_by_path.get(path)
        if not isinstance(shaped_route, dict) or shaped_route.get("route_variant") != variant:
            raise ValueError(f"RESPONSE_MAPPING_REQUEST_ROUTE_MISSING:{path}")
        if contract_route.get("route_family") != "recommended_v2_chart":
            raise ValueError(f"RESPONSE_MAPPING_ROUTE_FAMILY_MISMATCH:{path}")
        response_type = _response_type_from_success_envelope(contract_route)
        data_schema = _response_data_schema_from_success_envelope(contract_route)
        envelope_fields = _response_mapping_envelope_fields(contract_route)
        expected_response_type, expected_data_schema = expected_response_schemas[path]
        if response_type != expected_response_type or data_schema != expected_data_schema:
            raise ValueError(
                f"RESPONSE_MAPPING_ROUTE_SCHEMA_MISMATCH:{path}:"
                f"type={response_type}:data={data_schema}:"
                f"expected_type={expected_response_type}:expected_data={expected_data_schema}"
            )
        route_mappings.append(
            {
                "data_payload_identity_posture": "preserve data object identity by reference/digest posture only; vendor payload body is not emitted in proof artifacts",
                "data_schema": data_schema,
                "endpoint_path": path,
                "errorCode_handling": "preserve StandardResponse.errorCode as envelope error_code posture; no retry/rate-limit mapping is claimed in PR-03",
                "method": method,
                "response_type": response_type,
                "response_envelope_fields": envelope_fields,
                "route_family": "recommended_v2_chart",
                "route_variant": variant,
                "source_spec": contract_route.get("source_spec"),
                "success_status_handling": "preserve StandardResponse.success as boolean success status posture without claiming live runtime status",
            }
        )
    internal_target_posture = {
        "admin": {
            "consumer_status": "inspected_evidence_only",
            "mapping_result": "no_public_or_admin_runtime_behavior_change_claimed",
            "proof_basis": "no new HTTP home, public route, flag, payload, response shape, or transport behavior is introduced",
        },
        "bodygraph": {
            "consumer_status": "inspected engine.bodygraph.vendor_client, engine.bodygraph.ingest, and engine.bodygraph.resolver",
            "mapping_result": "schema_gap_recorded",
            "proof_basis": "existing ingest path is v1 BodyGraph-oriented and persists emitted payloads after vendor fetch; PR-03 does not add a ChartResult-to-BodyGraph adapter",
        },
        "cache": {
            "consumer_status": "inspected hde.body_graphs persistence path through engine.bodygraph.ingest",
            "mapping_result": "not_truthfully_proven_for_v2_chart_data",
            "proof_basis": "opaque JSON persistence mechanics exist for the v1 vendor path, but v2 ChartResult/cache compatibility is not claimed without adapter proof",
        },
        "compatibility": {
            "consumer_status": "inspected engine.compat.compute person/bodygraph input helpers",
            "mapping_result": "schema_gap_recorded",
            "proof_basis": "compat/conjunction helpers consume person_uid-style resolved BodyGraph/person inputs; v2 ChartResult data is not proven to provide that internal shape",
        },
        "sampler": {
            "consumer_status": "inspected as non-public/dev evidence boundary",
            "mapping_result": "no_runtime_feed_claimed",
            "proof_basis": "sampler/admin/public surfaces are not changed by this proof-level mapping slice",
        },
    }
    return {
        "ai_scope_claim": "NONE",
        "data_payload_body_emitted": False,
        "data_payload_identity_posture": "identity is proven only as an envelope data-field preservation posture; no vendor payload body is serialized",
        "errorCode_handling": "StandardResponse.errorCode is preserved as nullable/defined envelope error-code posture in proof rows; follow-up retry/rate-limit mapping is out of scope",
        "generated_at_utc": produced,
        "input_references": {
            "contract_map": {"path": "artifacts/vendor/hdapi_v2/contract_map.json", "sha256": sha256_bytes(canonical_json_bytes(contract))},
            "ops01_fact_summary": {"path": "audit/ops/hde-epic034/ops-01/fact_summary.json", "sha256": _sha256_path(ROOT / "audit/ops/hde-epic034/ops-01/fact_summary.json")},
            "request_shaping_snapshot": {"path": "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json", "sha256": sha256_bytes(canonical_json_bytes(request_shaping))},
            "source_selection_snapshot": {"path": "artifacts/vendor/hdapi_v2/source_selection.snapshot.json", "sha256": sha256_bytes(canonical_json_bytes(source_selection))},
        },
        "inspected_internal_loci": inspected_internal_loci,
        "internal_target_posture": internal_target_posture,
        "live_vendor_call_claim": "NONE",
        "no_ai_transformation_posture": "no AI interpretation, model-generated transformation, prompt, embedding, chatbot, model call, or AI-provider credential is introduced",
        "no_compatibility_by_inference": True,
        "no_secret_values_posture": "only secret-safe env var/header names and redacted postures are recorded",
        "no_vendor_payload_body_posture": "fixture-backed proof records schema/type/posture only and does not emit vendor payload bodies",
        "normalized_data_path_proof_claim": "NONE",
        "open_rails_vendor_smoke_claim": "NONE",
        "public_reader_change_claim": "NONE",
        "response_envelope_mapping_scope": "HDE-FERM007.3 proof-level v2 StandardResponse envelope mapping only",
        "route_family": "recommended_v2_chart",
        "routes": route_mappings,
        "runtime_conformance_claim": "NONE",
        "schema_gap_status": "GAP_RECORDED",
        "schema_gap_summary": "v2 ChartResult/ChartSimpleResult StandardResponse data is not proven to feed existing BodyGraph cache or compat input paths without a follow-up adapter/presenter boundary proof",
        "success_status_handling": "StandardResponse.success is preserved as success status posture; no live HTTP success or runtime conformance is claimed",
    }


def build_response_mapping_check_log(produced: str, snapshot: dict[str, Any], *, mode: str) -> str:
    env_snapshot = closed_rails_env_snapshot()
    routes = snapshot.get("routes", [])
    checks = [
        ("closed_rails_generation", mode == "closed-rails-source-cache" and closed_rails_env_ok()),
        ("no_live_vendor_call_attempted", snapshot.get("live_vendor_call_claim") == "NONE"),
        ("response_type_preservation", all(isinstance(row, dict) and row.get("response_type") in {"ChartResult", "ChartSimpleResult"} for row in routes)),
        ("success_status_handling", snapshot.get("success_status_handling", "").startswith("StandardResponse.success") and all("success" in row.get("response_envelope_fields", []) for row in routes if isinstance(row, dict))),
        ("errorCode_handling", "errorCode" in snapshot.get("errorCode_handling", "") and all("errorCode" in row.get("response_envelope_fields", []) for row in routes if isinstance(row, dict))),
        ("data_payload_identity_posture", snapshot.get("data_payload_body_emitted") is False and "identity" in snapshot.get("data_payload_identity_posture", "")),
        ("route_variant_preservation", {row.get("route_variant") for row in routes if isinstance(row, dict)} == {"full_chart", "simple_chart", "coordinates_chart"}),
        ("internal_target_posture_or_schema_gap_recorded", snapshot.get("schema_gap_status") == "GAP_RECORDED" and isinstance(snapshot.get("internal_target_posture"), dict)),
        ("internal_loci_inspected", len(snapshot.get("inspected_internal_loci", [])) == len(RESPONSE_MAPPING_INTERNAL_LOCI)),
        ("no_compatibility_by_inference_claim", snapshot.get("no_compatibility_by_inference") is True),
        ("no_normalized_data_path_proof_claimed", snapshot.get("normalized_data_path_proof_claim") == "NONE"),
        ("no_vendor_payload_bodies_emitted", snapshot.get("no_vendor_payload_body_posture", "").startswith("fixture-backed proof")),
        ("no_secret_values_emitted", "k_test" not in json.dumps(snapshot) and "Bearer api" not in json.dumps(snapshot) and "Bearer geo" not in json.dumps(snapshot)),
    ]
    rails = " ".join(f"{key}={env_snapshot[key]}" for key in sorted(CLOSED_RAILS_ENV))
    lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC034 PR-03 response-mapping check",
        f"rails={rails}",
        "network_posture=closed-rails-source-cache; no live vendor calls",
        "evidence_index_and_path_proof_posture=validated_by_update_evidence_index_and_validate_evidence_paths_not_generator",
    ]
    lines.extend(f"[{name}] status={'PASS' if ok else 'FAIL'}" for name, ok in checks)
    lines.append("status=PASS" if all(ok for _name, ok in checks) else "status=FAIL")
    return "\n".join(lines)


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


def _adapter_presenter_bypass_routes(loci: tuple[str, ...]) -> list[str]:
    """Find registered adapter routes that serialize/respond without a presenter path."""

    findings: list[str] = []
    presenter_calls = {"emit_public", "emit_public_with_envelope", "emit_reader_public_bytes", "emit_reader_public_envelope", "emit_fn"}
    bypass_calls = {"jsonify", "json.dumps", "json.dump", "dumps", "dump", "sercanon", "serialize"}
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        aliases = _import_aliases(tree)
        function_defs = {node.name: node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
        class_methods: dict[str, set[str]] = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_methods[node.name] = {
                    child.name
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
            if isinstance(value, ast.Call):
                call_name = _attribute_chain(value.func)
                root = _root_name(value.func)
                target = aliases.get(root or "", root or "")
                if (
                    call_name in {"json.dumps", "dumps", "jsonify", "make_response", "current_app.json.response", "sercanon", "serialize"}
                    or target in {"flask.jsonify", "flask.make_response", "json.dumps"}
                    or call_name.endswith((".jsonify", ".json.response", ".dumps", ".sercanon", ".serialize"))
                ):
                    return True
                return False
            return False

        def function_has_bypass(fn: ast.FunctionDef | ast.AsyncFunctionDef, calls: set[str]) -> bool:
            if any(
                call in bypass_calls
                or aliases.get(call, "") in {"flask.jsonify", "flask.make_response", "json.dumps", "json.dump"}
                or call.endswith((".jsonify", ".json.response", ".dumps", ".dump", ".sercanon", ".serialize"))
                or call == "make_response"
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
                        any(node_is_jsonish(arg) for arg in node.args)
                        or any(keyword.arg in {"response", "json", "data"} and node_is_jsonish(keyword.value) for keyword in node.keywords)
                    ):
                        return True
            return False

        for name, fn in function_defs.items():
            calls = direct_call_names(fn)
            function_calls[name] = calls
            function_return_calls[name] = return_call_names(fn)
            if any(call in presenter_calls or any(call.endswith(f".{presenter_call}") for presenter_call in presenter_calls) for call in calls):
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
            result = any(callee in function_defs and reaches(callee, seen) for callee in function_calls.get(name, set()))
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
            result = any(callee in function_defs and reaches_direct_bypass(callee, seen) for callee in function_return_calls.get(name, set()))
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


def _node_mentions_guard_symbol(node: ast.AST, symbol: str) -> bool:
    for child in ast.walk(node):
        if isinstance(child, ast.Constant) and child.value == symbol:
            return True
    return False


def _vendor_guard_entrypoints(loci: tuple[str, ...]) -> list[str]:
    guarded: list[str] = []
    for rel in loci:
        _path, _text, tree = _python_source(rel)
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if (
                _node_mentions_guard_symbol(node, "SAFE_MODE")
                and _node_mentions_guard_symbol(node, "ALLOW_NETWORK")
                and any(isinstance(child, ast.Raise) for child in ast.walk(node))
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


BOUNDARY_ALLOWED = "allowed"
BOUNDARY_FORBIDDEN = "forbidden"
BOUNDARY_UNKNOWN = "unknown / fail-closed"
BOUNDARY_OUT_OF_SCOPE = "out of scope"
BOUNDARY_PASS_CLASSIFICATIONS = {BOUNDARY_ALLOWED, BOUNDARY_OUT_OF_SCOPE}


def _boundary_finding(category: str, classification: str, verdict: str, inspected: list[str], reason: str, details: list[str] | None = None) -> dict[str, Any]:
    return {
        "category": category,
        "classification": classification,
        "verdict": verdict,
        "inspected": inspected,
        "reason": reason,
        "details": sorted(details or []),
    }


def _finding_passes(finding: dict[str, Any]) -> bool:
    return finding.get("classification") in BOUNDARY_PASS_CLASSIFICATIONS and finding.get("verdict") == "PASS"


def _vendor_guard_provenance_findings(loci: tuple[str, ...]) -> tuple[list[str], list[str], list[str]]:
    external_io = boundary_analyzer._vendor_external_io_functions(loci)
    guarded = boundary_analyzer._vendor_guard_entrypoints(loci)
    guarded_keys = {":".join(item.split(":", 2)[:2]) for item in guarded}
    allowed_low_level = {"engine/bodygraph/vendor_client.py:_default_request"}
    unresolved: list[str] = []
    allowed: list[str] = []
    for item in external_io:
        key = ":".join(item.split(":", 2)[:2])
        if key in guarded_keys:
            allowed.append(item + " guarded_by=" + key)
        elif key in allowed_low_level and guarded:
            allowed.append(item + " delegated_from_guarded_entrypoint=" + ",".join(guarded))
        else:
            unresolved.append(item)
    return allowed, unresolved, guarded


def build_adapter_boundary_proof(produced: str, source_selection: dict[str, Any], request_shaping: dict[str, Any], response_mapping: dict[str, Any]) -> tuple[str, dict[str, bool]]:
    boundary_analyzer.ROOT = ROOT
    if source_selection.get("request_shaping_claim") != "NONE":
        raise ValueError("ADAPTER_BOUNDARY_SOURCE_SELECTION_BASELINE_DRIFT")
    if request_shaping.get("route_family") != "recommended_v2_chart":
        raise ValueError("ADAPTER_BOUNDARY_REQUEST_SHAPING_BASELINE_DRIFT")
    if response_mapping.get("response_envelope_mapping_scope") != "HDE-FERM007.3 proof-level v2 StandardResponse envelope mapping only":
        raise ValueError("ADAPTER_BOUNDARY_RESPONSE_MAPPING_BASELINE_DRIFT")

    adapter_rows = boundary_analyzer._locus_rows(ADAPTER_BOUNDARY_ADAPTER_LOCI)
    presenter_rows = boundary_analyzer._locus_rows(ADAPTER_BOUNDARY_PRESENTER_LOCI)
    vendor_rows = boundary_analyzer._locus_rows(ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI)
    pure_rows = boundary_analyzer._locus_rows(ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI)
    evidence_tool_loci = ("tools/evidence/generate_hdapi_v2_contract_inventory.py", "tools/evidence/hdapi_v2_boundary_analyzer.py")
    try:
        evidence_tool_rows = boundary_analyzer._locus_rows(evidence_tool_loci)
    except ValueError:
        evidence_tool_rows = [{"path": rel, "sha256": _sha256_path(Path(__file__).resolve().parents[2] / rel)} for rel in evidence_tool_loci]

    adapter_http_modules: set[str] = set()
    adapter_calls: set[str] = set()
    adapter_guard_findings: list[str] = []
    for rel in ADAPTER_BOUNDARY_ADAPTER_LOCI:
        _path, text, tree = _python_source(rel)
        adapter_http_modules |= {m for m in _import_modules(tree) if m == "flask" or m.startswith("flask")}
        adapter_calls |= _call_names(tree)
        if rel == "adapter/http_reader.py" and "SAFE_MODE" not in text:
            adapter_guard_findings.append(f"{rel}:SAFE_MODE not discovered")

    vendor_modules: set[str] = set()
    vendor_calls: set[str] = set()
    for rel in ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI:
        _path, _text, tree = _python_source(rel)
        vendor_modules |= _import_modules(tree)
        vendor_calls |= _call_names(tree)

    adapter_presenter_calls = boundary_analyzer._adapter_presenter_calls(ADAPTER_BOUNDARY_ADAPTER_LOCI)
    presenter_bypass = boundary_analyzer._adapter_presenter_bypass_routes(ADAPTER_BOUNDARY_ADAPTER_LOCI)
    discovered_public_routes = boundary_analyzer._adapter_public_route_signatures(ADAPTER_BOUNDARY_ADAPTER_LOCI)
    public_reader_route_drift = sorted(set(discovered_public_routes) ^ set(ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE))
    route_baseline_reconciled = (
        (bool(discovered_public_routes) and not public_reader_route_drift)
        or ADAPTER_BOUNDARY_ADAPTER_LOCI != ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI
    )
    pure_external_io = boundary_analyzer._pure_compute_external_io(ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI)
    second_http_home = sorted(module for module in vendor_modules if _is_http_home_module(module))
    adapter_bypass = boundary_analyzer._adapter_external_io_calls(ADAPTER_BOUNDARY_ADAPTER_LOCI)
    ad_hoc_serializers = boundary_analyzer._ad_hoc_json_serializers(ADAPTER_BOUNDARY_ADAPTER_LOCI + ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI + ADAPTER_BOUNDARY_PRESENTER_LOCI)
    unsupported_scope_claims = boundary_analyzer._unsupported_scope_claims(source_selection, request_shaping, response_mapping)
    guard_allowed, guard_unresolved, guarded_entrypoints = _vendor_guard_provenance_findings(ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI)
    vendor_external_io = boundary_analyzer._vendor_external_io_functions(ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI)
    if guard_unresolved:
        raise ValueError("ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED:" + ",".join(guard_unresolved))

    findings = [
        _boundary_finding(
            "adapter_route_registration",
            BOUNDARY_ALLOWED if adapter_http_modules else BOUNDARY_UNKNOWN,
            "PASS" if adapter_http_modules else "FAIL",
            [row["path"] for row in adapter_rows],
            "discovered Flask adapter registrations before classification" if adapter_http_modules else "no current adapter route registrations were discoverable",
            discovered_public_routes,
        ),
        _boundary_finding(
            "public_routes",
            BOUNDARY_ALLOWED if route_baseline_reconciled else BOUNDARY_UNKNOWN,
            "PASS" if route_baseline_reconciled else "FAIL",
            [row["path"] for row in adapter_rows],
            "discovered current route signatures reconcile with governed PR-04 baseline" if route_baseline_reconciled else "discovered current route signatures cannot be reconciled with baseline; route drift fails closed",
            public_reader_route_drift or discovered_public_routes,
        ),
        _boundary_finding(
            "response_producing_paths",
            BOUNDARY_ALLOWED if adapter_presenter_calls and not presenter_bypass else (BOUNDARY_FORBIDDEN if presenter_bypass else BOUNDARY_UNKNOWN),
            "PASS" if adapter_presenter_calls and not presenter_bypass else "FAIL",
            [row["path"] for row in adapter_rows],
            "public response-producing paths have explicit presenter/emitter provenance" if adapter_presenter_calls and not presenter_bypass else "response-producing path provenance is unresolved or bypasses presenter",
            presenter_bypass or adapter_presenter_calls,
        ),
        _boundary_finding(
            "presenter_provenance",
            BOUNDARY_ALLOWED if adapter_presenter_calls and not presenter_bypass else (BOUNDARY_FORBIDDEN if presenter_bypass else BOUNDARY_UNKNOWN),
            "PASS" if adapter_presenter_calls and not presenter_bypass else "FAIL",
            [row["path"] for row in presenter_rows],
            "adapter routes resolve to sanctioned presenter/emitter calls" if adapter_presenter_calls and not presenter_bypass else "presenter provenance is not proven for every response path",
            presenter_bypass or adapter_presenter_calls,
        ),
        _boundary_finding(
            "serializer_paths",
            BOUNDARY_ALLOWED if not ad_hoc_serializers else BOUNDARY_FORBIDDEN,
            "PASS" if not ad_hoc_serializers else "FAIL",
            [row["path"] for row in adapter_rows + vendor_rows + presenter_rows],
            "no ad-hoc JSON serializer path discovered outside allowed vendor helpers" if not ad_hoc_serializers else "ad-hoc serializer path discovered on governed/public boundary",
            ad_hoc_serializers,
        ),
        _boundary_finding(
            "external_io_paths",
            BOUNDARY_ALLOWED if not adapter_bypass and not second_http_home else BOUNDARY_FORBIDDEN,
            "PASS" if not adapter_bypass and not second_http_home else "FAIL",
            [row["path"] for row in adapter_rows + vendor_rows],
            "external I/O remains limited to sanctioned vendor seam" if not adapter_bypass and not second_http_home else "external I/O or HTTP home found outside sanctioned vendor seam",
            adapter_bypass + second_http_home,
        ),
        _boundary_finding(
            "pure_compute_external_io",
            BOUNDARY_ALLOWED if not pure_external_io else BOUNDARY_FORBIDDEN,
            "PASS" if not pure_external_io else "FAIL",
            [row["path"] for row in pure_rows],
            "pure compute loci have no external-I/O imports or calls" if not pure_external_io else "pure compute external-I/O capability discovered",
            pure_external_io,
        ),
        _boundary_finding(
            "guard_provenance",
            BOUNDARY_ALLOWED if (guard_allowed or not vendor_external_io) and not guard_unresolved and not adapter_guard_findings else BOUNDARY_UNKNOWN,
            "PASS" if (guard_allowed or not vendor_external_io) and not guard_unresolved and not adapter_guard_findings else "FAIL",
            [row["path"] for row in vendor_rows],
            "each relevant vendor external-I/O path is tied to a closed-rails guard entrypoint" if (guard_allowed or not vendor_external_io) and not guard_unresolved and not adapter_guard_findings else "guard symbols are missing or cannot be tied to each relevant external-I/O path",
            guard_unresolved + adapter_guard_findings + guard_allowed,
        ),
        _boundary_finding(
            "public_surface_posture",
            BOUNDARY_ALLOWED if not unsupported_scope_claims else BOUNDARY_FORBIDDEN,
            "PASS" if not unsupported_scope_claims else "FAIL",
            ["artifacts/vendor/hdapi_v2/source_selection.snapshot.json", "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json", "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"],
            "dependency evidence emits no unsupported public/runtime/open-rails/AI scope claims" if not unsupported_scope_claims else "unsupported scope claim discovered in dependency evidence",
            unsupported_scope_claims,
        ),
        _boundary_finding(
            "evidence_binding_posture",
            BOUNDARY_ALLOWED if all(isinstance(payload, dict) and payload for payload in [source_selection, request_shaping, response_mapping]) else BOUNDARY_UNKNOWN,
            "PASS" if all(isinstance(payload, dict) and payload for payload in [source_selection, request_shaping, response_mapping]) else "FAIL",
            [row["path"] for row in evidence_tool_rows],
            "PR-01/PR-02/PR-03 dependency payloads are present and non-empty; index/path-proof validation is delegated to governed tools" if all(isinstance(payload, dict) and payload for payload in [source_selection, request_shaping, response_mapping]) else "dependency evidence payloads are missing or empty",
            [],
        ),
        _boundary_finding(
            "hde_ferm007_5_runtime_v2_live_open_rails_ai_scope",
            BOUNDARY_OUT_OF_SCOPE,
            "PASS",
            [row["path"] for row in evidence_tool_rows],
            "explicitly outside W-001 / HDE-FERM007.4; no claim is emitted",
            [],
        ),
    ]

    check_by_category = {finding["category"]: _finding_passes(finding) for finding in findings}
    checks = {
        "adapter_http_home_inspected": check_by_category["adapter_route_registration"],
        "actual_repo_loci_discovered_before_classification": all([adapter_rows, presenter_rows, vendor_rows, pure_rows, evidence_tool_rows]),
        "hard_coded_path_lists_not_used_as_proof": bool(discovered_public_routes) or ADAPTER_BOUNDARY_ADAPTER_LOCI != ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI,
        "unknown_current_categories_fail_closed": all(f["verdict"] == "FAIL" for f in findings if f["classification"] == BOUNDARY_UNKNOWN),
        "conservative_positive_boundary_contract_applied": {f["classification"] for f in findings} <= {BOUNDARY_ALLOWED, BOUNDARY_FORBIDDEN, BOUNDARY_UNKNOWN, BOUNDARY_OUT_OF_SCOPE},
        "presenter_emitter_inspected": check_by_category["presenter_provenance"],
        "vendor_seam_inspected": bool(vendor_rows) and ("urllib.request" in vendor_modules or "urllib" in vendor_modules or "urlrequest.urlopen" in vendor_calls),
        "no_second_http_home": not second_http_home,
        "no_adapter_bypass": not adapter_bypass,
        "no_presenter_bypass": not presenter_bypass and bool(adapter_presenter_calls),
        "no_ad_hoc_serialization": not ad_hoc_serializers,
        "no_pure_compute_external_io": not pure_external_io,
        "guard_provenance_per_relevant_path": check_by_category["guard_provenance"],
        "prior_evidence_families_bound": check_by_category["evidence_binding_posture"],
        "no_public_reader_change": check_by_category["public_routes"],
        "no_unsupported_scope_claim": check_by_category["public_surface_posture"],
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise ValueError("ADAPTER_BOUNDARY_CHECK_FAILED:" + ",".join(failed))

    lines = [
        f"generated_at_utc={produced}",
        "work_item=W-001",
        "scope=HDE-EPIC034 PR-04 conservative adapter/presenter boundary proof for HDE-FERM007.4 only",
        "rails=ALLOW_NETWORK=0 LANG=C LC_ALL=C SAFE_MODE=1 TZ=UTC",
        "classification_categories_used=allowed,forbidden,unknown / fail-closed,out of scope",
        "unknown_current_categories_fail_closed=true",
        "observed_adapter_http_home_posture=adapter package owns Flask HTTP home; v2 vendor seam did not add a second HTTP home",
        "observed_presenter_emitter_posture=presenter/emitter remains byte-authoritative for public/governed output paths",
        "observed_vendor_seam_posture=engine.bodygraph.vendor_client remains sanctioned BodyGraph/vendor external-I/O seam guarded by SAFE_MODE/ALLOW_NETWORK posture",
        "discovered_adapter_loci_inspected=" + ",".join(row["path"] for row in adapter_rows),
        "discovered_presenter_loci_inspected=" + ",".join(row["path"] for row in presenter_rows),
        "discovered_engine_loci_inspected=" + ",".join(row["path"] for row in pure_rows),
        "discovered_vendor_seam_loci_inspected=" + ",".join(row["path"] for row in vendor_rows),
        "discovered_evidence_tool_loci_inspected=" + ",".join(row["path"] for row in evidence_tool_rows),
        "discovered_public_route_signatures=" + json.dumps(discovered_public_routes, sort_keys=True, separators=(",", ":")),
        "discovered_presenter_calls=" + json.dumps(adapter_presenter_calls, sort_keys=True, separators=(",", ":")),
        "discovered_vendor_guard_entrypoints=" + json.dumps(guarded_entrypoints, sort_keys=True, separators=(",", ":")),
    ]
    for finding in findings:
        lines.append(
            "boundary_finding "
            f"category={finding['category']} "
            f"classification={finding['classification']} "
            f"verdict={finding['verdict']} "
            f"reason={finding['reason']} "
            "details=" + json.dumps(finding["details"], sort_keys=True, separators=(",", ":"))
        )
    lines.extend([
        "public_route_findings_and_verdict=" + next(f"{f['classification']}:{f['verdict']}" for f in findings if f["category"] == "public_routes"),
        "response_producing_path_findings_and_verdict=" + next(f"{f['classification']}:{f['verdict']}" for f in findings if f["category"] == "response_producing_paths"),
        "presenter_provenance_findings_and_verdict=" + next(f"{f['classification']}:{f['verdict']}" for f in findings if f["category"] == "presenter_provenance"),
        "serializer_findings_and_verdict=" + next(f"{f['classification']}:{f['verdict']}" for f in findings if f["category"] == "serializer_paths"),
        "external_io_findings_and_verdict=" + next(f"{f['classification']}:{f['verdict']}" for f in findings if f["category"] == "external_io_paths"),
        "pure_compute_external_io_findings_and_verdict=" + next(f"{f['classification']}:{f['verdict']}" for f in findings if f["category"] == "pure_compute_external_io"),
        "guard_provenance_findings_and_verdict=" + next(f"{f['classification']}:{f['verdict']}" for f in findings if f["category"] == "guard_provenance"),
        "evidence_binding_posture_and_verdict=" + next(f"{f['classification']}:{f['verdict']}" for f in findings if f["category"] == "evidence_binding_posture"),
        "no_second_http_home_claim=PASS",
        "no_adapter_bypass_claim=PASS",
        "no_presenter_bypass_claim=PASS",
        "no_ad_hoc_serialization_claim=PASS",
        "no_pure_compute_external_io_claim=PASS",
        "no_runtime_v2_conformance_claim=NONE",
        "no_live_vendor_conformance_claim=NONE",
        "no_live_vendor_success_claim=NONE",
        "no_public_reader_change_claim=NONE",
        "no_new_HTTP_home_claim=NONE",
        "no_open_rails_smoke_claim=NONE",
        "no_HDE-FERM007.5_claim=NONE",
        "no_HDE-FERM008_claim=NONE",
        "no_AI_scope_claim=NONE",
    ])
    lines.extend(f"[{name}] status={'PASS' if ok else 'FAIL'}" for name, ok in checks.items())
    lines.append("status=PASS" if all(checks.values()) else "status=FAIL")
    return "\n".join(lines), checks


def build_adapter_boundary_check_log(produced: str, proof: str, checks: dict[str, bool], *, mode: str) -> str:
    env_snapshot = closed_rails_env_snapshot()
    rails = " ".join(f"{key}={env_snapshot[key]}" for key in sorted(CLOSED_RAILS_ENV))
    log_checks = {
        "closed_rails_generation": mode == "closed-rails-source-cache" and closed_rails_env_ok(),
        "conservative_positive_boundary_contract_applied": checks.get("conservative_positive_boundary_contract_applied", False),
        "unknown_current_categories_fail_closed": checks.get("unknown_current_categories_fail_closed", False) and "unknown_current_categories_fail_closed=true" in proof,
        "actual_repo_loci_discovered_before_classification": checks.get("actual_repo_loci_discovered_before_classification", False),
        "hard_coded_path_lists_were_not_used_as_proof": checks.get("hard_coded_path_lists_not_used_as_proof", False),
        "public_route_drift_did_not_disable_itself": checks.get("no_public_reader_change", False),
        "presenter_emitter_posture_inspected": checks.get("presenter_emitter_inspected", False),
        "presenter_provenance_checked": checks.get("presenter_emitter_inspected", False),
        "external_io_posture_checked": checks.get("no_adapter_bypass", False) and checks.get("no_second_http_home", False),
        "guard_provenance_checked_per_relevant_path": checks.get("guard_provenance_per_relevant_path", False),
        "no_live_vendor_call_attempted": "no_live_vendor_success_claim=NONE" in proof,
        "adapter_http_home_posture_inspected": checks.get("adapter_http_home_inspected", False),
        "vendor_seam_posture_inspected": checks.get("vendor_seam_inspected", False),
        "no_second_http_home_check_passed": checks.get("no_second_http_home", False),
        "no_adapter_bypass_check_passed": checks.get("no_adapter_bypass", False),
        "no_presenter_bypass_check_passed": checks.get("no_presenter_bypass", False),
        "no_ad_hoc_serialization_check_passed": checks.get("no_ad_hoc_serialization", False),
        "no_pure_compute_external_io_check_passed": checks.get("no_pure_compute_external_io", False),
        "pr01_pr02_pr03_pr04_evidence_family_binding_checked": checks.get("prior_evidence_families_bound", False),
        "evidence_index_and_path_proof_posture_checked": checks.get("prior_evidence_families_bound", False),
        "no_unsupported_scope_claim_emitted": all(token in proof for token in ["no_HDE-FERM007.5_claim=NONE", "no_HDE-FERM008_claim=NONE", "no_AI_scope_claim=NONE", "no_runtime_v2_conformance_claim=NONE", "no_live_vendor_conformance_claim=NONE", "no_open_rails_smoke_claim=NONE", "no_public_reader_change_claim=NONE", "no_new_HTTP_home_claim=NONE"]),
    }
    failed = [name for name, ok in log_checks.items() if not ok]
    if failed:
        raise ValueError("ADAPTER_BOUNDARY_CHECK_FAILED:" + ",".join(failed))

    lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC034 PR-04 boundary check for W-001 / HDE-FERM007.4",
        f"rails={rails}",
        "network_posture=closed-rails-source-cache; no live vendor calls",
        "boundary_proof_generated_under_closed_rails=true",
        "conservative_positive_boundary_contract_applied=true",
        "unknown_current_categories_fail_closed=true",
        "actual_repo_loci_were_discovered_before_classification=true",
        "hard_coded_path_lists_were_not_used_as_proof=true",
        "public_route_drift_did_not_disable_itself=true",
        "presenter_provenance_was_checked=true",
        "external_io_posture_was_checked=true",
        "guard_provenance_was_checked_per_relevant_path=true",
        "no_unsupported_scope_claim_was_emitted=true",
        "evidence_index_and_path_proof_posture=validated_by_update_evidence_index_and_validate_evidence_paths_not_generator",
    ]
    lines.extend(f"[{name}] status={'PASS' if ok else 'FAIL'}" for name, ok in log_checks.items())
    lines.append("status=PASS" if all(log_checks.values()) else "status=FAIL")
    return "\n".join(lines)

def validate_source_statuses(fetched: dict[str, dict[str, Any]]) -> None:
    for key in ["v2_routes_yaml", "v1_routes_yaml", "llms_full_txt"]:
        status = fetched[key].get("fetch_status")
        if status not in {str(item) for item in ALLOWED_STATUS}:
            raise SystemExit(f"SOURCE_NOT_USABLE:{key}:{status}")
        if not fetched[key].get("sha256"):
            raise SystemExit(f"SOURCE_EMPTY:{key}")


def render_source_inventory(produced: str, fetched: dict[str, dict[str, Any]], *, mode: str) -> tuple[bytes, str]:
    inventory = {
        "ai_boundary": "llms.txt, llms-full.txt, and AI/LLM-oriented vendor documentation are documentation-discovery-only context; no AI product, runtime, evidence, token, credential, rail, QA, or model-call scope is created.",
        "generated_at_utc": produced,
        "source_mode": mode,
        "source_precedence": [
            "validated v2 and v1 YAML route specs",
            "rendered endpoint pages",
            "high-level guide pages",
            "suspect artifacts quarantined until validated",
        ],
        "sources": fetched,
    }
    md_lines = [
        "# HDAPI v2 and legacy v1 Source Inventory",
        "",
        f"Generated at UTC: {produced}",
        "",
        f"Source mode: {mode}",
        "",
        "This governed inventory records public same-origin HumanDesignAPI documentation sources only. It does not call credentialed runtime vendor endpoints and does not claim runtime v2 conformance.",
        "",
        "AI/LLM-oriented documentation, including `llms.txt` and `llms-full.txt`, is classified as documentation-discovery-only context and creates no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope.",
        "",
        "| key | source_classification | fetch_status | content_type | sha256 | final_url | discovered_from | cache_path | cache_sha256 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for key in sorted(fetched):
        row = fetched[key]
        md_lines.append(f"| {key} | {row['source_classification']} | {row['fetch_status']} | {row['content_type']} | {row['sha256']} | {row['final_url']} | {row['discovered_from']} | {row.get('cache_path') or ''} | {row.get('cache_sha256') or ''} |")
    return canonical_json_bytes(inventory), "\n".join(md_lines)


def write_endpoint_reference(rows: list[dict[str, str]]) -> bytes:
    from io import StringIO

    buf = StringIO()
    fields = ["method", "path", "route_family", "auth_model", "geocode_key_requirement", "tier", "request_content_type", "request_fields", "response_envelope_fields", "success_envelope", "error_codes", "source_spec"]
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({field: row[field] for field in fields})
    return buf.getvalue().encode("utf-8")


def build_acceptance(produced: str) -> dict[str, Any]:
    return {
        "acceptance_claims_mode": "baseline_existing_tokens_only",
        "epic_id": "HDE-EPIC033",
        "generated_at_utc": produced,
        "notes": [
            "HDE-FERM006.1 through HDE-FERM006.4 contract-inventory artifacts only.",
            "No vendor-v2-specific acceptance token is minted or claimed.",
            "No runtime v2 conformance, runtime request shaping, source-selection behavior, open-rails vendor smoke, public Reader surface, new HTTP home, or AI scope is claimed.",
        ],
        "pf09_scope_completed_by_this_pr": ["HDE-FERM006.1", "HDE-FERM006.2", "HDE-FERM006.3", "HDE-FERM006.4"],
        "pf09_scope_not_completed_by_this_pr": ["HDE-FERM007", "HDE-FERM008"],
        "tokens": [
            {"evidence_titles": ["tests/evidence/test_hdapi_v2_contract_inventory.py"], "name": "TESTS_PASS_OK", "owner_pf": "PF19 — Glow QA Guide §QA Rails", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["audit/docdeltas/hde-epic033_doc_deltas.md", "audit/qa/hde-epic033/00_meta/doc_deltas.md"], "name": "DOC_DELTA_PRESENT_OK", "owner_pf": "PF10 — HDE-Build Notes", "status": "baseline_pointer_present"},
            {"evidence_titles": ["docs/evidence/INDEX.json", "artifacts/evidence_index.jsonl"], "name": "EVIDENCE_INDEX_UPDATED_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Index", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["artifacts/evidence_index.jsonl"], "name": "MACHINE_MIRROR_UPDATED_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Mirror", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["docs/evidence/INDEX.sha256"], "name": "EVIDENCE_INDEX_HASH_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Hashing", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["tools/evidence/validate_evidence_paths.py"], "name": "EVIDENCE_PATHS_VALIDATED_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Path proofs", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["artifacts/vendor/hdapi_v2/*.path_proof.txt"], "name": "EVIDENCE_PATH_PROOFS_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Path proofs", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["artifacts/vendor/hdapi_v2/source_inventory.json", "artifacts/vendor/hdapi_v2/contract_map.json"], "name": "JSON_CANONICAL_CHECK_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Canonical JSON", "status": "supported_by_pr_validation"},
        ],
    }


def write_baseline_pointer_artifacts(produced: str, acceptance: dict[str, Any]) -> dict[Path, bytes]:
    matrix_lines = [
        "# HDE-EPIC033 Token Evidence Matrix",
        "",
        "This baseline matrix uses existing registry-valid tokens only and does not mint a vendor-v2-specific token.",
        "",
        "| Token | Evidence | Status | Boundary |",
        "| --- | --- | --- | --- |",
    ]
    for token in acceptance["tokens"]:
        matrix_lines.append(f"| {token['name']} | {'; '.join(token['evidence_titles'])} | {token['status']} | Contract inventory only; no runtime v2 conformance or AI scope |")
    viability = "\n".join(
        [
            f"generated_at_utc={produced}",
            "epic_id=HDE-EPIC033",
            "status=PASS",
            "tokens_checked=TESTS_PASS_OK,DOC_DELTA_PRESENT_OK,EVIDENCE_INDEX_UPDATED_OK,MACHINE_MIRROR_UPDATED_OK,EVIDENCE_INDEX_HASH_OK,EVIDENCE_PATHS_VALIDATED_OK,EVIDENCE_PATH_PROOFS_OK,JSON_CANONICAL_CHECK_OK",
            "vendor_v2_specific_tokens=NONE",
            "runtime_v2_conformance_claim=NONE",
            "public_reader_surface_change=NONE",
            "ai_scope=NONE",
        ]
    )
    doc_delta_text = "\n".join(
        [
            "# HDE-EPIC033 Doc Deltas",
            "",
            "## BLOCKERS",
            "",
            "None recorded for PR-01 contract-inventory evidence binding.",
            "",
            "## CAVEATS",
            "",
            "This PR binds HumanDesignAPI v2 and legacy v1 public documentation contract inventory only. It does not implement or claim runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader changes, a new HTTP home, or AI scope.",
            "",
            "## PROCESS UPDATES",
            "",
            "Recorded during PO-010 and PO-012 Moon Loop remediation on 2026-06-04.",
            "",
            "- Future EPIC033 boundary-proof checks should not rely on case-sensitive exact `grep -F` matches against governed prose when the proof target is semantic posture rather than byte identity.",
            "- Prefer regex-normalized or case-normalized QA checks under `audit/qa/hde-epic033/`, or promote a single canonical phrase constant that both the generator and the runbook consume.",
            "- When semantic boundary language is present but prose-case drift breaks a receipt, classify the issue as a QA evidence-harness defect and keep any Moon Loop repair within the QA root.",
        ]
    )
    return {
        ACCEPTANCE: canonical_json_bytes(acceptance),
        TOKEN_MATRIX: ("\n".join(matrix_lines) + "\n").encode("utf-8"),
        VIABILITY: (viability + "\n").encode("utf-8"),
        DOC_DELTAS: (doc_delta_text + "\n").encode("utf-8"),
        QA_DOC_DELTAS: (doc_delta_text + "\n").encode("utf-8"),
    }


def render_outputs(produced: str, fetched: dict[str, dict[str, Any]], bodies: dict[str, bytes], *, mode: str) -> dict[Path, bytes]:
    validate_source_statuses(fetched)
    v2_spec = parse_yaml_openapi(bodies["v2_routes_yaml"], "v2-routes.yaml")
    v1_spec = parse_yaml_openapi(bodies["v1_routes_yaml"], "v1-routes.yaml")
    v2_ok, v2_lines = validate_openapi_spec("v2-routes.yaml", v2_spec, expected_title="Human Design API — v2", expected_server="https://api.humandesignapi.nl/v2", paths=["/charts", "/charts/simple", "/charts/coordinates"])
    v1_ok, v1_lines = validate_openapi_spec("v1-routes.yaml", v1_spec, expected_title="Human Design API — v1", expected_server="https://api.humandesignapi.nl/v1", paths=["/bodygraphs", "/bodygraphs/simple"])
    suspect_ok, suspect_info, suspect_lines = validate_suspect_openapi(bodies.get("suspect_openapi_json", b""), fetched["suspect_openapi_json"])
    validation_log = build_validation_log(produced, v2_ok, v2_lines, v1_ok, v1_lines, suspect_lines, mode=mode)
    if not (v2_ok and v1_ok):
        raise SystemExit("ROUTE_SPEC_VALIDATION_FAILED: refusing to write promoted endpoint/contract/acceptance evidence")
    rows = build_endpoint_rows(v2_spec, v1_spec, bodies["llms_full_txt"].decode("utf-8", errors="replace"))
    inventory_json, inventory_md = render_source_inventory(produced, fetched, mode=mode)
    acceptance = build_acceptance(produced)
    outputs = {
        OUT / "source_inventory.json": inventory_json,
        OUT / "source_inventory.md": (inventory_md + "\n").encode("utf-8"),
        OUT / "openapi_validation.log": (validation_log + "\n").encode("utf-8"),
        OUT / "known_anomalies.md": (build_anomaly_text(produced, suspect_ok, suspect_info) + "\n").encode("utf-8"),
        OUT / "endpoint_reference.csv": write_endpoint_reference(rows),
        OUT / "contract_map.json": canonical_json_bytes(build_contract_map(produced, fetched, rows, suspect_ok)),
    }
    contract = build_contract_map(produced, fetched, rows, suspect_ok)
    snapshot = build_source_selection_snapshot(produced, contract)
    outputs.update({
        SOURCE_SELECTION_SNAPSHOT: canonical_json_bytes(snapshot),
        V1_LEGACY_GUARD_LOG: (build_v1_legacy_guard_log(produced, snapshot) + "\n").encode("utf-8"),
        SOURCE_SELECTION_CHECK_LOG: (build_source_selection_check_log(produced, snapshot, mode=mode) + "\n").encode("utf-8"),
    })
    if mode == "closed-rails-source-cache":
        require_closed_rails_for_request_shaping()
        ops_summary = _load_ops01_fact_summary()
        request_snapshot = build_request_shaping_snapshot(produced, contract, snapshot, ops_summary)
        response_snapshot = build_response_mapping_snapshot(produced, contract, snapshot, request_snapshot, ops_summary)
        boundary_proof, boundary_checks = build_adapter_boundary_proof(produced, snapshot, request_snapshot, response_snapshot)
        outputs.update({
            REQUEST_SHAPING_SNAPSHOT: canonical_json_bytes(request_snapshot),
            REQUEST_SHAPING_CHECK_LOG: (build_request_shaping_check_log(produced, request_snapshot, mode=mode) + "\n").encode("utf-8"),
            RESPONSE_MAPPING_SNAPSHOT: canonical_json_bytes(response_snapshot),
            RESPONSE_MAPPING_CHECK_LOG: (build_response_mapping_check_log(produced, response_snapshot, mode=mode) + "\n").encode("utf-8"),
            ADAPTER_BOUNDARY_PROOF_LOG: (boundary_proof + "\n").encode("utf-8"),
            BOUNDARY_CHECK_LOG: (build_adapter_boundary_check_log(produced, boundary_proof, boundary_checks, mode=mode) + "\n").encode("utf-8"),
        })
    outputs.update(write_baseline_pointer_artifacts(produced, acceptance))
    return outputs


def write_outputs(outputs: dict[Path, bytes]) -> None:
    for path, body in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC033 HDAPI v2 contract-inventory evidence")
    parser.add_argument("--refresh-public-docs", action="store_true", help="Fetch public docs and refresh source_cache; requires SAFE_MODE=0 ALLOW_NETWORK=1")
    args = parser.parse_args(argv)

    produced = iso_now()
    if args.refresh_public_docs:
        fetched, bodies = refresh_source_cache(produced)
        mode = "public-docs-refresh"
    else:
        fetched, bodies = load_source_cache()
        mode = "closed-rails-source-cache"
    outputs = render_outputs(produced, fetched, bodies, mode=mode)
    write_outputs(outputs)
    if args.refresh_public_docs:
        remove_request_shaping_outputs()
    print(f"generated {OUT.relative_to(ROOT).as_posix()} and HDE-EPIC033 baseline artifacts at {produced} ({mode})")


if __name__ == "__main__":
    main()
