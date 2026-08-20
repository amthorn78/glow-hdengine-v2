from __future__ import annotations

import hashlib
from pathlib import Path

from ci.checks import classify_ci_changes as classifier


ROOT = Path(__file__).resolve().parents[2]


def _test_python_candidates() -> tuple[Path, ...]:
    return tuple(sorted((ROOT / "tests").rglob("*.py")))


def _test_tree_candidates() -> tuple[Path, ...]:
    return tuple(sorted((ROOT / "tests").rglob("*")))


def test_http_reader_owner_registry_matches_current_direct_consumers() -> None:
    direct_consumers = {
        candidate.relative_to(ROOT).as_posix()
        for candidate in _test_python_candidates()
        if candidate.is_file()
        and not candidate.is_symlink()
        and classifier._is_pytest_test_module(candidate)
        and classifier._test_module_imports_http_reader(candidate)
    }
    registered_direct = set(classifier._HTTP_READER_TEST_OWNERS) - (
        classifier._HTTP_READER_INDIRECT_TEST_OWNERS
        | {classifier._HTTP_READER_OWNERSHIP_GUARD}
    )
    direct_dispositions = registered_direct | set(
        classifier._HTTP_READER_DIRECT_NON_OWNERS
    )

    assert direct_consumers
    assert direct_consumers == direct_dispositions
    assert not (
        classifier._HTTP_READER_DIRECT_NON_OWNERS
        & set(classifier._HTTP_READER_TEST_OWNERS)
    )
    for nonowner in classifier._HTTP_READER_DIRECT_NON_OWNERS:
        candidate = ROOT / nonowner
        assert candidate.is_file(), nonowner
        assert not candidate.is_symlink(), nonowner
        assert hashlib.sha256(candidate.read_bytes()).hexdigest() == (
            classifier._HTTP_READER_DIRECT_NON_OWNER_SHA256[nonowner]
        )
    for owner in classifier._HTTP_READER_TEST_OWNERS:
        candidate = ROOT / owner
        assert candidate.is_file(), owner
        assert not candidate.is_symlink(), owner


def test_http_reader_test_support_has_no_direct_consumers() -> None:
    support_consumers = {
        candidate.relative_to(ROOT).as_posix()
        for candidate in _test_python_candidates()
        if candidate.is_file()
        and not candidate.is_symlink()
        and not classifier._is_pytest_test_module(candidate)
        and classifier._test_module_imports_http_reader(candidate)
    }

    assert support_consumers == set()


def test_http_reader_bridge_registry_covers_every_indirect_consumer() -> None:
    bridge_consumers = {
        candidate.relative_to(ROOT).as_posix()
        for candidate in _test_python_candidates()
        if candidate.is_file()
        and not candidate.is_symlink()
        and classifier._test_module_imports_http_reader_bridge(candidate)
        and not classifier._test_module_imports_http_reader(candidate)
    }
    dispositions = set(classifier._HTTP_READER_INDIRECT_TEST_OWNERS) | set(
        classifier._HTTP_READER_INDIRECT_NON_OWNERS
    )

    assert bridge_consumers
    assert bridge_consumers == dispositions
    active_nonowners = set(classifier._HTTP_READER_INDIRECT_NON_OWNERS) - set(
        classifier._FULL_VALIDATION_INACTIVE_TESTS
    )
    assert active_nonowners == {
        "tests/_helpers/app_import.py",
        "tests/adapter/test_env_guard_import_purity.py",
        "tests/adapter/test_jsonschema.py",
        "tests/adapter/test_readyz.py",
    }


def test_http_reader_bridge_topology_is_live_and_independent() -> None:
    topology = classifier._HTTP_READER_BRIDGE_TOPOLOGY

    assert set(topology) == set(classifier._HTTP_READER_BRIDGE_MODULES)
    for bridge, chain in sorted(topology.items()):
        source_path = ROOT / Path(*bridge.split(".")).with_suffix(".py")
        assert source_path.is_file(), bridge
        assert not source_path.is_symlink(), bridge
        for module in chain:
            assert classifier._python_module_imports(
                source_path, module
            ), f"{bridge} -> {module}"
            source_path = ROOT / Path(*module.split(".")).with_suffix(".py")
            assert source_path.is_file(), module
            assert not source_path.is_symlink(), module


def test_http_reader_indirect_owner_bridges_are_live() -> None:
    bridges = classifier._HTTP_READER_INDIRECT_OWNER_BRIDGES

    assert set(bridges) == classifier._HTTP_READER_INDIRECT_TEST_OWNERS
    assert set(bridges) <= set(classifier._HTTP_READER_TEST_OWNERS)
    for owner, chain in sorted(bridges.items()):
        owner_path = ROOT / owner
        assert classifier._is_pytest_test_module(owner_path), owner
        assert owner_path.is_file(), owner
        assert not owner_path.is_symlink(), owner
        source_path = owner_path
        for module in chain:
            target_path = ROOT / Path(*module.split(".")).with_suffix(".py")
            assert target_path.is_file(), module
            assert not target_path.is_symlink(), module
            assert classifier._python_module_statically_imports(
                source_path, module
            ), f"{source_path.relative_to(ROOT).as_posix()} -> {module}"
            source_path = target_path
        assert chain[-1] == "adapter.http_reader", owner


def test_test_tree_has_no_symlinks() -> None:
    symlinks = {
        candidate.relative_to(ROOT).as_posix()
        for candidate in _test_tree_candidates()
        if candidate.is_symlink()
    }

    assert symlinks == set()
