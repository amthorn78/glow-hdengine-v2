from __future__ import annotations

import argparse
import importlib.metadata
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Sequence, Tuple

from engine.bodygraph import resolve_bodygraph
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.mapped_cache import MappedBodyGraphRow, MappedCacheError, read_current_mapped_bodygraph
from engine.bodygraph.projection import BodyGraphProjectionError, canonical_uuid
from engine.bodygraph.resolver import ResolvedCompatChart, projection_refusal, resolve_compat_chart
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import (
    EvaluationParty,
    conjunction_public_resolved,
    evaluate_pair,
    evaluation_party,
    harmony_band,
    is_ineligible_carrier,
    orient,
)
from engine.compat.error_tokens import CompatBoundaryError
from engine.compat.thresholds import THRESHOLDS_V1
from engine.config.registry_loader import RegistryConfigError
from engine.db import DBAccess
from engine.db.errors import AdapterError
from engine.presenter import emitter
from engine.runtime import emit_reader_public_envelope, identity_meta
from engine.serializer.canon import sercanon
from engine.narratives import emit_public_aux, get_pack
from engine.narratives.constants import BANDS as AUX_BANDS, PERSPECTIVES as AUX_PERSPECTIVES
from engine.validation.viewer_prefs import normalize_viewer_prefs, validate_viewer_prefs
from engine.bodygraph.vendor_client import VendorError
from engine.sampler.core import CandidateFeatures, ViewerProfile, sample_and_rank

from ._admin_dump import canon_dump

_PROJECTION_KEYS = ("bodygraph", "person", "person_uid", "source")
_IDENTITY_KEYS = ("user_id", "canonical_person_id")
_BIRTH_KEYS = ("birthdate", "birthtime", "location")


class CliError(Exception):
    """Typed CLI failure used to map to process exit codes."""

    def __init__(self, code: str, exit_code: int = 64) -> None:
        super().__init__(code)
        self.code = code
        self.exit_code = exit_code


