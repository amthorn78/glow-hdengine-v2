"""CLI helper for comparing canonical presenter JSON bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Any

from engine.presenter import emitter

DEFAULT_LOG_PATH = Path("artifacts/presenter/json_canon_compare.log")


class JsonCanonCompareError(Exception):
    """Raised when parity inputs are invalid."""


def _load_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise JsonCanonCompareError(f"missing file: {path}") from exc
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        raise JsonCanonCompareError(f"invalid JSON: {path}") from exc
    return payload


def _canonical_bytes(payload: Any) -> bytes:
    if not isinstance(payload, dict):
        raise JsonCanonCompareError("inputs must be JSON objects")
    return emitter.emit_public(payload, sort_keys=True)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _utc_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + "Z"


def _append_log(path: Path, record: dict[str, Any]) -> None:
    if str(path) == "-":
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)


def _compare(left: Path, right: Path) -> tuple[str, str, bool]:
    left_payload = _load_json(left)
    right_payload = _load_json(right)
    left_bytes = _canonical_bytes(left_payload)
    right_bytes = _canonical_bytes(right_payload)
    left_sha = _sha256(left_bytes)
    right_sha = _sha256(right_bytes)
    match = left_bytes == right_bytes
    return left_sha, right_sha, match


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m presenter.json_canon_compare",
        description="Compare two JSON files using the presenter/emitter canon.",
    )
    parser.add_argument("left", type=Path, help="First JSON payload (vendor upsert)")
    parser.add_argument("right", type=Path, help="Second JSON payload (DB resolve)")
    parser.add_argument(
        "--log",
        type=Path,
        default=DEFAULT_LOG_PATH,
        help="Optional log path for canonical parity records",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        left_sha, right_sha, match = _compare(args.left, args.right)
    except JsonCanonCompareError as exc:
        parser.error(str(exc))
    label = "FILE_EQ_CANON_BYTES_OK" if match else "DIFF"
    lines = [
        f"compare: {label}",
        f"ab_sha256: {left_sha}",
        f"ba_sha256: {right_sha}",
    ]
    sys.stdout.write("\n".join(lines) + "\n")
    record = {
        "at": _utc_iso(),
        "left_path": str(args.left),
        "right_path": str(args.right),
        "left_sha256": left_sha,
        "right_sha256": right_sha,
        "compare": label,
        "match": match,
    }
    if args.log:
        _append_log(args.log, record)
    return 0


if __name__ == "__main__":
    sys.exit(main())
