from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Sequence, Tuple

from engine.bodygraph import resolve_bodygraph
from engine.bodygraph.ingest import (
    VendorInputs,
    ingest_vendor_bodygraph,
    resolve_db_user_id,
)
from engine.compat import ts_v0
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import compat_public, band_for
from engine.compat.compute import conjunction_public_resolved
from engine.compat.ordering import normalize_pair, pair_key
from engine.compat.thresholds import THRESHOLDS_V1
from engine.db import DBAccess
from engine.db.errors import AdapterError
from engine.constants import (
    COMP_MAX,
    EM_MAX,
    MIND_THROAT_MAX,
    MOTOR_THROAT_MAX,
    THROAT_EM_MAX,
    CENTER_MAX,
)
from engine.presenter import emitter
from engine.runtime import emit_reader_public_envelope
from engine.serializer.canon import sercanon
from engine.narratives import emit_public_aux, get_pack
from engine.narratives.constants import BANDS as AUX_BANDS, PERSPECTIVES as AUX_PERSPECTIVES
from engine.validation.viewer_prefs import validate_viewer_prefs
from engine.bodygraph.vendor_client import VendorError
from engine.sampler.core import CandidateFeatures, ViewerProfile, sample_and_rank

from ._admin_dump import canon_dump

_TYPE_SEQUENCE = (
    "Generator",
    "Manifesting Generator",
    "Projector",
    "Manifestor",
    "Reflector",
)


class CliError(Exception):
    """Typed CLI failure used to map to process exit codes."""

    def __init__(self, code: str, exit_code: int = 64) -> None:
        super().__init__(code)
        self.code = code
        self.exit_code = exit_code


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hdctl",
        description="Glow HD Engine compatibility CLI",
        allow_abbrev=False,
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
        help="Request durability upsert once implemented",
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
    return {name: os.environ.get(name) for name in ("SAFE_MODE", "ALLOW_NETWORK", "APP_ENV")}


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
    return data


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


def _fingerprint(payload: Dict[str, Any]) -> str:
    canon_bytes = sercanon(payload)
    return hashlib.sha256(canon_bytes).hexdigest()


def _derive_uid(fields: Dict[str, Any]) -> str:
    existing = fields.get("person_uid")
    if isinstance(existing, str) and existing.strip() and len(existing.strip()) <= 64:
        return existing.strip()
    base = {k: fields[k] for k in ("birthdate", "birthtime", "location", "tz") if k in fields}
    digest = _fingerprint(base)
    return f"cli-{digest[:32]}"


def _normalize_party(obj: Any, label: str) -> Dict[str, Any]:
    if not isinstance(obj, dict):
        raise CliError(f"INVALID_PARTY_{label.upper()}")
    required = ("birthdate", "birthtime", "location")
    normalized: Dict[str, Any] = {}
    for key in required:
        value = obj.get(key)
        if not isinstance(value, str) or not value.strip():
            raise CliError(f"MISSING_FIELD_{label.upper()}_{key.upper()}")
        normalized[key] = value.strip()
    tz_val = obj.get("tz")
    if isinstance(tz_val, str) and tz_val.strip():
        normalized["tz"] = tz_val.strip()
    if isinstance(obj.get("person_uid"), str):
        normalized["person_uid"] = obj["person_uid"].strip()
    normalized["person_uid"] = _derive_uid(normalized)
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


