#!/usr/bin/env python3
"""PO-authorized post-deploy smoke (HDE-COAG003.5); never run as PR validation.

Runs the governed post-deploy checks against one deployed HD Engine service and
writes the capture set into one evidence directory, with a retained-path
manifest (HDE-EPIC043 Specification delta 01, D14 and C-16; PF10 addendum 2.8).

* Seven fixed read-only probes; no credential, chart, identity or valid Reader
  request is ever sent, and no request writes.
* The three A7 success-route proofs ``success_get.txt``, ``success_head.txt``
  and ``success_304.txt`` are never captured (Product Owner waiver C-16). The
  production refusal of the catalog's A7 route ``GET /reader`` is captured in
  their place.
* A read-only DB posture spot-check through ``engine.db.DBAccess`` compares the
  live introspection results with the governed ``artifacts/db/*`` posture files.
* Logs are keys-only; the files carry only the governed posture headers, the
  public ``/internal/version`` body and hashes. Every file is scanned before
  anything is written. A precondition refusal writes nothing.
* The harness writes no path proof, Evidence Index row or Machine Mirror row;
  the evidence updater indexes the capture in the Ops evidence pull request.

Exit codes: 0 PASS; 2 usage error; 3 precondition refusal; 4 completed with a
FAIL or a refused check; 5 secret scan refused the files; 6 write failure.
"""
from __future__ import annotations

import argparse
import hashlib
import http.client
import ipaddress
import json
import os
import re
import ssl
import subprocess
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.db import DBAccess  # noqa: E402
from engine.db.adapter import retired_db_transport_keys_present  # noqa: E402
from engine.db.errors import AdapterError  # noqa: E402
from engine.serializer.canon import sercanon  # noqa: E402
from tools.evidence.retained_evidence_safety import validate_retained_text_safety  # noqa: E402

HARNESS_REL = "scripts/ops/post_deploy_smoke.py"
CATALOG_PATH = ROOT / "docs/ENDPOINTS_CATALOG.json"
DB_REFERENCE_DIR = ROOT / "artifacts/db"
DB_REFERENCE_FILES = ("check_constraints.txt", "check_schema.txt", "ddl_fingerprint.json", "grants.txt")
# The tracked DDL that check_constraints.txt cites as its source. Its unique clause is
# what the reference label ``unique_body_graph_identity`` stands for: the label is not
# a database object name, so DB-3 compares constraint definitions, not names.
DDL_SOURCE_REL = "migrations/011_body_graphs_durability.sql"
DDL_SOURCE_PATH = ROOT / DDL_SOURCE_REL
PROTECTED_DIRS = ("artifacts/proofs", "artifacts/ops/internal_version", "artifacts/db")
READER_A7_ROUTE = "/reader"
TIMEOUT_SECONDS = 10
JSON_CONTENT_TYPE = "application/json; charset=utf-8"
INTERNAL_VERSION_KEYS = (
    "engine_tag",
    "build_commit",
    "invocation_tag",
    "invocation_sha256",
    "emitter_sha256",
    "release_id",
)
OPS_TASK_REF_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{2,127}\Z")
ERROR_CODE_RE = re.compile(r"ERR_[A-Z0-9_]+\Z")
RECORDABLE_HEADER_RE = re.compile(r"[A-Za-z0-9 ;=/,._+-]{1,128}\Z")
TARGET_APP_ENVS = ("prod",)

EXIT_PASS = 0
EXIT_REFUSED = 3
EXIT_FAIL = 4
EXIT_UNSAFE = 5
EXIT_WRITE_FAILED = 6

# The capture set, in write order. ``HDE_EPIC043_SMOKE_FILES`` in
# tools/evidence/update_evidence_index.py registers exactly these names.
CAPTURE_FILES = (
    "env_pins.txt",
    "headers_get.txt",
    "body_get.json",
    "body_get.sha256",
    "headers_head.txt",
    "cond_if_none_match_headers.txt",
    "cond_if_modified_since_headers.txt",
    "provenance_note.md",
    "success_writers_errors.txt",
    "reader_refusal_get.txt",
    "db_posture_spot_check.json",
    "retained_path_manifest.json",
)
WAIVED_PROOFS = ("success_304.txt", "success_get.txt", "success_head.txt")
REFUSAL_DELIVERABLE = "production refusal of GET /reader"
DB_DELIVERABLE = "DB posture spot-check result"

MANIFEST_KEYS = frozenset(
    {
        "captured_at_utc",
        "entries",
        "evidence_dir",
        "harness",
        "manifest_version",
        "nonclaims",
        "ops_task_ref",
        "reference_inputs",
        "run_result",
    }
)
ENTRY_KEYS = frozenset(
    {
        "basis",
        "check",
        "check_result",
        "deliverable",
        "retained_path",
        "sha256",
        "size_bytes",
        "source",
        "status",
        "substitute_for",
    }
)
STATUSES = frozenset({"CAPTURED", "EQUIVALENT_BY_MAPPING", "NOT_CAPTURED_UNDER_C16"})
CHECK_RESULTS = frozenset({"PASS", "FAIL", "REFUSED", "NOT_RUN"})
NONCLAIMS = (
    "no QA verdict",
    "no acceptance",
    "no PF09 status movement",
    "no production A7 success-route behaviour",
    "no comparison of the deployed release_id with an expected value",
    "no path proof, Evidence Index row or Machine Mirror row",
    "server rails not observed",
)


@dataclass(frozen=True)
class Probe:
    id: str
    check: str
    method: str
    target: str
    headers: tuple[tuple[str, str], ...]
    body: bytes | None
    label: str


_IDENTITY = (("Accept-Encoding", "identity"),)
_JSON_POST = (("Accept-Encoding", "identity"), ("Content-Type", "application/json"))

