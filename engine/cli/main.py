from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable

from engine.bodygraph import resolve_bodygraph
from engine.compat import ts_v0
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import compat_public, band_for
from engine.compat.ordering import pair_key
from engine.compat.thresholds import THRESHOLDS_V1
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
    show.set_defaults(handler=showcompat)

    aux = sub.add_parser(
        "aux-preview",
        help="Preview Aux narrative text for a public tuple",
        allow_abbrev=False,
    )
    aux.add_argument("--category", required=True, help="Narrative category slug")
    aux.add_argument("--band", required=True, choices=AUX_BANDS)
    aux.add_argument("--perspective", required=True, choices=AUX_PERSPECTIVES)
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
    return parser


def _resolver_env() -> Dict[str, str | None]:
    return {name: os.environ.get(name) for name in ("SAFE_MODE", "ALLOW_NETWORK", "APP_ENV")}


def bg_resolve(args: argparse.Namespace) -> int:
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
        return int(exc.code or 0)
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
    birth = {k: payload[k] for k in birth_keys if k in payload}
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
    release_id = os.environ.get("RELEASE_ID", "0" * 64)
    emission = emit_public_aux(
        category=args.category,
        band=args.band,
        perspective=args.perspective,
        viewer_top=None,
        flags=None,
        families_fired=(),
        release_id=release_id,
        pack_sha=pack.pack_sha,
    )

    if not emission.suppressed:
        sys.stdout.buffer.write(emission.body)
    return 0


def showcompat(_: argparse.Namespace) -> int:
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

    a_chart = _chart_for(left_payload["person_uid"])
    b_chart = _chart_for(right_payload["person_uid"])
    a_ts = ts_v0.extract_ts(a_chart)
    b_ts = ts_v0.extract_ts(b_chart)
    features = ts_v0.compute_features(a_ts, b_ts)
    weights = _viewer_weights()
    engine_tag, release_id, invocation_tag = _engine_identity()
    compat_full = compat_public(
        {"person_uid": left_payload["person_uid"]},
        {"person_uid": right_payload["person_uid"]},
        CATEGORIES_ORDER_V1[0],
        weights,
        engine_tag=engine_tag,
        release_id=release_id,
        invocation_tag=invocation_tag,
    )
    public_bytes, _ = emit_reader_public_envelope(
        a_chart,
        b_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
    )

    if getattr(_, "dump_reader", None):
        _dump_reader_bytes(_.dump_reader, public_bytes)

    case_name = _case_name(_)
    _emit_admin_dumps(_, case_name, left_payload, right_payload, a_chart, b_chart, compat_full.get("categories", []), features, weights)

    sys.stdout.buffer.write(public_bytes)
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
