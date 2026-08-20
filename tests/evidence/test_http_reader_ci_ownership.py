from __future__ import annotations

from pathlib import Path

from ci.checks import classify_ci_changes as classifier


ROOT = Path(__file__).resolve().parents[2]


def test_http_reader_owner_registry_matches_current_direct_consumers() -> None:
    direct_consumers = {
        candidate.relative_to(ROOT).as_posix()
        for candidate in sorted((ROOT / "tests").rglob("test_*.py"))
        if candidate.is_file()
        and not candidate.is_symlink()
        and classifier._test_module_imports_http_reader(candidate)
    }
    registered_direct = set(classifier._HTTP_READER_TEST_OWNERS) - (
        classifier._HTTP_READER_INDIRECT_TEST_OWNERS
        | {classifier._HTTP_READER_OWNERSHIP_GUARD}
    )

    assert direct_consumers
    assert direct_consumers == registered_direct
    for owner in classifier._HTTP_READER_TEST_OWNERS:
        candidate = ROOT / owner
        assert candidate.is_file(), owner
        assert not candidate.is_symlink(), owner