PROBES: tuple[Probe, ...] = (
    Probe("P-1", "H-02", "GET", "/internal/version", _IDENTITY, None, "GET /internal/version"),
    Probe("P-2", "H-03", "HEAD", "/internal/version", _IDENTITY, None, "HEAD /internal/version"),
    Probe(
        "P-3",
        "H-04",
        "GET",
        "/internal/version",
        _IDENTITY + (("If-None-Match", "xyz"),),
        None,
        "GET /internal/version",
    ),
    Probe(
        "P-4",
        "H-04",
        "GET",
        "/internal/version",
        _IDENTITY + (("If-Modified-Since", "Wed, 21 Oct 2015 07:28:00 GMT"),),
        None,
        "GET /internal/version",
    ),
    # Not JSON: no valid Reader request can equal it.
    Probe("P-5", "H-06", "POST", "/api/reader?v=1", _JSON_POST, b"{", "POST /api/reader?v=1 body=not_json"),
    # An unsupported version; version validation precedes the body.
    Probe("P-6", "H-06", "POST", "/api/reader?v=9", _JSON_POST, b"{}", "POST /api/reader?v=9 body=unsupported_version"),
    # The catalog's A7 route with the minimal valid version (the refusal needs v=1).
    Probe("P-7", "H-07", "GET", READER_A7_ROUTE + "?v=1", _IDENTITY, None, "GET /reader?v=1"),
)


class Refusal(Exception):
    """A typed, value-free precondition refusal."""

    def __init__(self, token: str):
        super().__init__(token)
        self.token = token


@dataclass(frozen=True)
class Target:
    scheme: str
    host: str
    port: int
    proxy: tuple[str, int] | None = None


@dataclass(frozen=True)
class Response:
    status: int | None
    headers: tuple[tuple[str, str], ...]
    body: bytes
    error: str | None = None


# --- preconditions -----------------------------------------------------------


def _base_target(base_url: str) -> Target:
    parts = urllib.parse.urlsplit(base_url)
    host = parts.hostname
    if (
        parts.scheme not in ("https", "http")
        or not host
        or "@" in parts.netloc
        or parts.query
        or parts.fragment
        or parts.path not in ("", "/")
    ):
        raise Refusal("BASE_URL_FORM")
    try:
        port = parts.port
    except ValueError:
        raise Refusal("BASE_URL_FORM") from None
    if parts.scheme == "http":
        try:
            loopback = ipaddress.ip_address(host).is_loopback
        except ValueError:
            loopback = False
        if not loopback:
            raise Refusal("BASE_URL_FORM")
    return Target(parts.scheme, host, port or (443 if parts.scheme == "https" else 80))


def _with_proxy(target: Target, environ: Mapping[str, str]) -> Target:
    if target.scheme != "https":
        return target
    proxy_url = environ.get("HTTPS_PROXY") or environ.get("https_proxy") or ""
    if not proxy_url:
        return target
    no_proxy = environ.get("NO_PROXY") or environ.get("no_proxy") or ""
    if urllib.request.proxy_bypass_environment(target.host, {"no": no_proxy}):
        return target
    parts = urllib.parse.urlsplit(proxy_url)
    if (
        parts.scheme != "http"
        or not parts.hostname
        or "@" in parts.netloc
        or parts.query
        or parts.fragment
        or parts.path not in ("", "/")
    ):
        raise Refusal("PROXY_FORM")
    try:
        port = parts.port or 80
    except ValueError:
        raise Refusal("PROXY_FORM") from None
    return Target(target.scheme, target.host, target.port, (parts.hostname, port))


def _connection_target(base_url: str, environ: Mapping[str, str]) -> Target:
    return _with_proxy(_base_target(base_url), environ)


def _protected(resolved: Path) -> bool:
    for rel in PROTECTED_DIRS:
        base = (ROOT / rel).resolve()
        if resolved == base or base in resolved.parents:
            return True
    return False


def _check_evidence_dir(evidence_dir: Path) -> Path:
    resolved = evidence_dir.resolve()
    if _protected(resolved):
        raise Refusal("EVIDENCE_DIR_PROTECTED")
    if resolved.exists() or resolved.is_symlink():
        if not resolved.is_dir():
            raise Refusal("EVIDENCE_DIR_NOT_A_DIRECTORY")
        if any(resolved.iterdir()):
            raise Refusal("EVIDENCE_DIR_NOT_EMPTY")
    return resolved


def _strict_json(data: bytes) -> Any:
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError("duplicate key")
        return dict(items)

    return json.loads(data.decode("utf-8"), object_pairs_hook=pairs)


def _read_references() -> tuple[dict[str, bytes], bytes]:
    try:
        catalog_bytes = CATALOG_PATH.read_bytes()
        catalog = _strict_json(catalog_bytes)
    except (OSError, ValueError):
        raise Refusal("CATALOG_ROUTE") from None
    route = {"method": "GET", "path": READER_A7_ROUTE}
    endpoints = catalog.get("endpoints") if isinstance(catalog, dict) else None
    if (
        not isinstance(catalog, dict)
        or catalog.get("success_endpoints") != [route]
        or not isinstance(endpoints, list)
        or not any(
            isinstance(row, dict)
            and row.get("method") == "GET"
            and row.get("path") == READER_A7_ROUTE
            and row.get("a7_eligible") is True
            for row in endpoints
        )
    ):
        raise Refusal("CATALOG_ROUTE")
    references: dict[str, bytes] = {}
    for rel, path in [(f"artifacts/db/{name}", DB_REFERENCE_DIR / name) for name in DB_REFERENCE_FILES] + [
        (DDL_SOURCE_REL, DDL_SOURCE_PATH)
    ]:
        if path.is_symlink() or not path.is_file():
            raise Refusal("REFERENCE_INPUT_MISSING")
        references[rel] = path.read_bytes()
    return references, catalog_bytes


