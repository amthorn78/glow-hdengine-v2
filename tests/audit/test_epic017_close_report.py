from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = ROOT / "audit/EPIC017_close_report.md"

EXPECTED_HEADINGS = [
    "Overview",
    "D1 — Canonical Serialization Package",
    "D2 — Evidence & Transparency",
    "D3 — Config & Registry",
    "D4 — Matching Logic & Fairness",
    "D5 — Paper Trail and PF Updates",
]


def test_close_report_structure():
    assert REPORT_PATH.exists(), "missing close-out report"
    text = REPORT_PATH.read_text(encoding="utf-8")
    for heading in EXPECTED_HEADINGS:
        assert heading in text