def _person_and_chart_from_payload(payload: Mapping[str, Any], *, uid_hint: str | None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    birth = _birth_fields_from_payload(payload)
    uid = payload.get("person_uid")
    if not uid and birth:
        uid = _derive_uid(birth)
    if not uid:
        uid = uid_hint or _derive_uid({"person_uid": "fallback"})
    mechanics = payload.get("mechanics") or {}
    mech_type = mechanics.get("type") or payload.get("type")
    if not isinstance(mech_type, str) or not mech_type.strip():
        raise CliError("MISSING_MECHANICS_TYPE")
    chart = {"person_uid": uid, "mechanics": {"type": mech_type.strip()}}
    if birth:
        chart["birth"] = dict(birth)
    person = {"person_uid": uid}
    if birth:
        person["birth"] = dict(birth)
    return person, chart


def _party_from_normalized(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    chart = _chart_for(payload["person_uid"])
    bodygraph = _bodygraph(payload, chart)
    birth = {k: payload[k] for k in ("birthdate", "birthtime", "location", "tz") if k in payload}
    person = {"person_uid": payload["person_uid"]}
    if birth:
        person["birth"] = birth
    return person, bodygraph


def _fetch_db_bodygraph(user_id: str, db_access: DBAccess | None = None) -> Tuple[Mapping[str, Any], str]:
    normalized = resolve_db_user_id(user_id)
    if os.environ.get("HDE_FORCE_DB_UNAVAILABLE") == "1":
        raise CliError("DB_QUERY_FAILED")
    try:
        db = db_access or DBAccess.for_current_env()
        rows = db.query(
            """
            SELECT payload::text
            FROM hde.body_graphs_current
            WHERE user_id = %s
            ORDER BY vendor_version DESC
            LIMIT 1
            """,
            (normalized,),
        )
    except AdapterError as exc:
        raise CliError("DB_QUERY_FAILED") from exc
    if not rows:
        raise CliError("BODYGRAPH_NOT_FOUND")
    try:
        payload = json.loads(rows[0][0])
    except json.JSONDecodeError as exc:
        raise CliError("INVALID_BODYGRAPH_PAYLOAD") from exc
    return payload, normalized


def _vendor_inputs_from_args(args: argparse.Namespace, prefix: str) -> VendorInputs:
    birthdate = getattr(args, f"birthdate_{prefix}", None)
    birthtime = getattr(args, f"birthtime_{prefix}", None)
    location = getattr(args, f"location_{prefix}", None)
    missing = [name for name, value in (("birthdate", birthdate), ("birthtime", birthtime), ("location", location)) if not (value and value.strip())]
    if missing:
        raise CliError("MISSING_VENDOR_INPUT")
    base = {"birthdate": birthdate.strip(), "birthtime": birthtime.strip(), "location": location.strip()}
    user_id = _derive_uid(base)
    return VendorInputs(
        user_id=user_id,
        birthdate=base["birthdate"],
        birthtime=base["birthtime"],
        location=base["location"],
    )


def _conjunction_party_from_payload(raw: Any, label: str) -> Dict[str, str]:
    if not isinstance(raw, Mapping):
        raise CliError(f"MISSING_CONJUNCTION_{label.upper()}")
    party: Dict[str, str] = {}
    person_uid = raw.get("person_uid")
    user_id = raw.get("user_id")
    if isinstance(person_uid, str) and person_uid.strip():
        party["person_uid"] = person_uid.strip()
    elif isinstance(user_id, str) and user_id.strip():
        party["user_id"] = user_id.strip()
    else:
        raise CliError(f"MISSING_CONJUNCTION_{label.upper()}")
    for key, value in _birth_fields_from_payload(raw).items():
        if key in ("birthdate", "birthtime", "location"):
            party[key] = value
    return party


def _chart_for(uid: str) -> Dict[str, Any]:
    digest = hashlib.sha256(uid.encode("utf-8")).digest()[0]
    mech_type = _TYPE_SEQUENCE[digest % len(_TYPE_SEQUENCE)]
    chart = {"person_uid": uid, "mechanics": {"type": mech_type}}
    ts = ts_v0.extract_ts(chart)
    chart["mechanics"]["strategy"] = ts["strategy"]
    return chart


def _engine_identity() -> tuple[str, str, str]:
    engine_tag = os.environ.get("ENGINE_TAG", "hdengine-dev")
    release_id = os.environ.get("RELEASE_ID", "0" * 64)
    invocation_tag = os.environ.get("PRODUCT_INVOCATION_TAG", "INV-LOCAL")
    return engine_tag, release_id, invocation_tag


def _viewer_weights() -> Dict[str, int]:
    return {cat: 50 for cat in CATEGORIES_ORDER_V1}


def _signals(features: Dict[str, Any]) -> list[Dict[str, Any]]:
    return [
        {"name": name, "value": features[name]}
        for name in sorted(features.keys())
    ]


def _per_category_proof(categories: Iterable[Dict[str, Any]], weights: Dict[str, int]) -> Dict[str, Dict[str, Any]]:
    proof: Dict[str, Dict[str, Any]] = {}
    for cat in CATEGORIES_ORDER_V1:
        match = next((c for c in categories if c["id"] == cat), None)
        if match is None:
            continue
        score = int(match.get("score", 0))
        clamped = max(0, min(100, score))
        proof[cat] = {
            "raw": score,
            "normalized": score,
            "clamped": clamped,
            "rounded": clamped,
            "band": match.get("band", "Cool"),
            "proof": [
                {"step": "hash_score", "value": score},
                {"step": "weight", "value": weights.get(cat, 0)},
                {"step": "band_threshold", "value": match.get("band", "Cool")},
            ],
        }
    return proof


def _overall_from(proof: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    if not proof:
        return {"percent": 0, "band": band_for(0)}
    total = sum(item["rounded"] for item in proof.values())
    avg = total / len(proof)
    percent = int(math.floor(avg + 0.5))
    return {"percent": percent, "band": band_for(percent)}


def _bodygraph(payload: Dict[str, Any], chart: Dict[str, Any]) -> Dict[str, Any]:
    birth_keys = ("birthdate", "birthtime", "location", "tz")
    birth_payload = payload.get("birth") if isinstance(payload.get("birth"), Mapping) else {}
    birth = {}
    for key in birth_keys:
        if key in payload:
            birth[key] = payload[key]
        elif key in birth_payload:
            birth[key] = birth_payload[key]
    return {
        "person_uid": payload["person_uid"],
        "mechanics": chart["mechanics"],
        "birth": birth,
    }


def _composite_bodygraph(a: Dict[str, Any], b: Dict[str, Any], features: Dict[str, Any]) -> Dict[str, Any]:
    pk = pair_key({"person_uid": a["person_uid"]}, {"person_uid": b["person_uid"]})
    return {
        "pair_key": pk,
        "left_person_uid": a["person_uid"],
        "right_person_uid": b["person_uid"],
        "features": features,
        "band": ts_v0.band_v0(features),
    }


def _compat_proof(categories: Iterable[Dict[str, Any]], features: Dict[str, Any], weights: Dict[str, int]) -> Dict[str, Any]:
    per_category = _per_category_proof(categories, weights)
    return {
        "constants": {
            "EM_MAX": EM_MAX,
            "THROAT_EM_MAX": THROAT_EM_MAX,
            "CENTER_MAX": CENTER_MAX,
            "MIND_THROAT_MAX": MIND_THROAT_MAX,
            "MOTOR_THROAT_MAX": MOTOR_THROAT_MAX,
            "COMP_MAX": COMP_MAX,
        },
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
        "categories_frozen_order": list(CATEGORIES_ORDER_V1),
        "signals": _signals(features),
        "per_category": per_category,
        "overall": _overall_from(per_category),
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
    left_payload: Dict[str, Any],
    right_payload: Dict[str, Any],
    a_chart: Dict[str, Any],
    b_chart: Dict[str, Any],
    categories: Iterable[Dict[str, Any]],
    features: Dict[str, Any],
    weights: Dict[str, int],
) -> None:
    if not getattr(args, "dump_admin_dir", None):
        return
    admin_dir = Path(args.dump_admin_dir)
    left = _bodygraph(left_payload, a_chart)
    right = _bodygraph(right_payload, b_chart)
    composite = _composite_bodygraph(left, right, features)
    proof = _compat_proof(categories, features, weights)

    canon_dump(admin_dir / f"{case_name}.left.bodygraph.json", left)
    canon_dump(admin_dir / f"{case_name}.right.bodygraph.json", right)
    canon_dump(admin_dir / f"{case_name}.composite.bodygraph.json", composite)
    canon_dump(admin_dir / f"{case_name}.compat.proof.json", proof)


def aux_preview(args: argparse.Namespace) -> int:
    pack = get_pack()

    def _resolve_from_pair_file() -> Tuple[str, str, str, str, Dict[str, Any]]:
        raw = _read_file(args.pair_file)
        data = _parse_input(raw)
        compat = data.get("compat") or {}
        if not isinstance(compat, Mapping):
            raise CliError("INVALID_COMPAT_INPUT")
        categories = compat.get("categories") or []
        if not categories:
            raise CliError("MISSING_COMPAT_CATEGORY")
        viewer_prefs = data.get("viewer_prefs") or {}
        category = viewer_prefs.get("top_category") if isinstance(viewer_prefs, Mapping) else None
        if not isinstance(category, str):
            category = categories[0].get("id")
        band = next((c.get("band") for c in categories if c.get("id") == category), None) or categories[0].get("band")
        if not isinstance(band, str):
            raise CliError("MISSING_COMPAT_CATEGORY")
        perspective = args.perspective or "shared"
        meta = compat.get("meta") or {}
        release_id = meta.get("release_id") or os.environ.get("RELEASE_ID", "0" * 64)
        return category, band, perspective, release_id, data

    def _resolve_inputs() -> Tuple[str, str, str, str, Dict[str, Any] | None]:
        if args.pair_file:
            return _resolve_from_pair_file()
        if not (args.category and args.band and args.perspective):
            raise CliError("MISSING_AUX_INPUT")
        release_id = os.environ.get("RELEASE_ID", "0" * 64)
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
        if isinstance(data, Mapping):
            a = data.get("a") or {}
            b = data.get("b") or {}
            if isinstance(a, Mapping) and isinstance(b, Mapping):
                sidecar["pair"] = {
                    "a_person_uid": a.get("person_uid"),
                    "b_person_uid": b.get("person_uid"),
                }
        canon_dump(args.admin_out, sidecar)
    return 0


def _canonical_pair(
    left_person: Dict[str, Any],
    right_person: Dict[str, Any],
    left_chart: Dict[str, Any],
    right_chart: Dict[str, Any],
) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    ordered_people = list(normalize_pair(left_person, right_person))
    charts = {
        left_person["person_uid"]: left_chart,
        right_person["person_uid"]: right_chart,
    }
    ordered_charts = [charts[p["person_uid"]] for p in ordered_people]
    return ordered_people[0], ordered_people[1], ordered_charts[0], ordered_charts[1]


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

    def _lookup_local_conjunction(user_id: str) -> Mapping[str, Any] | None:
        try:
            payload, _ = _fetch_db_bodygraph(user_id)
            return payload
        except CliError as exc:
            if exc.code == "BODYGRAPH_NOT_FOUND":
                return None
            raise

    def _load_from_source() -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
        source = getattr(_, "source", None)
        if not source:
            return _load_from_files_or_stdin()
        if _.pair_file or _.a_file or _.b_file:
            raise CliError("CONFLICTING_FILE_ARGS")
        if source == "db":
            if not (_.user_a and _.user_b):
                raise CliError("MISSING_DB_USER")
            left_payload, left_uid = _fetch_db_bodygraph(_.user_a)
            right_payload, right_uid = _fetch_db_bodygraph(_.user_b)
            left_person, left_chart = _person_and_chart_from_payload(left_payload, uid_hint=left_uid)
            right_person, right_chart = _person_and_chart_from_payload(right_payload, uid_hint=right_uid)
            return left_person, right_person, left_chart, right_chart
        if source == "vendor":
            left_inputs = _vendor_inputs_from_args(_, "a")
            right_inputs = _vendor_inputs_from_args(_, "b")
            try:
                left_outcome = ingest_vendor_bodygraph(left_inputs, env=_resolver_env(), dry_run=True)
                right_outcome = ingest_vendor_bodygraph(right_inputs, env=_resolver_env(), dry_run=True)
            except VendorError as exc:
                raise CliError(exc.code, exit_code=1) from exc
            left_person, left_chart = _person_and_chart_from_payload(left_outcome.payload, uid_hint=left_inputs.user_id)
            right_person, right_chart = _person_and_chart_from_payload(right_outcome.payload, uid_hint=right_inputs.user_id)
            return left_person, right_person, left_chart, right_chart
        if source == "auto":
            if _.user_a and _.user_b:
                _.source = "db"
                return _load_from_source()
            if _.birthdate_a or _.birthdate_b:
                _.source = "vendor"
                return _load_from_source()
            raise CliError("AUTO_SOURCE_UNRESOLVED")
        raise CliError("UNSUPPORTED_SOURCE")

    def _load_from_files_or_stdin() -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
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
        left_person, left_chart = _party_from_normalized(left_payload)
        right_person, right_chart = _party_from_normalized(right_payload)
        return left_person, right_person, left_chart, right_chart

    if getattr(_, "conjunction", False):
        if getattr(_, "dump_reader", None) or getattr(_, "dump_admin_dir", None):
            raise CliError("CONJUNCTION_DUMPS_UNSUPPORTED")
        left, right = _conjunction_inputs()
        try:
            conjunction_payload = conjunction_public_resolved(
                left,
                right,
                viewer_top=viewer_prefs["top_category"],
                viewer_weights=viewer_prefs["weights"],
                engine_tag=engine_tag,
                release_id=release_id,
                invocation_tag=invocation_tag,
                env=_resolver_env(),
                local_lookup=_lookup_local_conjunction,
            )
        except VendorError as exc:
            raise CliError(exc.code, exit_code=1) from exc
        _emit_stdout_bytes(emitter.emit_public(conjunction_payload))
        return 0

    left_person, right_person, a_chart, b_chart = _load_from_source()
    left_person, right_person, a_chart, b_chart = _canonical_pair(
        left_person, right_person, a_chart, b_chart
    )
    a_ts = ts_v0.extract_ts(a_chart)
    b_ts = ts_v0.extract_ts(b_chart)
    features = ts_v0.compute_features(a_ts, b_ts)
    compat_full = compat_public(
        left_person,
        right_person,
        viewer_prefs["top_category"],
        viewer_prefs["weights"],
        engine_tag=engine_tag,
        release_id=release_id,
        invocation_tag=invocation_tag,
    )
    compat_payload = {
        "a": left_person,
        "b": right_person,
        "viewer_prefs": viewer_prefs,
        "compat": compat_full,
    }
    compat_bytes = emitter.emit_public(compat_payload)

    reader_bytes, reader_envelope = emit_reader_public_envelope(
        a_chart,
        b_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
    )

    if getattr(_, "dump_reader", None):
        _dump_reader_bytes(_.dump_reader, reader_bytes)

    case_name = _case_name(_)
    _emit_admin_dumps(
        _,
        case_name,
        left_person,
        right_person,
        a_chart,
        b_chart,
        compat_full.get("categories", []),
        features,
        viewer_prefs["weights"],
    )

    _emit_stdout_bytes(compat_bytes)
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
