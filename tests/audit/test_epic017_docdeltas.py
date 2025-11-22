from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCDELTA_DIR = ROOT / "audit/docdeltas"
EXPECTED_FILES = [
    "PF09_EPIC017_redlines.md",
    "PF10_EPIC017_addendum.md",
    "PF12_EPIC017_registry_and_mirror.md",
    "PF14_EPIC017_mechanics_and_CI.md",
    "PF19_EPIC017_evidence_CI_rails.md",
    "PF20_EPIC017_record.md",
    "PF04_EPIC017_tokens_and_env.md",
]


def test_docdeltas_exist_and_nonempty():
    assert DOCDELTA_DIR.exists(), "docdeltas directory missing"
    for filename in EXPECTED_FILES:
        path = DOCDELTA_DIR / filename
        assert path.exists(), f"missing {filename}"
        assert path.read_text(encoding="utf-8").strip(), f"empty {filename}"
