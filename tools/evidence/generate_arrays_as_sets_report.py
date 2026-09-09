#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import stat
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.mech.helpers import canonicalize_declared_set  # noqa: E402
from engine.config.registry_loader import (  # noqa: E402
    RegistryConfigError,
    validate_channel_gates,
)
from engine.runtime.determinism_env import ensure_determinism_env  # noqa: E402

REPORT_PATH = ROOT / "artifacts" / "canonical" / "arrays_as_sets_report.log"
CHANNELS_PATH = ROOT / "catalog" / "channels_v1.json"


def _load_channels(path: Path) -> list[dict[str, object]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    channels = raw.get("channels")
    if not isinstance(channels, list):
        raise SystemExit("channels_v1.json missing channels list")
    return channels


def _require_canonical_set(
    values: object, *, identity: str | None, path: str
) -> None:
    if not isinstance(values, list):
        raise SystemExit(f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:{path}")
    try:
        normalized = canonicalize_declared_set(values, identity=identity)
    except ValueError as exc:
        raise SystemExit(f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:{path}") from exc
    if values != normalized:
        raise SystemExit(f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:{path}")


def _validate_source_sets(channels: list[dict[str, object]]) -> None:
    _require_canonical_set(channels, identity="id", path="$.channels")
    for index, entry in enumerate(channels):
        if not isinstance(entry, dict):
            raise SystemExit(
                f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:$.channels[{index}]"
            )
        _require_numeric_gates(entry.get("gates"), entry.get("id"), index)
        for field in ("centers", "domains", "flags"):
            _require_canonical_set(
                entry.get(field),
                identity=None,
                path=f"$.channels[{index}].{field}",
            )


def _require_numeric_gates(values: object, channel_id: object, index: int) -> list[int]:
    """Validate the Channel endpoint tuple; other scalar sets remain ASCII."""
    try:
        return list(validate_channel_gates(values, channel_id=channel_id))
    except (RegistryConfigError, ValueError, TypeError) as exc:
        raise SystemExit(
            f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:$.channels[{index}].gates"
        ) from exc


def _select_case(channels: list[dict[str, object]], field: str) -> tuple[dict[str, object], bool]:
    fallback_entry: dict[str, object] | None = None
    fallback_raw: list[object] | None = None
    fallback_normalized: list[object] | None = None

    for index, entry in enumerate(channels):
        if not isinstance(entry, dict):
            raise SystemExit(
                f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:$.channels[{index}]"
            )
        values = entry.get(field)
        path = f"$.channels[{index}].{field}"
        if not isinstance(values, list):
            raise SystemExit(f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:{path}")
        if not values:
            continue
        channel_id = entry.get("id")
        if not isinstance(channel_id, str):
            raise SystemExit(
                f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:$.channels[{index}]"
            )
        raw = list(values)
        try:
            normalized = (
                _require_numeric_gates(raw, channel_id, index)
                if field == "gates"
                else canonicalize_declared_set(raw, identity=None)
            )
        except ValueError as exc:
            raise SystemExit(f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:{path}") from exc
        if normalized != raw:
            raise SystemExit(f"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:{path}")
        if fallback_entry is None:
            fallback_entry = entry
            fallback_raw = raw
            fallback_normalized = normalized

    if fallback_entry is None or fallback_raw is None or fallback_normalized is None:
        raise SystemExit(f"no {field} array found in channels_v1.json")

    return (
        {
            "channel_id": str(fallback_entry["id"]),
            "field": field,
            "raw": fallback_raw,
            "normalized": fallback_normalized,
        },
        True,
    )


def _render_case(case: dict[str, object], *, fallback: bool) -> list[str]:
    channel_id = case["channel_id"]
    field = case["field"]
    raw = case["raw"]
    normalized = case["normalized"]
    path = f"catalog/channels_v1.json:channels[id={channel_id}].{field}"
    lines = [
        f"case: channel_id={channel_id} field={field}",
        f"path: {path}",
        (
            "validator: engine.config.registry_loader.validate_channel_gates "
            "(strict numeric ascending endpoints)"
            if field == "gates"
            else "normalizer: engine.mech.helpers.canonicalize_declared_set(identity=None)"
        ),
        f"raw: {json.dumps(raw, ensure_ascii=False)}",
        f"normalized: {json.dumps(normalized, ensure_ascii=False)}",
    ]
    if fallback:
        lines.append("note: raw == normalized (already canonical)")
    lines.append("")
    return lines


def _render_channel_roster_case(channels: list[dict[str, object]]) -> list[str]:
    try:
        normalized = canonicalize_declared_set(channels, identity="id")
    except ValueError as exc:
        raise SystemExit("ARRAYS_AS_SETS_SOURCE_NONCANONICAL:$.channels") from exc
    if channels != normalized:
        raise SystemExit("ARRAYS_AS_SETS_SOURCE_NONCANONICAL:$.channels")
    raw_ids = [entry.get("id") for entry in channels]
    normalized_ids = [entry.get("id") for entry in normalized]
    lines = [
        "case: field=channels identity=id",
        "path: catalog/channels_v1.json:channels",
        "normalizer: engine.mech.helpers.canonicalize_declared_set(identity=id)",
        f"raw identities: {json.dumps(raw_ids, ensure_ascii=False)}",
        f"normalized identities: {json.dumps(normalized_ids, ensure_ascii=False)}",
    ]
    lines.append("note: raw == normalized (already canonical)")
    lines.append("")
    return lines


def build_report() -> str:
    channels = _load_channels(CHANNELS_PATH)
    _validate_source_sets(channels)
    lines = [
        "arrays-as-sets report v1",
        "surface: registry.catalog.channels_v1",
        f"source: {CHANNELS_PATH.relative_to(ROOT)}",
        "",
    ]
    lines.extend(_render_channel_roster_case(channels))
    for field in ("centers", "domains", "flags", "gates"):
        case, fallback = _select_case(channels, field)
        lines.extend(_render_case(case, fallback=fallback))
    return "\n".join(lines).rstrip("\n") + "\n"


def write_report(*, check: bool = False) -> Path:
    ensure_determinism_env()
    # Refuse aliasing even when expected bytes already match. The coordinated
    # owner captures this primary's preimage before invoking this writer.
    target = Path(os.path.abspath(REPORT_PATH))
    for path in (target, *target.parents):
        if path.is_symlink():
            raise SystemExit("ARRAYS_AS_SETS_REPORT_UNSAFE_TARGET")
        if path != target and path.exists() and not path.is_dir():
            raise SystemExit("ARRAYS_AS_SETS_REPORT_UNSAFE_TARGET")
    if target.exists() and not stat.S_ISREG(target.stat().st_mode):
        raise SystemExit("ARRAYS_AS_SETS_REPORT_UNSAFE_TARGET")
    expected = build_report().encode("utf-8")
    if check:
        if not REPORT_PATH.is_file() or REPORT_PATH.read_bytes() != expected:
            raise SystemExit("ARRAYS_AS_SETS_REPORT_STALE")
        return REPORT_PATH
    if REPORT_PATH.is_file() and REPORT_PATH.read_bytes() == expected:
        return REPORT_PATH
    from tools.evidence import update_evidence_index
    update_evidence_index._publish_staged({REPORT_PATH: expected})
    return REPORT_PATH


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate arrays-as-sets report")
    parser.add_argument("--check", action="store_true", help="fail if the report is missing or stale")
    args = parser.parse_args(argv)
    write_report(check=args.check)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(_main())