def _preflight(args: argparse.Namespace, environ: Mapping[str, str]) -> tuple[Target, Path, dict[str, bytes], bytes]:
    if (environ.get("LC_ALL"), environ.get("LANG"), environ.get("TZ")) != ("C", "C", "UTC"):
        raise Refusal("LOCALE_PINS")
    target = _base_target(args.base_url)
    evidence_dir = _check_evidence_dir(Path(args.evidence_dir))
    if retired_db_transport_keys_present(environ):
        raise Refusal("RETIRED_DB_TRANSPORT_KEYS")
    if environ.get("SAFE_MODE") not in ("0", "1") or environ.get("ALLOW_NETWORK") not in ("0", "1"):
        raise Refusal("RAILS_POSTURE_UNSET")
    if not OPS_TASK_REF_RE.fullmatch(args.ops_task_ref or ""):
        raise Refusal("OPS_TASK_REF_INVALID")
    if args.target_app_env not in TARGET_APP_ENVS:
        raise Refusal("TARGET_APP_ENV_UNSUPPORTED")
    target = _with_proxy(target, environ)
    references, catalog_bytes = _read_references()
    return target, evidence_dir, references, catalog_bytes


# --- probes --------------------------------------------------------------------


def _send(target: Target, probe: Probe) -> Response:
    try:
        if target.scheme == "https":
            context = ssl.create_default_context()
            if target.proxy is not None:
                conn: http.client.HTTPConnection = http.client.HTTPSConnection(
                    target.proxy[0], target.proxy[1], timeout=TIMEOUT_SECONDS, context=context
                )
                conn.set_tunnel(target.host, target.port)
            else:
                conn = http.client.HTTPSConnection(
                    target.host, target.port, timeout=TIMEOUT_SECONDS, context=context
                )
        else:
            conn = http.client.HTTPConnection(target.host, target.port, timeout=TIMEOUT_SECONDS)
        try:
            conn.request(probe.method, probe.target, body=probe.body, headers=dict(probe.headers))
            response = conn.getresponse()
            body = response.read()
            return Response(response.status, tuple(response.getheaders()), body)
        finally:
            conn.close()
    except (OSError, http.client.HTTPException) as exc:
        return Response(None, (), b"", type(exc).__name__)


def _header_values(response: Response, name: str) -> list[str]:
    lowered = name.lower()
    return [value for key, value in response.headers if key.lower() == lowered]


def _single(response: Response, name: str) -> str | None:
    values = _header_values(response, name)
    return values[0] if len(values) == 1 else None


def _recordable(response: Response, name: str) -> str:
    values = _header_values(response, name)
    if not values:
        return "<absent>"
    if len(values) > 1:
        return "<multiple>"
    value = values[0]
    return value if RECORDABLE_HEADER_RE.fullmatch(value) else "<unrecordable>"


def _content_length(response: Response) -> int | None:
    value = _single(response, "Content-Length")
    if value is None or not value.isdigit():
        return None
    return int(value)


def _governed_posture(response: Response) -> list[str]:
    """Reasons the governed no-store, no-ETag, JSON posture fails; empty when it holds."""
    reasons = []
    for name in ("Cache-Control", "Content-Type", "Content-Length", "ETag"):
        if len(_header_values(response, name)) > 1:
            reasons.append("duplicate_" + name.lower())
    if _single(response, "Cache-Control") != "no-store":
        reasons.append("cache_control")
    if _header_values(response, "ETag"):
        reasons.append("etag_present")
    if _single(response, "Content-Type") != JSON_CONTENT_TYPE:
        reasons.append("content_type")
    return reasons


def _canonical_identity_body(body: bytes) -> dict[str, str] | None:
    if not body.endswith(b"\n") or body.endswith(b"\n\n"):
        return None
    try:
        obj = _strict_json(body)
    except (UnicodeDecodeError, ValueError):
        return None
    if not isinstance(obj, dict) or tuple(obj) != INTERNAL_VERSION_KEYS:
        return None
    if not all(isinstance(value, str) for value in obj.values()):
        return None
    if sercanon(obj, sort_keys=False) != body:
        return None
    return obj


def _typed_error(body: bytes) -> tuple[str | None, bool, bool]:
    """Return (code, numeric_free, canonical) for a typed JSON error body."""
    numbers: list[str] = []

    def number(text: str) -> int:
        numbers.append(text)
        return 0

    try:
        obj = json.loads(
            body.decode("utf-8"),
            parse_int=number,
            parse_float=number,
            parse_constant=number,
        )
        numeric_free = not numbers
        exact = _strict_json(body)
    except (UnicodeDecodeError, ValueError):
        return None, False, False
    if not isinstance(obj, dict) or obj.get("ok") is not False:
        return None, numeric_free, False
    code = obj.get("code")
    if not isinstance(code, str) or not ERROR_CODE_RE.fullmatch(code):
        return None, numeric_free, False
    return code, numeric_free, sercanon(exact) == body


# --- checks --------------------------------------------------------------------


@dataclass
class Outcome:
    result: str
    reasons: list[str]


def _classify_get(response: Response) -> tuple[Outcome, dict[str, str] | None]:
    if response.status is None:
        return Outcome("FAIL", ["no_response"]), None
    reasons = []
    if response.status != 200:
        reasons.append("status")
    reasons.extend(_governed_posture(response))
    if _content_length(response) != len(response.body):
        reasons.append("content_length")
    identity = _canonical_identity_body(response.body)
    if identity is None:
        reasons.append("body_not_canonical")
    return Outcome("FAIL" if reasons else "PASS", reasons), identity


