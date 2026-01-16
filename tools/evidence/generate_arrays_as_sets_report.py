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


def _select_case(channels: list[dict[str, object]], field: str) -> dict[str, object]:
    for entry in channels:
        values = entry.get(field)
        if not isinstance(values, list) or not values:
            continue
        raw = _normalize_strings(values)
        normalized = canonicalize_array(raw)
        if normalized != raw:
            channel_id = entry.get("id")
            if not isinstance(channel_id, str):
                continue
            return {
                "channel_id": channel_id,
                "field": field,
                "raw": raw,
                "normalized": normalized,
            }
    raise SystemExit(f"no unsorted {field} array found in channels_v1.json")


def _render_case(case: dict[str, object]) -> list[str]:
    channel_id = case["channel_id"]
    field = case["field"]
    raw = case["raw"]
    normalized = case["normalized"]
    path = f"catalog/channels_v1.json:channels[id={channel_id}].{field}"
    return [
        f"case: channel_id={channel_id} field={field}",
        f"path: {path}",
        "normalizer: engine.mech.helpers.canonicalize_array",
        f"raw: {json.dumps(raw, ensure_ascii=False)}",
        f"normalized: {json.dumps(normalized, ensure_ascii=False)}",
        "",
    ]


def build_report() -> str:
    channels = _load_channels(CHANNELS_PATH)
    centers_case = _select_case(channels, "centers")
    domains_case = _select_case(channels, "domains")
    lines = [
        "arrays-as-sets report v1",
        "surface: registry.catalog.channels_v1",
        f"source: {CHANNELS_PATH.relative_to(ROOT)}",
        "",
    ]
    lines.extend(_render_case(centers_case))
    lines.extend(_render_case(domains_case))
    return "\n".join(lines).rstrip("\n") + "\n"


def write_report() -> Path:
    ensure_determinism_env()
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(build_report(), encoding="utf-8")
    return REPORT_PATH


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate arrays-as-sets report")
    args = parser.parse_args(argv)
    write_report()
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(_main())
