from __future__ import annotations

import json
from pathlib import Path

from engine.bodygraph import retention


def test_bodygraph_retention_checks_are_read_only():
    for check in retention.BODYGRAPH_RETENTION_CHECKS:
        sql_upper = check.sql.upper()
        assert "DELETE" not in sql_upper
        assert "TRUNCATE" not in sql_upper
        assert sql_upper.startswith("SELECT"), sql_upper


def test_bodygraph_retention_results_report_zero_deletes():
    class FakeDB:
        def __init__(self):
            self.calls: list[str] = []

        def query(self, sql: str, params=None):
            self.calls.append(sql)
            return [(123,)]

    db = FakeDB()
    results = retention.run_bodygraph_retention(db)  # type: ignore[arg-type]
    assert db.calls
    for entry in results:
        assert entry["deleted_rows"] == 0
        assert entry["inspected_rows"] == 123


def test_retention_log_includes_bodygraph_entry():
    path = Path("artifacts/db/retention/retention_run.log")
    assert path.exists(), "retention_run.log missing"
    records = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    tables = {rec.get("table"): rec for rec in records if "table" in rec}
    entry = tables.get("hde.body_graphs")
    assert entry, "missing hde.body_graphs entry"
    assert entry["deleted_rows"] == 0
    assert entry["action"] == "verify-only"