def _classify_head(response: Response, get: Response) -> Outcome:
    if response.status is None:
        return Outcome("FAIL", ["no_response"])
    reasons = []
    if response.status != 200:
        reasons.append("status")
    if response.body:
        reasons.append("body_present")
    reasons.extend(_governed_posture(response))
    if get.status is None or _content_length(response) != len(get.body):
        reasons.append("content_length")
    return Outcome("FAIL" if reasons else "PASS", reasons)


def _classify_conditional(response: Response, get: Response) -> Outcome:
    if response.status is None:
        return Outcome("FAIL", ["no_response"])
    reasons = []
    if response.status != 200:
        reasons.append("status")
    reasons.extend(_governed_posture(response))
    if _content_length(response) != len(response.body):
        reasons.append("content_length")
    if get.status is None or response.body != get.body:
        reasons.append("body_differs")
    return Outcome("FAIL" if reasons else "PASS", reasons)


def _classify_error(response: Response, *, expected_code: str | None) -> tuple[Outcome, str | None, bool, bool]:
    if response.status is None:
        return Outcome("FAIL", ["no_response"]), None, False, False
    reasons = []
    if expected_code is None:
        if not 400 <= response.status <= 499:
            reasons.append("status")
    elif response.status != 403:
        reasons.append("status")
    reasons.extend(_governed_posture(response))
    code, numeric_free, canonical = _typed_error(response.body)
    if code is None:
        reasons.append("untyped")
    elif expected_code is not None and code != expected_code:
        reasons.append("code")
    if not numeric_free:
        reasons.append("numeric")
    if not canonical:
        reasons.append("body_not_canonical")
    return Outcome("FAIL" if reasons else "PASS", reasons), code, numeric_free, canonical


# --- DB posture spot-check (H-08) ---------------------------------------------

_CONSTRAINT_LINE = re.compile(r"PASS constraint (?P<name>[A-Za-z0-9_]+) source=(?P<source>\S+)\Z")
_UNIQUE_CLAUSE = re.compile(r"unique \((?P<columns>[a-z0-9_]+(?:, ?[a-z0-9_]+)*)\)")
_NOT_NULL_LINE = re.compile(r"PASS not_null hde\.body_graphs\.(?P<column>[A-Za-z0-9_]+) source=\S+\Z")
_CHECK_LINE = re.compile(r"PASS check hde\.body_graphs\.[A-Za-z0-9_]+ predicate=\S.* source=\S+\Z")


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _refs(references: Mapping[str, bytes], *names: str) -> list[dict[str, str]]:
    return [{"path": rel, "sha256": _sha256(references[rel])} for rel in sorted(names)]


def _columns(text: str) -> tuple[str, ...]:
    return tuple(part.strip() for part in text.split(","))


def _tracked_unique_clauses(ddl_source: bytes) -> list[tuple[str, ...]] | None:
    """The unique column lists of ``hde.body_graphs`` in the tracked DDL, normalized as
    tools/evidence/generate_db_runtime_posture.py normalizes it; ``None`` if absent."""
    text = re.sub(r"--.*", "", ddl_source.decode("utf-8", "replace"))
    text = re.sub(r"\s+", " ", text).strip().lower()
    start = text.find("create table if not exists hde.body_graphs (")
    if start < 0:
        return None
    end = text.find(");", start)
    if end < 0:
        return None
    return [_columns(match["columns"]) for match in _UNIQUE_CLAUSE.finditer(text[start:end])]


def _item(item_id: str, result: str, reason: str | None, references: Mapping[str, bytes], *names: str) -> dict[str, Any]:
    return {"id": item_id, "reason": reason, "references": _refs(references, *names), "result": result}


