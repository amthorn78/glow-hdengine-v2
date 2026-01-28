#!/usr/bin/env python3
"""Validate that evidence mirror paths resolve to real artifacts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env


def _load_index(path: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            obj = json.loads(raw)
        except Exception as exc:  # noqa: BLE001
            raise SystemExit(f"JSON:{i}:{exc}") from exc
        if isinstance(obj, dict):
            records.append(obj)
    return records


def main() -> int:
    try:
        ensure_determinism_env(apply=True)
    except DeterminismEnvError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    index_path = ROOT / "artifacts" / "evidence_index.jsonl"
    if not index_path.exists():
        print("MISSING:artifacts/evidence_index.jsonl", file=sys.stderr)
        return 1

    ok = True
    root_resolved = ROOT.resolve()
    for i, entry in enumerate(_load_index(index_path), 1):
        path = entry.get("discovered_physical_path")
        if not isinstance(path, str) or not path:
            print(f"PATH_INVALID:{i}:{path!r}", file=sys.stderr)
            ok = False
            continue
        candidate = Path(path)
        if candidate.is_absolute():
            print(f"PATH_ABSOLUTE:{i}:{path}", file=sys.stderr)
            ok = False
            continue
        if ".." in candidate.parts:
            print(f"PATH_TRAVERSAL:{i}:{path}", file=sys.stderr)
            ok = False
            continue
        artifact_path = (ROOT / candidate).resolve()
        try:
            artifact_path.relative_to(root_resolved)
        except ValueError:
            print(f"PATH_OUTSIDE_ROOT:{i}:{path}", file=sys.stderr)
            ok = False
            continue
        if not artifact_path.exists():
            print(f"MISSING:{i}:{path}", file=sys.stderr)
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