def _cli_version_text() -> str:
    engine_tag, release_id, _ = _engine_identity()
    try:
        package_version = importlib.metadata.version("glow-hdengine")
    except importlib.metadata.PackageNotFoundError:
        package_version = "0.0.0"
    return f"hdctl {package_version} ({engine_tag};{release_id})"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hdctl",
        description="Glow HD Engine compatibility CLI",
        allow_abbrev=False,
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="show program version and exit",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    show = sub.add_parser(
        "showcompat",
        help="Emit canonical Reader v1 bytes from vendor JSON (stdin or files)",
        allow_abbrev=False,
    )
    show.add_argument("--pair-file", help="Path to JSON with left/right payloads")
    show.add_argument("--a-file", dest="a_file", help="Path to JSON file containing the left payload")
    show.add_argument("--b-file", dest="b_file", help="Path to JSON file containing the right payload")
    show.add_argument("--a", dest="a_file", help="Alias for --a-file", metavar="A_FILE")
    show.add_argument("--b", dest="b_file", help="Alias for --b-file", metavar="B_FILE")
    show.add_argument(
        "--dump-reader",
        dest="dump_reader",
        help="Optional path to write public Reader JSON (canonical bytes)",
    )
    show.add_argument(
        "--dump-admin-dir",
        dest="dump_admin_dir",
        help="Directory for admin proofs (writes 0600 JSON + .sha256 sidecars)",
    )
    show.add_argument(
        "--source",
        choices=("db", "vendor", "auto"),
        help="Explicit BodyGraph source (db, vendor, or auto)",
    )
    show.add_argument(
        "--conjunction",
        action="store_true",
        help=(
            "Emit conjunction contract JSON (requires --user-a/--user-b or conjunction pair input; "
            "uses SAFE rails resolver gating)"
        ),
    )
    show.add_argument(
        "--viewer-prefs-file",
        dest="viewer_prefs_file",
        help="Path to JSON viewer prefs (top_category + weights)",
    )
    show.add_argument("--user-a", help="DB user identifier for party A")
    show.add_argument("--user-b", help="DB user identifier for party B")
    show.add_argument("--birthdate-a", dest="birthdate_a", help="Birthdate for party A (YYYY-MM-DD)")
    show.add_argument("--birthtime-a", dest="birthtime_a", help="Birth time for party A (HH:MM)")
    show.add_argument("--location-a", dest="location_a", help="Location for party A")
    show.add_argument("--birthdate-b", dest="birthdate_b", help="Birthdate for party B (YYYY-MM-DD)")
    show.add_argument("--birthtime-b", dest="birthtime_b", help="Birth time for party B (HH:MM)")
    show.add_argument("--location-b", dest="location_b", help="Location for party B")
    show.set_defaults(handler=showcompat)

    aux = sub.add_parser(
        "aux-preview",
        help="Preview Aux narrative text for a public tuple",
        allow_abbrev=False,
    )
    aux.add_argument("--category", help="Narrative category slug")
    aux.add_argument("--band", choices=AUX_BANDS)
    aux.add_argument("--perspective", choices=AUX_PERSPECTIVES)
    aux.add_argument("--pair-file", help="Compat JSON pair file from showcompat")
    aux.add_argument("--show-narrative", action="store_true", help="Emit narrative text to stdout")
    aux.add_argument("--admin-out", dest="admin_out", help="Write ids-only preview JSON")
    aux.set_defaults(handler=aux_preview)
    bg = sub.add_parser(
        "bg:resolve",
        help="Resolve BodyGraphs from db/vendor sources (Phase S8a stub)",
        allow_abbrev=False,
    )
    bg.add_argument("--user", required=True, help="BodyGraph user identifier")
    bg.add_argument(
        "--source",
        choices=("auto", "db", "vendor"),
        default="auto",
        help="Source to consult (default: auto)",
    )
    bg.add_argument(
        "--upsert",
        action="store_true",
        help="Request controlled durability upsert when the selected source supports it",
    )
    bg.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Emit planning envelope without performing writes",
    )
    bg.add_argument("--birthdate", help="Birthdate (YYYY-MM-DD) for vendor source")
    bg.add_argument("--birthtime", help="Birth time (HH:MM) for vendor source")
    bg.add_argument("--location", help="Location string for vendor source")
    bg.set_defaults(handler=bg_resolve)

    dev_sampler = sub.add_parser(
        "dev:sampler",
        help="DEV/ADMIN ONLY: deterministic sampler harness (seedable)",
        allow_abbrev=False,
    )
    dev_sampler.add_argument("--viewer", required=True, help="Viewer identifier for the sampler run")
    dev_sampler.add_argument(
        "--candidates-file",
        required=True,
        help="Path to JSON payload containing sampler candidates",
    )
    dev_sampler.add_argument(
        "--seed",
        help=(
            "Optional seed value (echoed only; reserved for deterministic tie-breakers in future phases)"
        ),
    )
    dev_sampler.set_defaults(handler=dev_sampler_run)
    return parser


def _resolver_env() -> Dict[str, str | None]:
    return {name: os.environ.get(name) for name in ("SAFE_MODE", "ALLOW_NETWORK", "APP_ENV", "HD_API_BASE_URL", "HDAPI_BASE_URL")}


def _load_viewer_prefs(path: str | None) -> Dict[str, Any]:
    base = {"top_category": CATEGORIES_ORDER_V1[0], "weights": _viewer_weights()}
    if not path:
        return base
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise CliError("VIEWER_PREFS_NOT_FOUND") from exc
    except OSError as exc:
        raise CliError("VIEWER_PREFS_READ_ERROR") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CliError("INVALID_VIEWER_PREFS") from exc
    err = validate_viewer_prefs(data)
    if err:
        raise CliError("INVALID_VIEWER_PREFS")
    return normalize_viewer_prefs(data)


def bg_resolve(args: argparse.Namespace) -> int:
    if args.source == "vendor":
        # PF-canon: vendor CLI invocations must supply the full birth tuple explicitly.
        missing = [name for name in ("birthdate", "birthtime", "location") if not getattr(args, name, None)]
        if missing:
            raise CliError("MISSING_VENDOR_INPUT", exit_code=64)
    result = resolve_bodygraph(
        args.user,
        source=args.source,
        upsert=bool(args.upsert),
        dry_run=bool(getattr(args, "dry_run", False)),
        env=_resolver_env(),
        birthdate=getattr(args, "birthdate", None),
        birthtime=getattr(args, "birthtime", None),
        location=getattr(args, "location", None),
    )
    output = emitter.emit_public(result.payload).decode("utf-8")
    sys.stdout.write(output)
    return result.exit_code