def compare_db_posture(
    search_path: Any,
    fingerprint: Any,
    grants: Any,
    references: Mapping[str, bytes],
) -> dict[str, Any]:
    """Compare live introspection results with the governed posture files.

    Only DB-1 to DB-4 can PASS; ``NOT_COMPARABLE`` and ``CAPTURED_BY_HASH`` never
    count as PASS. View definitions, defaults and constraint definitions are read
    for presence only and never returned.
    """
    items: list[dict[str, Any]] = []
    try:
        ddl = _strict_json(references["artifacts/db/ddl_fingerprint.json"])
        if not isinstance(ddl, dict):
            raise ValueError("ddl")
    except (UnicodeDecodeError, ValueError):
        ddl = None
    schema_lines = references["artifacts/db/check_schema.txt"].decode("utf-8", "replace").splitlines()
    schema_ref = schema_lines[0].strip() if schema_lines else ""

    # DB-1 search path.
    live_path = search_path.get("search_path") if isinstance(search_path, Mapping) else None
    if ddl is None or not schema_ref or not isinstance(ddl.get("search_path"), str):
        items.append(_item("DB-1", "FAIL", "REFERENCE_UNPARSED", references, "artifacts/db/check_schema.txt", "artifacts/db/ddl_fingerprint.json"))
    elif schema_ref != ddl["search_path"]:
        items.append(_item("DB-1", "FAIL", "REFERENCE_DISAGREES", references, "artifacts/db/check_schema.txt", "artifacts/db/ddl_fingerprint.json"))
    elif live_path != schema_ref:
        items.append(_item("DB-1", "FAIL", "SEARCH_PATH_DIFFERS", references, "artifacts/db/check_schema.txt", "artifacts/db/ddl_fingerprint.json"))
    else:
        items.append(_item("DB-1", "PASS", None, references, "artifacts/db/check_schema.txt", "artifacts/db/ddl_fingerprint.json"))

    # DB-2 objects.
    objects = fingerprint.get("objects") if isinstance(fingerprint, Mapping) else None
    names = ddl.get("objects") if ddl is not None else None
    if not isinstance(names, list) or not names or not all(isinstance(name, str) for name in names):
        items.append(_item("DB-2", "FAIL", "REFERENCE_UNPARSED", references, "artifacts/db/ddl_fingerprint.json"))
    elif not isinstance(objects, Mapping):
        items.append(_item("DB-2", "FAIL", "LIVE_SHAPE", references, "artifacts/db/ddl_fingerprint.json"))
    else:
        absent = []
        for name in names:
            entry = objects.get(name)
            if not isinstance(entry, Mapping):
                absent.append(name)
            elif "columns" in entry:
                if not isinstance(entry["columns"], list) or not entry["columns"]:
                    absent.append(name)
            elif not (isinstance(entry.get("definition"), str) and entry["definition"].strip()):
                absent.append(name)
        if absent:
            items.append(_item("DB-2", "FAIL", "OBJECT_ABSENT:" + ",".join(absent), references, "artifacts/db/ddl_fingerprint.json"))
        else:
            items.append(_item("DB-2", "PASS", None, references, "artifacts/db/ddl_fingerprint.json"))

    # DB-3 and DB-4 from check_constraints.txt.
    unique: list[str] = []
    not_null: list[str] = []
    unparsed = False
    for line in references["artifacts/db/check_constraints.txt"].decode("utf-8", "replace").splitlines():
        if not line.strip():
            continue
        if match := _CONSTRAINT_LINE.fullmatch(line):
            unique.append(match["name"])
            if match["source"] != DDL_SOURCE_REL:
                unparsed = True
        elif match := _NOT_NULL_LINE.fullmatch(line):
            not_null.append(match["column"])
        elif not _CHECK_LINE.fullmatch(line):
            unparsed = True
    table = objects.get("hde.body_graphs") if isinstance(objects, Mapping) else None
    live_constraints = table.get("constraints") if isinstance(table, Mapping) else None
    live_columns = table.get("columns") if isinstance(table, Mapping) else None
    # DB-3: each reference unique constraint is a label for a unique clause of the
    # tracked DDL; the live definitions (pg_get_constraintdef) must carry each clause.
    tracked = _tracked_unique_clauses(references[DDL_SOURCE_REL])
    db3_refs = ("artifacts/db/check_constraints.txt", DDL_SOURCE_REL)
    if unparsed or not unique or tracked is None or len(tracked) != len(unique):
        items.append(_item("DB-3", "FAIL", "REFERENCE_UNPARSED", references, *db3_refs))
    elif not isinstance(live_constraints, list):
        items.append(_item("DB-3", "FAIL", "LIVE_SHAPE", references, *db3_refs))
    else:
        live_unique = set()
        for row in live_constraints:
            definition = row.get("definition") if isinstance(row, Mapping) else None
            if isinstance(definition, str):
                match = _UNIQUE_CLAUSE.fullmatch(" ".join(definition.lower().split()))
                if match:
                    live_unique.add(_columns(match["columns"]))
        missing = [clause for clause in tracked if clause not in live_unique]
        if missing:
            items.append(_item("DB-3", "FAIL", f"UNIQUE_ABSENT:{len(missing)}", references, *db3_refs))
        else:
            items.append(_item("DB-3", "PASS", None, references, *db3_refs))
    if unparsed or not not_null:
        items.append(_item("DB-4", "FAIL", "REFERENCE_UNPARSED", references, "artifacts/db/check_constraints.txt"))
    elif not isinstance(live_columns, list):
        items.append(_item("DB-4", "FAIL", "LIVE_SHAPE", references, "artifacts/db/check_constraints.txt"))
    else:
        nullable = {
            row.get("name"): row.get("nullable") for row in live_columns if isinstance(row, Mapping)
        }
        wrong = [column for column in not_null if nullable.get(column) is not False]
        if wrong:
            items.append(_item("DB-4", "FAIL", "NULLABLE:" + ",".join(wrong), references, "artifacts/db/check_constraints.txt"))
        else:
            items.append(_item("DB-4", "PASS", None, references, "artifacts/db/check_constraints.txt"))

    # DB-5 to DB-7: the introspection helper cannot supply them.
    items.append(_item("DB-5", "NOT_COMPARABLE", "HELPER_READS_UNIQUE_CONSTRAINTS_ONLY", references, "artifacts/db/check_constraints.txt"))
    items.append(_item("DB-6", "NOT_COMPARABLE", "NEEDS_CHECK_CONSTRAINTS", references, "artifacts/db/ddl_fingerprint.json"))
    items.append(_item("DB-7", "NOT_COMPARABLE", "OFFLINE_HASH_OF_TRACKED_DDL", references, "artifacts/db/ddl_fingerprint.json"))
    # DB-8: grants captured by hash and presence only.
    items.append(_item("DB-8", "CAPTURED_BY_HASH", None, references, "artifacts/db/grants.txt"))

    passed = all(item["result"] == "PASS" for item in items if item["id"] in {"DB-1", "DB-2", "DB-3", "DB-4"})
    return {
        "check_result": "PASS" if passed else "FAIL",
        "grants_sha256": _sha256(sercanon(grants)),
        "items": items,
    }


def _live_db_reader(environ: Mapping[str, str]) -> dict[str, Any]:
    access = DBAccess.for_current_env(environ=environ)
    return {
        "search_path": access.introspect_search_path(),
        "fingerprint": access.introspect_fingerprint(),
        "grants": access.introspect_grants(),
    }


