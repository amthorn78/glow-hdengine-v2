#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.mech.helpers import canonicalize_array  # noqa: E402
from engine.runtime.determinism_env import ensure_determinism_env  # noqa: E402

REPORT_PATH = ROOT / "artifacts" / "canonical" / "arrays_as_sets_report.log"
CHANNELS_PATH = ROOT / "catalog" / "channels_v1.json"


def _load_channels(path: Path) -> list[dict[str, object]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    channels = raw.get("channels")
    if not isinstance(channels, list):
        raise SystemExit("channels_v1.json missing channels list")
    return channels


def _normalize_strings(values: Iterable[object]) -> list[str]:
    return [str(value) for value in values]


def _select_case(channels: list[dict[str, object]], field: str) -> tuple[dict[str, object], bool]:
    fallback_entry: dict[str, object] | None = None
    fallback_raw: list[str] | None = None
    fallback_normalized: list[str] | None = None

    for entry in channels:
        values = entry.get(field)
        if not isinstance(values, list) or not values:
            continue
        channel_id = entry.get("id")
        if not isinstance(channel_id, str):
            continue
        raw = _normalize_strings(values)
        normalized = canonicalize_array(raw)
        if normalized != raw:
            return (
                {
                    "channel_id": channel_id,
                    "field": field,
                    "raw": raw,
                    "normalized": normalized,
                },
                False,
            )
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
        "normalizer: engine.mech.helpers.canonicalize_array",
        f"raw: {json.dumps(raw, ensure_ascii=False)}",
        f"normalized: {json.dumps(normalized, ensure_ascii=False)}",
    ]
    if fallback:
        lines.append("note: raw == normalized (already canonical)")
    lines.append("")
    return lines


def build_report() -> str:
    channels = _load_channels(CHANNELS_PATH)
    centers_case, centers_fallback = _select_case(channels, "centers")
    domains_case, domains_fallback = _select_case(channels, "domains")
    lines = [
        "arrays-as-sets report v1",
        "surface: registry.catalog.channels_v1",
        f"source: {CHANNELS_PATH.relative_to(ROOT)}",
        "",
    ]
    lines.extend(_render_case(centers_case, fallback=centers_fallback))
    lines.extend(_render_case(domains_case, fallback=domains_fallback))
    return "\n".join(lines).rstrip("\n") + "\n"


def write_report(*, check: bool = False) -> Path:
    ensure_determinism_env()
    expected = build_report().encode("utf-8")
    if check:
        if not REPORT_PATH.is_file() or REPORT_PATH.read_bytes() != expected:
            raise SystemExit("ARRAYS_AS_SETS_REPORT_STALE")
        return REPORT_PATH
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_bytes(expected)
    return REPORT_PATH


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate arrays-as-sets report")
    parser.add_argument("--check", action="store_true", help="fail if the report is missing or stale")
    args = parser.parse_args(argv)
    write_report(check=args.check)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(_main())