def cli(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--version" in argv:
        if len(argv) == 1:
            sys.stdout.write(f"{_cli_version_text()}\n")
            return 0
        sys.stderr.write("VERSION_FLAG_WITH_COMMAND\n")
        return 64

    parser = _build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:  # argparse already emitted help/usage
        code = int(exc.code or 0)
        return 64 if code else 0
    handler = getattr(args, "handler", None)
    if handler is None:
        parser.print_usage(sys.stderr)
        return 64
    try:
        return int(handler(args) or 0)
    except CliError as err:
        sys.stderr.write(f"{err.code}\n")
        return err.exit_code
    except CompatBoundaryError as exc:
        # PF05 §4.1.4: the stderr code string equals the error_v1 code for the same failure.
        sys.stderr.write(f"{exc.token}\n")
        return 1
    except VendorError as exc:
        sys.stderr.write(f"{exc.code}\n")
        return 1
    except RegistryConfigError as exc:
        # Admission refusal (for example INCOMPLETE_RELEASE_ROSTER) propagates unchanged.
        sys.stderr.write(f"{exc.code}\n")
        return 1
    except Exception as exc:  # pragma: no cover - defensive guard
        sys.stderr.write(f"CLI_UNEXPECTED:{exc}\n")
        return 1


def _parse_input(raw: str) -> Dict[str, Any]:
    if not raw.strip():
        raise CliError("EMPTY_INPUT")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:  # pragma: no cover - JSON path exercised by tests
        raise CliError("INVALID_JSON") from exc
    if not isinstance(data, dict):
        raise CliError("INVALID_JSON")
    return data


def _normalize_party(obj: Any, label: str) -> Dict[str, Any]:
    """Normalize one file/stdin party into the resolver's input shape.

    A complete mapped chart passes through with its identity slots; declared
    birth fields (top-level or under ``birth``) are lifted to the top level for
    the birth-seed identity route.  No chart is synthesized and no ``cli-``
    identity is derived; the resolver refuses incomplete or legacy input.
    """

    if not isinstance(obj, dict):
        raise CliError(f"INVALID_PARTY_{label.upper()}")
    normalized: Dict[str, Any] = {}
    for key in _PROJECTION_KEYS:
        if key in obj:
            normalized[key] = obj[key]
    for key in _IDENTITY_KEYS:
        value = obj.get(key)
        if isinstance(value, str) and value.strip():
            normalized[key] = value.strip()
    for key, value in _birth_fields_from_payload(obj).items():
        if key in _BIRTH_KEYS:
            normalized[key] = value
    return normalized


def _birth_fields_from_payload(payload: Mapping[str, Any]) -> Dict[str, str]:
    birth: Dict[str, str] = {}
    raw_birth = payload.get("birth") or {}
    if isinstance(raw_birth, Mapping):
        birthdate = raw_birth.get("date") or raw_birth.get("birthdate")
        birthtime = raw_birth.get("time") or raw_birth.get("birthtime")
        tz = raw_birth.get("timezone") or raw_birth.get("tz")
        location = raw_birth.get("location") or raw_birth.get("place")
        if isinstance(birthdate, str) and birthdate.strip():
            birth["birthdate"] = birthdate.strip()
        if isinstance(birthtime, str) and birthtime.strip():
            birth["birthtime"] = birthtime.strip()
        if isinstance(location, str) and location.strip():
            birth["location"] = location.strip()
        if isinstance(tz, str) and tz.strip():
            birth["tz"] = tz.strip()
    for key in ("birthdate", "birthtime", "location", "tz"):
        val = payload.get(key)
        if isinstance(val, str) and val.strip():
            birth.setdefault(key, val.strip())
    return birth


def _resolve_party(
    payload: Mapping[str, Any] | str,
    *,
    source_policy: str,
    local_lookup=None,
) -> ResolvedCompatChart:
    return resolve_compat_chart(
        payload,
        source_policy=source_policy,
        env=_resolver_env(),
        local_lookup=local_lookup,
    )


def _person_and_chart_from_payload(payload: Mapping[str, Any], *, uid_hint: str | None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Bind a stored payload to its trusted row identity (``uid_hint``) and return ``(person, chart)``."""

    party: Dict[str, Any] = dict(payload)
    if uid_hint:
        party["user_id"] = uid_hint
    resolved = _resolve_party(party, source_policy="local")
    return {"person_uid": resolved.canonical_person_id}, dict(resolved.mapped_chart)


def _party_from_normalized(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Return ``(person, complete_chart)`` for one normalized file party without I/O."""

    resolved = _resolve_party(payload, source_policy="local")
    return {"person_uid": resolved.canonical_person_id}, dict(resolved.mapped_chart)


def _fetch_db_bodygraph(user_id: str, db_access: DBAccess | None = None) -> Tuple[MappedBodyGraphRow, str]:
    """Read-only current-row lookup for an engine user key; returns the bound row and canonical UUID."""

    normalized = resolve_db_user_id(user_id)
    canonical = canonical_uuid(normalized)
    if canonical is None:
        raise CliError("INVALID_DB_USER")
    if os.environ.get("HDE_FORCE_DB_UNAVAILABLE") == "1":
        raise CliError("DB_QUERY_FAILED")
    try:
        db = db_access or DBAccess.for_current_env()
    except AdapterError as exc:
        raise CliError("DB_QUERY_FAILED") from exc
    try:
        row = read_current_mapped_bodygraph(db, canonical)
    except MappedCacheError as exc:
        if exc.code == "DB_QUERY_FAILED":
            raise CliError("DB_QUERY_FAILED") from exc
        raise CliError("INVALID_BODYGRAPH_PAYLOAD") from exc
    except BodyGraphProjectionError as exc:
        raise projection_refusal(exc) from None
    if row is None:
        raise CliError("BODYGRAPH_NOT_FOUND")
    return row, canonical


def _resolve_db_party(user_id: str) -> ResolvedCompatChart:
    row, canonical = _fetch_db_bodygraph(user_id)
    return _resolve_party(
        {"user_id": user_id},
        source_policy="local",
        local_lookup=lambda key: row if key == canonical else None,
    )


def _vendor_inputs_from_args(args: argparse.Namespace, prefix: str) -> Dict[str, str]:
    """Return the complete birth tuple for one party (input class 3); identity is never derived here."""

    birthdate = getattr(args, f"birthdate_{prefix}", None)
    birthtime = getattr(args, f"birthtime_{prefix}", None)
    location = getattr(args, f"location_{prefix}", None)
    missing = [name for name, value in (("birthdate", birthdate), ("birthtime", birthtime), ("location", location)) if not (value and value.strip())]
    if missing:
        raise CliError("MISSING_VENDOR_INPUT")
    return {"birthdate": birthdate.strip(), "birthtime": birthtime.strip(), "location": location.strip()}


def _conjunction_party_from_payload(raw: Any, label: str) -> Dict[str, Any]:
    """Normalize one conjunction party: a complete chart, an engine key, or a birth tuple.

    The complete chart and its trusted identity slots pass through unchanged
    for the resolver; a bare ``person_uid``/``user_id`` is a stored-user key;
    a complete birth tuple alone is the no-user route.  Nothing else is accepted.
    """

    if not isinstance(raw, Mapping):
        raise CliError(f"MISSING_CONJUNCTION_{label.upper()}")
    party: Dict[str, Any] = {}
    for key in _PROJECTION_KEYS:
        if key in raw:
            party[key] = raw[key]
    for key in ("person_uid", *_IDENTITY_KEYS):
        value = raw.get(key)
        if isinstance(value, str) and value.strip():
            party[key] = value.strip()
    birth = {key: value for key, value in _birth_fields_from_payload(raw).items() if key in _BIRTH_KEYS}
    party.update(birth)
    has_identity = any(key in party for key in ("person_uid", *_IDENTITY_KEYS))
    if "bodygraph" not in party and not has_identity and len(birth) != len(_BIRTH_KEYS):
        raise CliError(f"MISSING_CONJUNCTION_{label.upper()}")
    return party


def _engine_identity() -> tuple[str, str, str]:
    meta = identity_meta()
    return meta["engine_tag"], meta["release_id"], meta["invocation_tag"]


def _viewer_weights() -> Dict[str, int]:
    return {cat: 50 for cat in CATEGORIES_ORDER_V1}


def _admin_bodygraph(party: EvaluationParty) -> Dict[str, Any]:
    """Complete normalized projection with the verified canonical identity."""

    return dict(party.projection)


def _composite_bodygraph(lo: EvaluationParty, hi: EvaluationParty, result: Mapping[str, Any]) -> Dict[str, Any]:
    composite: Dict[str, Any] = {
        "left_person_uid": lo.canonical_person_id,
        "right_person_uid": hi.canonical_person_id,
        "eligible": not is_ineligible_carrier(result),
    }
    if composite["eligible"]:
        composite.update(
            {
                "pair_key": result["pair_key"],
                "config_id": result["config_id"],
                "release_id": result["release_id"],
                "left_chart_fingerprint": lo.chart_fingerprint,
                "right_chart_fingerprint": hi.chart_fingerprint,
            }
        )
    return composite


def _compat_proof(result: Mapping[str, Any]) -> Dict[str, Any]:
    """Admin proof derived only from the validated complete result."""

    if is_ineligible_carrier(result):
        return {"eligible": False, "categories": [], "signals": []}
    return {
        "schema": result["schema"],
        "config_id": result["config_id"],
        "release_id": result["release_id"],
        "pair_key": result["pair_key"],
        "signals": [dict(row) for row in result["signals"]],
        "categories": [dict(row) for row in result["categories"]],
        "thresholds": {
            "edges": [
                THRESHOLDS_V1["cool_max"],
                THRESHOLDS_V1["open_max"],
                THRESHOLDS_V1["warm_max"],
                100,
            ],
            "rounding": "round_half_up",
            "clamp": "0..100",
        },
    }


def _case_name(args: argparse.Namespace) -> str:
    if getattr(args, "pair_file", None):
        stem = Path(args.pair_file).stem
        return stem or "pair"
    if getattr(args, "a_file", None) and getattr(args, "b_file", None):
        left = Path(args.a_file).stem or "a"
        right = Path(args.b_file).stem or "b"
        return f"{left}-{right}"
    return "pair"


def _dump_reader_bytes(path: str, payload: bytes) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)


def _emit_stdout_bytes(payload: bytes) -> None:
    if not payload.endswith(b"\n"):
        raise CliError("STDOUT_MISSING_LF")
    if b"\r\n" in payload:
        raise CliError("STDOUT_CRLF")
    sys.stdout.buffer.write(payload)


def _emit_admin_dumps(
    args: argparse.Namespace,
    case_name: str,
    lo: EvaluationParty,
    hi: EvaluationParty,
    result: Mapping[str, Any],
) -> None:
    if not getattr(args, "dump_admin_dir", None):
        return
    admin_dir = Path(args.dump_admin_dir)
    canon_dump(admin_dir / f"{case_name}.left.bodygraph.json", _admin_bodygraph(lo))
    canon_dump(admin_dir / f"{case_name}.right.bodygraph.json", _admin_bodygraph(hi))
    canon_dump(admin_dir / f"{case_name}.composite.bodygraph.json", _composite_bodygraph(lo, hi, result))
    canon_dump(admin_dir / f"{case_name}.compat.proof.json", _compat_proof(result))


def aux_preview(args: argparse.Namespace) -> int:
    pack = get_pack()

    def _resolve_from_pair_file() -> Tuple[str, str, str, str, Dict[str, Any]]:
        # The pair file is the canonical ``magic10_compat_result.v1`` document
        # written by ``showcompat`` (or a conjunction payload carrying one).
        raw = _read_file(args.pair_file)
        data = _parse_input(raw)
        compat: Any = data
        if isinstance(data.get("conjunction"), Mapping):
            compat = data["conjunction"].get("compat")
        if not isinstance(compat, Mapping):
            raise CliError("INVALID_COMPAT_INPUT")
        categories = [row for row in (compat.get("categories") or []) if isinstance(row, Mapping)]
        if not categories:
            raise CliError("MISSING_COMPAT_CATEGORY")
        category = args.category
        if not isinstance(category, str):
            category = categories[0].get("category_id")
        band = next((row.get("band") for row in categories if row.get("category_id") == category), None)
        if not isinstance(category, str) or not isinstance(band, str):
            raise CliError("MISSING_COMPAT_CATEGORY")
        perspective = args.perspective or "shared"
        release_id = compat.get("release_id") or identity_meta()["release_id"]
        return category, band, perspective, release_id, data

    def _resolve_inputs() -> Tuple[str, str, str, str, Dict[str, Any] | None]:
        if args.pair_file:
            return _resolve_from_pair_file()
        if not (args.category and args.band and args.perspective):
            raise CliError("MISSING_AUX_INPUT")
        release_id = identity_meta()["release_id"]
        return args.category, args.band, args.perspective, release_id, None

    category, band, perspective, release_id, data = _resolve_inputs()
    emission = emit_public_aux(
        category=category,
        band=band,
        perspective=perspective,
        viewer_top=None,
        flags=None,
        families_fired=(),
        release_id=release_id,
        pack_sha=pack.pack_sha,
    )

    emit_text = args.show_narrative or not args.pair_file
    if emit_text and not emission.suppressed:
        sys.stdout.buffer.write(emission.body)

    if getattr(args, "admin_out", None):
        sidecar = {
            "composition_id": emission.composition_id,
            "key": emission.key,
            "pack_sha": emission.pack_sha,
            "release_id": release_id,
        }
        if isinstance(data, Mapping) and isinstance(data.get("conjunction"), Mapping):
            conjunction = data["conjunction"]
            left = conjunction.get("left") if isinstance(conjunction.get("left"), Mapping) else {}
            right = conjunction.get("right") if isinstance(conjunction.get("right"), Mapping) else {}
            sidecar["pair"] = {
                "a_person_uid": left.get("person_uid"),
                "b_person_uid": right.get("person_uid"),
            }
        canon_dump(args.admin_out, sidecar)
    return 0


def showcompat(_: argparse.Namespace) -> int:
    viewer_prefs = _load_viewer_prefs(getattr(_, "viewer_prefs_file", None))
    engine_tag, release_id, invocation_tag = _engine_identity()

    def _party_from_user_args(prefix: str) -> Dict[str, str] | None:
        user = getattr(_, f"user_{prefix}", None)
        if not isinstance(user, str) or not user.strip():
            return None
        party: Dict[str, str] = {"user_id": user.strip()}
        birthdate = getattr(_, f"birthdate_{prefix}", None)
        birthtime = getattr(_, f"birthtime_{prefix}", None)
        location = getattr(_, f"location_{prefix}", None)
        if isinstance(birthdate, str) and birthdate.strip():
            party["birthdate"] = birthdate.strip()
        if isinstance(birthtime, str) and birthtime.strip():
            party["birthtime"] = birthtime.strip()
        if isinstance(location, str) and location.strip():
            party["location"] = location.strip()
        return party

    def _conjunction_from_files_or_stdin() -> Tuple[Dict[str, str], Dict[str, str]]:
        if _.pair_file:
            if _.a_file or _.b_file:
                raise CliError("CONFLICTING_FILE_ARGS")
            raw = _read_file(_.pair_file)
            data = _parse_input(raw)
            left = _conjunction_party_from_payload(data.get("left"), "left")
            right = _conjunction_party_from_payload(data.get("right"), "right")
            return left, right
        if _.a_file or _.b_file:
            if not (_.a_file and _.b_file):
                raise CliError("MISSING_PARTY_FILE")
            left = _conjunction_party_from_payload(_load_party_file(_.a_file, "left"), "left")
            right = _conjunction_party_from_payload(_load_party_file(_.b_file, "right"), "right")
            return left, right
        raw = sys.stdin.read()
        data = _parse_input(raw)
        left = _conjunction_party_from_payload(data.get("left"), "left")
        right = _conjunction_party_from_payload(data.get("right"), "right")
        return left, right

    def _conjunction_inputs() -> Tuple[Dict[str, str], Dict[str, str]]:
        source = getattr(_, "source", None)
        left_from_args = _party_from_user_args("a")
        right_from_args = _party_from_user_args("b")
        if source in ("db", "vendor"):
            if left_from_args is None or right_from_args is None:
                raise CliError("MISSING_DB_USER")
            return left_from_args, right_from_args
        if source == "auto":
            if left_from_args is not None and right_from_args is not None:
                return left_from_args, right_from_args
            raise CliError("AUTO_SOURCE_UNRESOLVED")
        if source:
            raise CliError("UNSUPPORTED_SOURCE")
        if left_from_args is not None or right_from_args is not None:
            if left_from_args is None or right_from_args is None:
                raise CliError("MISSING_DB_USER")
            if _.pair_file or _.a_file or _.b_file:
                raise CliError("CONFLICTING_FILE_ARGS")
            return left_from_args, right_from_args
        return _conjunction_from_files_or_stdin()

    def _lookup_local_conjunction(user_id: str) -> MappedBodyGraphRow | None:
        try:
            row, _canonical = _fetch_db_bodygraph(user_id)
            return row
        except CliError as exc:
            if exc.code == "BODYGRAPH_NOT_FOUND":
                return None
            raise

    def _load_from_source() -> Tuple[ResolvedCompatChart, ResolvedCompatChart]:
        source = getattr(_, "source", None)
        if not source:
            return _load_from_files_or_stdin()
        if _.pair_file or _.a_file or _.b_file:
            raise CliError("CONFLICTING_FILE_ARGS")
        if source == "db":
            if not (_.user_a and _.user_b):
                raise CliError("MISSING_DB_USER")
            return _resolve_db_party(_.user_a), _resolve_db_party(_.user_b)
        if source == "vendor":
            # PF05 §4.1.2: vendor only, birth tuple explicit, rails decide inside the resolver.
            left_birth = _vendor_inputs_from_args(_, "a")
            right_birth = _vendor_inputs_from_args(_, "b")
            return (
                _resolve_party(left_birth, source_policy="vendor"),
                _resolve_party(right_birth, source_policy="vendor"),
            )
        if source == "auto":
            # PF05 §4.1.2: auto is DB-only; the birth-based vendor fallback is prohibited.
            if _.user_a and _.user_b:
                return _resolve_db_party(_.user_a), _resolve_db_party(_.user_b)
            raise CliError("AUTO_SOURCE_UNRESOLVED")
        raise CliError("UNSUPPORTED_SOURCE")

    def _load_from_files_or_stdin() -> Tuple[ResolvedCompatChart, ResolvedCompatChart]:
        left_payload: Dict[str, Any]
        right_payload: Dict[str, Any]
        if _.pair_file:
            if _.a_file or _.b_file:
                raise CliError("CONFLICTING_FILE_ARGS")
            raw = _read_file(_.pair_file)
            data = _parse_input(raw)
            left_payload = _normalize_party(data.get("left"), "left")
            right_payload = _normalize_party(data.get("right"), "right")
        elif _.a_file or _.b_file:
            if not (_.a_file and _.b_file):
                raise CliError("MISSING_PARTY_FILE")
            left_payload = _normalize_party(_load_party_file(_.a_file, "left"), "left")
            right_payload = _normalize_party(_load_party_file(_.b_file, "right"), "right")
        else:
            raw = sys.stdin.read()
            data = _parse_input(raw)
            left_payload = _normalize_party(data.get("left"), "left")
            right_payload = _normalize_party(data.get("right"), "right")
        # File and stdin modes perform no DB or vendor access (PF05 §4.1.2 B/C).
        return (
            _resolve_party(left_payload, source_policy="local"),
            _resolve_party(right_payload, source_policy="local"),
        )

    if getattr(_, "conjunction", False):
        if getattr(_, "dump_reader", None) or getattr(_, "dump_admin_dir", None):
            raise CliError("CONJUNCTION_DUMPS_UNSUPPORTED")
        left, right = _conjunction_inputs()
        source = getattr(_, "source", None)
        conjunction_payload = conjunction_public_resolved(
            left,
            right,
            env=_resolver_env(),
            local_lookup=_lookup_local_conjunction,
            source_policy="local" if source in ("db", "auto") else "vendor",
        )
        _emit_stdout_bytes(emitter.emit_public(conjunction_payload))
        return 0

    left_resolved, right_resolved = _load_from_source()
    a_party = evaluation_party(left_resolved)
    b_party = evaluation_party(right_resolved)
    result = evaluate_pair(a_party, b_party)
    lo, hi = orient(a_party, b_party)
    eligible = not is_ineligible_carrier(result)
    # Eligible pairs carry the admitted bundle's release identity; the vacuous
    # self-pair emits the runtime's manifest-derived identity (no bundle is read).
    reader_bytes, _reader_envelope = emit_reader_public_envelope(
        None,
        None,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=result["release_id"] if eligible else release_id,
        eligible=eligible,
        harmony_band=harmony_band(result) if eligible else None,
    )

    if getattr(_, "dump_reader", None):
        _dump_reader_bytes(_.dump_reader, reader_bytes)

    _emit_admin_dumps(_, _case_name(_), lo, hi, result)

    # PF05 §4.1.3: stdout is exactly the canonical ``magic10_compat_result.v1``
    # document (or the PF01 §4.7 carrier for a valid self-pair) plus one LF.
    _emit_stdout_bytes(emitter.emit_public(result))
    return 0


def _ensure_dev_admin_env() -> None:
    app_env = (os.environ.get("APP_ENV") or "").lower()
    if app_env not in ("dev", "test", "local"):
        raise CliError("DEV_ADMIN_ONLY")


def _normalize_categories(raw: Any) -> Sequence[str] | None:
    if raw is None:
        return None
    if isinstance(raw, (str, bytes)) or not isinstance(raw, Iterable):
        raise CliError("INVALID_CANDIDATE_CATEGORIES")
    normalized: list[str] = []
    for item in raw:
        if not isinstance(item, str) or not item.strip():
            raise CliError("INVALID_CANDIDATE_CATEGORIES")
        normalized.append(item.strip())
    return tuple(normalized)


def _candidate_from_payload(raw: Mapping[str, Any]) -> CandidateFeatures:
    person_uid = raw.get("person_uid") or raw.get("id")
    weight = raw.get("weight")
    compat_score = raw.get("compat_score")
    band = raw.get("band")
    diversity_key = raw.get("diversity_key")
    is_recent = bool(raw.get("is_recent", False))
    categories = raw.get("categories")

    if not isinstance(person_uid, str) or not person_uid.strip():
        raise CliError("INVALID_CANDIDATE_ID")
    if not isinstance(weight, (int, float)):
        raise CliError("INVALID_CANDIDATE_WEIGHT")
    if not isinstance(compat_score, int):
        raise CliError("INVALID_COMPAT_SCORE")
    if band is not None and not isinstance(band, str):
        raise CliError("INVALID_CANDIDATE_BAND")
    if diversity_key is not None and not isinstance(diversity_key, str):
        raise CliError("INVALID_DIVERSITY_KEY")

    return CandidateFeatures(
        person_uid=person_uid.strip(),
        weight=float(weight),
        compat_score=int(compat_score),
        band=band.strip() if isinstance(band, str) and band.strip() else None,
        diversity_key=diversity_key.strip() if isinstance(diversity_key, str) and diversity_key.strip() else None,
        is_recent=is_recent,
        categories=_normalize_categories(categories),
    )


def _load_candidates_from_path(path: str) -> list[CandidateFeatures]:
    raw = _read_file(path)
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CliError("INVALID_CANDIDATES_JSON") from exc

    if isinstance(payload, Mapping):
        candidates_raw = payload.get("candidates")
    else:
        candidates_raw = payload

    if not isinstance(candidates_raw, list):
        raise CliError("INVALID_CANDIDATES_PAYLOAD")

    candidates: list[CandidateFeatures] = []
    for item in candidates_raw:
        if not isinstance(item, Mapping):
            raise CliError("INVALID_CANDIDATE_ENTRY")
        candidates.append(_candidate_from_payload(item))
    return candidates


def _emit_sampler_output(viewer_id: str, seed: str | None, ranked) -> None:
    payload = {
        "viewer_id": viewer_id,
        # Seed is echoed only for now; future phases may use this for tie-breaking hooks.
        "seed": seed if seed is not None else None,
        "candidates": [
            {
                "person_uid": cand.person_uid,
                "score": cand.score,
                "weight": cand.weight,
                "band": cand.band,
                "rank": cand.rank,
                "diversity_key": cand.diversity_key,
                "is_recent": cand.is_recent,
            }
            for cand in ranked.candidates
        ],
    }
    sys.stdout.buffer.write(sercanon(payload))


def dev_sampler_run(args: argparse.Namespace) -> int:
    _ensure_dev_admin_env()
    viewer_id = args.viewer.strip()
    viewer = ViewerProfile(person_uid=viewer_id)
    candidates = _load_candidates_from_path(args.candidates_file)
    ranked = sample_and_rank(viewer, candidates)
    seed = args.seed if args.seed is not None else None
    _emit_sampler_output(viewer.person_uid, seed, ranked)
    return 0


def _read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise CliError("FILE_NOT_FOUND") from exc
    except OSError as exc:
        raise CliError("FILE_READ_ERROR") from exc


def _load_party_file(path: str, label: str) -> Dict[str, Any]:
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise CliError(f"FILE_NOT_FOUND_{label.upper()}") from exc
    except OSError as exc:
        raise CliError(f"FILE_READ_ERROR_{label.upper()}") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CliError(f"INVALID_JSON_{label.upper()}") from exc
    if not isinstance(data, dict):
        raise CliError(f"INVALID_JSON_{label.upper()}")
    return data