def _db_check(
    environ: Mapping[str, str],
    references: Mapping[str, bytes],
    db_reader: Callable[[], Mapping[str, Any]] | None,
) -> dict[str, Any]:
    database_url = "SET" if (environ.get("DATABASE_URL") or "").strip() else "UNSET"
    record: dict[str, Any] = {
        "check": "H-08",
        "check_result": "FAIL",
        "database_url": database_url,
        "error_code": None,
        "grants_sha256": None,
        "items": [],
        "refusal": None,
    }
    if db_reader is None:
        if database_url == "UNSET":
            record["check_result"] = "REFUSED"
            record["refusal"] = "DATABASE_URL_UNSET"
            return record

        def db_reader() -> Mapping[str, Any]:
            return _live_db_reader(environ)

    try:
        live = db_reader()
    except AdapterError as exc:
        record["error_code"] = str(getattr(exc, "code", None) or type(exc).__name__)
        return record
    except Exception as exc:  # the live database is an external system; record, never crash
        record["error_code"] = "unexpected:" + type(exc).__name__
        return record
    record.update(
        compare_db_posture(live.get("search_path"), live.get("fingerprint"), live.get("grants"), references)
    )
    return record


# --- files ---------------------------------------------------------------------


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _headers_text(probe: Probe, response: Response, outcome: Outcome, *, request_header: str | None = None) -> bytes:
    lines = [f"Request: {probe.method} {probe.target}"]
    if request_header is not None:
        lines.append(f"Request-Header: {request_header}")
    if response.status is None:
        lines += ["Status: NO_RESPONSE", f"Error: {response.error}"]
    else:
        lines += [
            f"Status: {response.status}",
            f"Cache-Control: {_recordable(response, 'Cache-Control')}",
            f"Content-Length: {_recordable(response, 'Content-Length')}",
            f"Content-Type: {_recordable(response, 'Content-Type')}",
            "ETag: " + ("<present>" if _header_values(response, "ETag") else "<absent>"),
            f"Body-Length: {len(response.body)} bytes",
            f"Body-SHA256: {_sha256(response.body)}",
        ]
    lines.append(f"Result: {outcome.result}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _error_block(
    probe: Probe,
    response: Response,
    outcome: Outcome,
    code: str | None,
    numeric_free: bool,
    canonical: bool,
    extra: Sequence[str] = (),
) -> list[str]:
    lines = [probe.label]
    if response.status is None:
        lines += ["status=NO_RESPONSE", f"error={response.error}"]
    else:
        lines += [
            f"status={response.status}",
            f"code={code or '<untyped>'}",
            f"cache_control={_recordable(response, 'Cache-Control')}",
            "etag_absent=" + ("false" if _header_values(response, "ETag") else "true"),
            f"content_type={_recordable(response, 'Content-Type')}",
            "numeric_free=" + ("true" if numeric_free else "false"),
            "canonical_body=" + ("true" if canonical else "false"),
        ]
    lines += list(extra)
    lines.append(f"result={outcome.result}")
    return lines


def _python_version() -> str:
    return ".".join(str(part) for part in sys.version_info[:3])


