"""Retention helpers for BodyGraph durability objects."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Mapping, Sequence

from engine.db.adapter import DBAccess


@dataclass(frozen=True)
class RetentionCheck:
    """Describes a retention inspection query for a table or view."""

    table: str
    sql: str
    action: str = "verify-only"


BODYGRAPH_RETENTION_CHECKS: Sequence[RetentionCheck] = (
    RetentionCheck("hde.body_graphs", "SELECT COUNT(*) FROM hde.body_graphs"),
    RetentionCheck(
        "hde.body_graphs_current",
        "SELECT COUNT(*) FROM hde.body_graphs_current",
    ),
    RetentionCheck(
        "public.hde_body_graphs_current",
        "SELECT COUNT(*) FROM public.hde_body_graphs_current",
    ),
)


class RetentionError(RuntimeError):
    """Raised when the retention harness encounters an unrecoverable issue."""


def _run_query(db: DBAccess, sql: str) -> int:
    rows = db.query(sql)
    if not rows:
        raise RetentionError(f"no_rows_returned:{sql}")
    try:
        return int(rows[0][0])
    except (ValueError, TypeError) as exc:  # pragma: no cover - defensive
        raise RetentionError(f"invalid_count:{sql}") from exc


def run_bodygraph_retention(db: DBAccess) -> List[Mapping[str, object]]:
    """Execute retention checks for BodyGraph durability tables/views.

    The BodyGraph durability policy forbids hard deletes or truncates for
    `hde.body_graphs` and its views. This helper enforces that by only issuing
    read-only queries (counts) and returning structured records that always
    report `deleted_rows = 0`. Any future retention/archival changes must keep
    this invariant intact.
    """

    results: List[Mapping[str, object]] = []
    for check in BODYGRAPH_RETENTION_CHECKS:
        count = _run_query(db, check.sql)
        results.append(
            {
                "table": check.table,
                "action": check.action,
                "inspected_rows": count,
                "deleted_rows": 0,
            }
        )
    return results
