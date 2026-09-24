#!/usr/bin/env python3
"""Read-only current-row Magic-10 Gate-readiness check (HDE-EPIC040-PR05).

Enumerates only an explicitly selected set of canonical user identities through
the existing ``DBAccess`` abstraction and the PR04 current-row read path, applies
the shared Gate predicate through the existing BodyGraph projection, and reports
bounded, aggregate, identity-safe diagnostics.  It issues no ``UPDATE``,
``INSERT`` or ``DELETE``, performs no acquisition, auto-repair, backfill or
vendor call, and never represents an unavailable dataset as ready.

Exit codes: ``0`` — a report was emitted (``READY`` or ``NOT_READY``); ``5`` —
refusal with one stderr token (``READINESS_EMPTY_SELECTION``,
``READINESS_SELECTION_INVALID`` or ``READINESS_UNAVAILABLE``); argparse usage
errors keep the parser's exit.  The tool never exits ``3``.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.mapped_cache import MappedCacheError, read_current_mapped_bodygraph  # noqa: E402
from engine.bodygraph.projection import (  # noqa: E402
    BodyGraphProjectionError, is_gate_ingress_code, strict_canonical_uuid,
)
from engine.db import DBAccess  # noqa: E402
from engine.db.errors import AdapterError  # noqa: E402
from engine.serializer.canon import sercanon  # noqa: E402

REPORT_SCHEMA = "magic10_gate_readiness.v1"
REFUSAL_EXIT_CODE = 5
READINESS_EMPTY_SELECTION = "READINESS_EMPTY_SELECTION"
READINESS_SELECTION_INVALID = "READINESS_SELECTION_INVALID"
READINESS_UNAVAILABLE = "READINESS_UNAVAILABLE"
COUNT_KEYS = ("ready", "missing", "duplicate", "row_invalid", "payload_invalid", "gates_invalid")
# ``read_current_mapped_bodygraph`` folds a multi-row current view into its
# row-contract refusal; the owning test pins this exact message so drift is caught.
DUPLICATE_ROW_MESSAGE = "current view returned more than one row"


class ReadinessRefusal(RuntimeError):
    """Value-free refusal: no report is emitted and nothing is ready."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class ReadinessReport:
    readiness: str
    provider: str
    requested: int
    selection_sha256: str
    counts: Mapping[str, int]
    diagnostics: tuple[tuple[str, int], ...]

    def to_payload(self) -> dict[str, object]:
        return {
            "schema": REPORT_SCHEMA,
            "readiness": self.readiness,
            "provider": self.provider,
            "read_only": True,
            "selection": {"requested": self.requested, "sha256": self.selection_sha256},
            "counts": {key: self.counts[key] for key in COUNT_KEYS},
            "diagnostics": [{"code": code, "count": count} for code, count in self.diagnostics],
        }


def parse_selection(user_ids: Sequence[str], selection_file: Path | None) -> tuple[str, ...]:
    """Return the sorted, duplicate-free canonical selection or refuse."""
    raw = [value for value in user_ids]
    if selection_file is not None:
        for line in selection_file.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                raw.append(stripped)
    if not raw:
        raise ReadinessRefusal(READINESS_EMPTY_SELECTION)
    if any(strict_canonical_uuid(value) is None for value in raw):
        raise ReadinessRefusal(READINESS_SELECTION_INVALID)
    if len(set(raw)) != len(raw):
        raise ReadinessRefusal(READINESS_SELECTION_INVALID)
    return tuple(sorted(raw))


def selection_digest(selection: Sequence[str]) -> str:
    return hashlib.sha256(sercanon(list(selection), sort_keys=True)).hexdigest()


def observe(db: DBAccess, selection: Sequence[str]) -> ReadinessReport:
    """Read each selected current row once; abort as unavailable on any DB failure."""
    counts = {key: 0 for key in COUNT_KEYS}
    diagnostics: Counter[str] = Counter()
    for user_id in selection:
        try:
            row = read_current_mapped_bodygraph(db, user_id)
        except MappedCacheError as exc:
            if exc.code == "DB_QUERY_FAILED":
                raise ReadinessRefusal(READINESS_UNAVAILABLE) from exc
            if exc.code == "DB_ROW_CONTRACT_VIOLATED" and str(exc) == DUPLICATE_ROW_MESSAGE:
                counts["duplicate"] += 1
            elif exc.code == "DB_ROW_CONTRACT_VIOLATED":
                counts["row_invalid"] += 1
            else:
                counts["payload_invalid"] += 1
            diagnostics[exc.code] += 1
        except BodyGraphProjectionError as exc:
            counts["gates_invalid" if is_gate_ingress_code(exc.code) else "payload_invalid"] += 1
            diagnostics[exc.code] += 1
        except AdapterError as exc:
            raise ReadinessRefusal(READINESS_UNAVAILABLE) from exc
        else:
            counts["missing" if row is None else "ready"] += 1
    readiness = "READY" if counts["ready"] == len(selection) else "NOT_READY"
    return ReadinessReport(
        readiness=readiness,
        provider=str(getattr(db, "provider_name", "unknown")),
        requested=len(selection),
        selection_sha256=selection_digest(selection),
        counts=counts,
        diagnostics=tuple(sorted(diagnostics.items())),
    )


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only current-row Magic-10 Gate-readiness check over an explicit selection",
    )
    parser.add_argument("--user-id", action="append", default=[], metavar="UUID",
                        help="Canonical lowercase hyphenated UUID to check; repeatable")
    parser.add_argument("--selection-file", type=Path, metavar="PATH",
                        help="File with one canonical UUID per line; blank lines and '#' comments ignored")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    try:
        selection = parse_selection(args.user_id, args.selection_file)
        try:
            db = DBAccess.for_current_env()
        except AdapterError as exc:
            raise ReadinessRefusal(READINESS_UNAVAILABLE) from exc
        report = observe(db, selection)
    except ReadinessRefusal as exc:
        sys.stderr.write(f"{exc.code}\n")
        return REFUSAL_EXIT_CODE
    sys.stdout.buffer.write(sercanon(report.to_payload(), sort_keys=True))
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