def _checkout_head() -> str:
    try:
        result = subprocess.run(
            ("git", "rev-parse", "HEAD"),
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return "not a git checkout"
    head = result.stdout.strip()
    return head if result.returncode == 0 and re.fullmatch(r"[0-9a-f]{40,64}", head) else "not a git checkout"


def _evidence_dir_label(evidence_dir: Path) -> str:
    try:
        return evidence_dir.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return "<outside-repository>"


def validate_manifest(obj: Any) -> None:
    """Raise ``ValueError`` unless ``obj`` is a manifest of the closed shape."""
    if not isinstance(obj, dict) or set(obj) != MANIFEST_KEYS:
        raise ValueError("manifest keys")
    if obj["manifest_version"] != 1 or obj["run_result"] not in ("PASS", "FAIL"):
        raise ValueError("manifest header")
    if not isinstance(obj["harness"], dict) or set(obj["harness"]) != {"path", "sha256"}:
        raise ValueError("manifest harness")
    if not isinstance(obj["reference_inputs"], list) or not all(
        isinstance(row, dict) and set(row) == {"path", "sha256"} for row in obj["reference_inputs"]
    ):
        raise ValueError("manifest reference inputs")
    if list(obj["nonclaims"]) != list(NONCLAIMS):
        raise ValueError("manifest nonclaims")
    entries = obj["entries"]
    if not isinstance(entries, list):
        raise ValueError("manifest entries")
    names = []
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != ENTRY_KEYS:
            raise ValueError("manifest entry keys")
        if entry["status"] not in STATUSES or entry["check_result"] not in CHECK_RESULTS:
            raise ValueError("manifest entry vocabulary")
        if entry["source"] not in ("HDE-COAG003.5", "D14"):
            raise ValueError("manifest entry source")
        waived = entry["status"] == "NOT_CAPTURED_UNDER_C16"
        if waived != (entry["retained_path"] is None):
            raise ValueError("manifest waived entry path")
        if waived and (
            entry["basis"] != "C-16"
            or entry["check"] is not None
            or entry["check_result"] != "NOT_RUN"
            or entry["sha256"] is not None
            or entry["size_bytes"] is not None
        ):
            raise ValueError("manifest waived entry")
        names.append(entry["deliverable"])
    expected = sorted(
        [name for name in CAPTURE_FILES if name not in {"db_posture_spot_check.json", "reader_refusal_get.txt", "retained_path_manifest.json"}]
        + [DB_DELIVERABLE, REFUSAL_DELIVERABLE, *WAIVED_PROOFS]
    )
    if names != expected:
        raise ValueError("manifest deliverables")


def _manifest(
    *,
    files: Mapping[str, bytes],
    check_results: Mapping[str, str],
    evidence_dir: Path,
    captured_at: str,
    ops_task_ref: str,
    run_result: str,
    reference_inputs: list[dict[str, str]],
) -> bytes:
    checks_by_file = {
        "env_pins.txt": "H-01",
        "headers_get.txt": "H-02",
        "body_get.json": "H-02",
        "body_get.sha256": "H-02",
        "headers_head.txt": "H-03",
        "cond_if_none_match_headers.txt": "H-04",
        "cond_if_modified_since_headers.txt": "H-04",
        "provenance_note.md": "H-05",
        "success_writers_errors.txt": "H-06",
        "reader_refusal_get.txt": "H-07",
        "db_posture_spot_check.json": "H-08",
    }

    def captured(deliverable: str, name: str, status: str, basis: str | None, substitute_for: list[str] | None) -> dict[str, Any]:
        check = checks_by_file[name]
        return {
            "basis": basis,
            "check": check,
            "check_result": check_results[check],
            "deliverable": deliverable,
            "retained_path": name,
            "sha256": _sha256(files[name]),
            "size_bytes": len(files[name]),
            "source": "D14" if status == "EQUIVALENT_BY_MAPPING" else "HDE-COAG003.5",
            "status": status,
            "substitute_for": substitute_for,
        }

    entries = [
        captured(name, name, "CAPTURED", None, None)
        for name in checks_by_file
        if name not in {"db_posture_spot_check.json", "reader_refusal_get.txt"}
    ]
    entries.append(captured(DB_DELIVERABLE, "db_posture_spot_check.json", "EQUIVALENT_BY_MAPPING", None, None))
    entries.append(
        captured(REFUSAL_DELIVERABLE, "reader_refusal_get.txt", "EQUIVALENT_BY_MAPPING", "C-16", list(WAIVED_PROOFS))
    )
    entries += [
        {
            "basis": "C-16",
            "check": None,
            "check_result": "NOT_RUN",
            "deliverable": name,
            "retained_path": None,
            "sha256": None,
            "size_bytes": None,
            "source": "HDE-COAG003.5",
            "status": "NOT_CAPTURED_UNDER_C16",
            "substitute_for": None,
        }
        for name in WAIVED_PROOFS
    ]
    manifest = {
        "captured_at_utc": captured_at,
        "entries": sorted(entries, key=lambda entry: entry["deliverable"]),
        "evidence_dir": _evidence_dir_label(evidence_dir),
        "harness": {"path": HARNESS_REL, "sha256": _sha256(Path(__file__).read_bytes())},
        "manifest_version": 1,
        "nonclaims": list(NONCLAIMS),
        "ops_task_ref": ops_task_ref,
        "reference_inputs": reference_inputs,
        "run_result": run_result,
    }
    validate_manifest(manifest)
    return sercanon(manifest)


def _create_file(path: Path, data: bytes) -> None:
    """Create ``path`` exclusively and write ``data``.

    Once the exclusive creation has succeeded the file is this run's: if its
    write or close then fails, the partly written file is removed before the
    error propagates, so nothing partial is left behind.
    """
    handle = open(path, "xb")
    try:
        with handle:
            handle.write(data)
    except OSError:
        try:
            path.unlink()
        except OSError:
            pass
        raise


def _write_all(evidence_dir: Path, files: Mapping[str, bytes]) -> bool:
    created_dir = False
    created: list[Path] = []
    try:
        if not evidence_dir.exists():
            evidence_dir.mkdir(parents=True)
            created_dir = True
        for name in CAPTURE_FILES:
            path = evidence_dir / name
            _create_file(path, files[name])
            created.append(path)
    except OSError:
        for path in reversed(created):
            try:
                path.unlink()
            except OSError:
                pass
        if created_dir:
            try:
                evidence_dir.rmdir()
            except OSError:
                pass
        return False
    return True


# --- main ----------------------------------------------------------------------


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="PO-authorized post-deploy smoke (HDE-COAG003.5); never run as PR validation"
    )
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--evidence-dir", required=True)
    parser.add_argument("--ops-task-ref", required=True)
    parser.add_argument("--target-app-env", required=True)
    return parser


def _refuse(token: str, code: int = EXIT_REFUSED) -> int:
    print(f"OPS_REFUSED:{token}", file=sys.stderr)
    return code


def main(
    argv: Sequence[str] | None = None,
    *,
    environ: Mapping[str, str] | None = None,
    db_reader: Callable[[], Mapping[str, Any]] | None = None,
) -> int:
    env = os.environ if environ is None else environ
    args = _parser().parse_args(argv)
    try:
        target, evidence_dir, references, catalog_bytes = _preflight(args, env)
    except Refusal as refusal:
        return _refuse(refusal.token)

    captured_at = _utc_now()
    responses = {probe.id: _send(target, probe) for probe in PROBES}
    by_id = {probe.id: probe for probe in PROBES}
    get = responses["P-1"]

    h02, identity = _classify_get(get)
    h03 = _classify_head(responses["P-2"], get)
    h04_inm = _classify_conditional(responses["P-3"], get)
    h04_ims = _classify_conditional(responses["P-4"], get)
    h04 = Outcome("PASS" if h04_inm.result == h04_ims.result == "PASS" else "FAIL", h04_inm.reasons + h04_ims.reasons)
    h06_blocks = [_classify_error(responses[pid], expected_code=None) for pid in ("P-5", "P-6")]
    h06 = Outcome("PASS" if all(block[0].result == "PASS" for block in h06_blocks) else "FAIL", [])
    h07, h07_code, h07_numeric, h07_canonical = _classify_error(responses["P-7"], expected_code="ERR_READER_FORBIDDEN")
    db_record = _db_check(env, references, db_reader)

    check_results = {
        "H-01": "PASS",
        "H-02": h02.result,
        "H-03": h03.result,
        "H-04": h04.result,
        "H-05": "PASS" if h02.result == "PASS" else "FAIL",
        "H-06": h06.result,
        "H-07": h07.result,
        "H-08": db_record["check_result"],
    }
    run_result = "PASS" if all(value == "PASS" for value in check_results.values()) else "FAIL"

    reference_inputs = sorted(
        [{"path": "docs/ENDPOINTS_CATALOG.json", "sha256": _sha256(catalog_bytes)}]
        + [{"path": rel, "sha256": _sha256(data)} for rel, data in references.items()],
        key=lambda row: row["path"],
    )
    harness_sha = _sha256(Path(__file__).read_bytes())

    files: dict[str, bytes] = {}
    files["env_pins.txt"] = (
        "\n".join(
            [
                "LC_ALL=C",
                "LANG=C",
                "TZ=UTC",
                f"SAFE_MODE={env['SAFE_MODE']}",
                f"ALLOW_NETWORK={env['ALLOW_NETWORK']}",
                f"DATABASE_URL={db_record['database_url']}",
                "HTTPS_PROXY=" + ("SET" if (env.get("HTTPS_PROXY") or env.get("https_proxy")) else "UNSET"),
                "retired_db_transport_keys=none",
                f"target_app_env={args.target_app_env}",
                f"ops_task_ref={args.ops_task_ref}",
                f"python={_python_version()}",
                "server_rails=not_observable_over_http",
            ]
        )
        + "\n"
    ).encode("utf-8")
    files["headers_get.txt"] = _headers_text(by_id["P-1"], get, h02)
    files["body_get.json"] = get.body
    files["body_get.sha256"] = (_sha256(get.body) + "\n").encode("ascii")
    files["headers_head.txt"] = _headers_text(by_id["P-2"], responses["P-2"], h03)
    files["cond_if_none_match_headers.txt"] = _headers_text(
        by_id["P-3"], responses["P-3"], h04_inm, request_header="If-None-Match"
    )
    files["cond_if_modified_since_headers.txt"] = _headers_text(
        by_id["P-4"], responses["P-4"], h04_ims, request_header="If-Modified-Since"
    )

    identity_lines = (
        [f"- {key}: {identity[key]}" for key in INTERNAL_VERSION_KEYS]
        if identity is not None and h02.result == "PASS"
        else ["- not available: H-02 did not pass"]
    )
    files["provenance_note.md"] = (
        "\n".join(
            [
                "# Post-deploy smoke provenance",
                "",
                f"- Base URL: {args.base_url}",
                f"- Started (UTC): {captured_at}",
                f"- Ops task reference: {args.ops_task_ref}",
                f"- Harness: {HARNESS_REL} (sha256 {harness_sha})",
                f"- Checkout HEAD: {_checkout_head()}",
                f"- Run result: {run_result}",
                "",
                "## Deployed identity (served by GET /internal/version)",
                "",
                *identity_lines,
                "",
                "## Reference inputs",
                "",
                *[f"- {row['path']} sha256 {row['sha256']}" for row in reference_inputs],
                "",
                "## C-16",
                "",
                "The three A7 success-route proofs (success_get.txt, success_head.txt, success_304.txt)"
                " are not captured, under the Product Owner's waiver C-16. The production refusal of"
                " GET /reader is captured in their place in reader_refusal_get.txt.",
                "",
                "## Nonclaims",
                "",
                *[f"- {claim}" for claim in NONCLAIMS],
            ]
        )
        + "\n"
    ).encode("utf-8")

    blocks = []
    for pid, (outcome, code, numeric_free, canonical) in zip(("P-5", "P-6"), h06_blocks):
        blocks.append("\n".join(_error_block(by_id[pid], responses[pid], outcome, code, numeric_free, canonical)))
    files["success_writers_errors.txt"] = ("\n\n".join(blocks) + "\n").encode("utf-8")
    files["reader_refusal_get.txt"] = (
        "\n".join(
            _error_block(
                by_id["P-7"],
                responses["P-7"],
                h07,
                h07_code,
                h07_numeric,
                h07_canonical,
                extra=("route_source=docs/ENDPOINTS_CATALOG.json success_endpoints",),
            )
        )
        + "\n"
    ).encode("utf-8")
    files["db_posture_spot_check.json"] = sercanon(db_record)
    files["retained_path_manifest.json"] = _manifest(
        files=files,
        check_results=check_results,
        evidence_dir=evidence_dir,
        captured_at=captured_at,
        ops_task_ref=args.ops_task_ref,
        run_result=run_result,
        reference_inputs=reference_inputs,
    )

    for name in CAPTURE_FILES:
        if validate_retained_text_safety(Path(name), files[name]):
            return _refuse("RETAINED_TEXT_UNSAFE", EXIT_UNSAFE)

    if not _write_all(evidence_dir, files):
        return _refuse("EVIDENCE_WRITE_FAILED", EXIT_WRITE_FAILED)

    for check in ("H-01", "H-02", "H-03", "H-04", "H-05", "H-06", "H-07", "H-08"):
        print(f"SMOKE_CHECK:{check}:{check_results[check]}")
    print("SMOKE_CHECK:H-09:PASS")
    print(f"SMOKE_RESULT:{run_result}")
    print(f"SMOKE_FILES:{len(CAPTURE_FILES)}")
    print(f"SMOKE_MANIFEST_SHA256:{_sha256(files['retained_path_manifest.json'])}")
    return EXIT_PASS if run_result == "PASS" else EXIT_FAIL


if __name__ == "__main__":
    raise SystemExit(main())
