from __future__ import annotations

import sys
from pathlib import Path
from types import ModuleType

import pytest

from ci.checks import classify_ci_changes as classifier
from ci.checks import import_http_reader_for_tests as reader_seam


ROOT = Path(__file__).resolve().parents[2]


def _python_modules() -> tuple[Path, ...]:
    return tuple(
        candidate
        for candidate in sorted((ROOT / "tests").rglob("*.py"))
        if candidate.is_file() and not candidate.is_symlink()
    )


def test_http_reader_owner_registry_matches_current_consumers() -> None:
    candidates = _python_modules()
    direct_consumers = {
        candidate.relative_to(ROOT).as_posix()
        for candidate in candidates
        if candidate.name.startswith("test_")
        and classifier._test_module_imports_http_reader(candidate)
    }
    static_support_consumers = {
        candidate.relative_to(ROOT).as_posix()
        for candidate in candidates
        if not candidate.name.startswith("test_")
        and classifier._test_module_imports_http_reader(candidate)
    }
    seam_consumers = {
        candidate.relative_to(ROOT).as_posix()
        for candidate in candidates
        if classifier._test_module_imports_http_reader_seam(candidate)
    }
    registered_direct = set(classifier._HTTP_READER_TEST_OWNERS) - (
        classifier._HTTP_READER_INDIRECT_TEST_OWNERS
        | classifier._HTTP_READER_DYNAMIC_TEST_OWNERS
        | {classifier._HTTP_READER_OWNERSHIP_GUARD}
    )

    literal_references = {
        candidate.relative_to(ROOT).as_posix()
        for candidate in candidates
        if classifier._test_module_references_http_reader(candidate)
    }

    assert direct_consumers
    assert direct_consumers == registered_direct
    assert not static_support_consumers
    assert seam_consumers == (
        classifier._HTTP_READER_DYNAMIC_TEST_OWNERS
        | {classifier._HTTP_READER_OWNERSHIP_GUARD}
    )
    assert classifier._HTTP_READER_DYNAMIC_TEST_OWNERS <= set(
        classifier._HTTP_READER_TEST_OWNERS
    )
    assert classifier._HTTP_READER_LITERAL_REFERENCE_TEST_OWNERS <= (
        classifier._HTTP_READER_INDIRECT_TEST_OWNERS
    )
    assert classifier._HTTP_READER_INDIRECT_TEST_OWNERS <= set(
        classifier._HTTP_READER_TEST_OWNERS
    )
    assert set(classifier._HTTP_READER_DYNAMIC_TEST_OWNER_SHA256) == (
        classifier._HTTP_READER_DYNAMIC_TEST_OWNERS
    )
    for path in sorted(classifier._HTTP_READER_DYNAMIC_TEST_OWNERS):
        classifier._validate_http_reader_dynamic_owner(ROOT / path, path)
    assert literal_references == (
        classifier._HTTP_READER_DYNAMIC_TEST_OWNERS
        | classifier._HTTP_READER_LITERAL_REFERENCE_TEST_OWNERS
    )
    for owner in classifier._HTTP_READER_TEST_OWNERS:
        candidate = ROOT / owner
        assert candidate.is_file(), owner
        assert not candidate.is_symlink(), owner

    seam = ROOT / classifier._HTTP_READER_TEST_IMPORT_SEAM
    assert seam.is_file()
    assert not seam.is_symlink()


def test_dynamic_reader_owner_edits_require_explicit_review(
    tmp_path: Path,
) -> None:
    path = sorted(classifier._HTTP_READER_DYNAMIC_TEST_OWNERS)[0]
    candidate = tmp_path / Path(path).name
    candidate.write_bytes((ROOT / path).read_bytes() + b"\n# changed owner shape\n")
    with pytest.raises(
        ValueError,
        match="CI_HTTP_READER_DYNAMIC_OWNER_REVIEW_REQUIRED",
    ):
        classifier._validate_http_reader_dynamic_owner(candidate, path)


def test_http_reader_detection_has_deliberately_bounded_source_shapes(
    tmp_path: Path,
) -> None:
    module = classifier._HTTP_READER_MODULE
    sources = {
        "static.py": f"from {module} import create_app\n",
        "static_submodule.py": f"import {module}.routes\n",
        "relative.py": "from .adapter import http_reader\n",
        "seam.py": (
            f"from {classifier._HTTP_READER_TEST_IMPORT_MODULE} "
            "import import_http_reader_for_test\n"
        ),
        "raw_dynamic.py": (
            "import importlib\n"
            f"importlib.import_module(name={module!r})\n"
        ),
        "concatenated.py": (
            "import importlib\n"
            "importlib.import_module('adapter.' + 'http_reader')\n"
        ),
        "keyword_patch.py": (
            "from unittest.mock import patch\n"
            f"patch(target={(module + '.create_app')!r})\n"
        ),
        "local_patch_target.py": (
            "from unittest.mock import patch\n"
            "def test_reader():\n"
            f"    target = {(module + '.create_app')!r}\n"
            "    patch(target)\n"
        ),
        "exec.py": "exec('import adapter.' + 'http_reader')\n",
        "innocent_reference.py": f"EXPECTED = {module!r}\n",
    }
    static: dict[str, bool] = {}
    references: dict[str, bool] = {}
    seam_imports: dict[str, bool] = {}
    for name, source in sources.items():
        candidate = tmp_path / name
        candidate.write_text(source, encoding="utf-8")
        static[name] = classifier._test_module_imports_http_reader(candidate)
        references[name] = classifier._test_module_references_http_reader(candidate)
        seam_imports[name] = classifier._test_module_imports_http_reader_seam(
            candidate
        )

    assert {name for name, matched in static.items() if matched} == {
        "static.py",
        "static_submodule.py",
    }
    assert {name for name, matched in references.items() if matched} == {
        "raw_dynamic.py",
        "concatenated.py",
        "keyword_patch.py",
        "local_patch_target.py",
        "exec.py",
        "innocent_reference.py",
    }
    assert {name for name, matched in seam_imports.items() if matched} == {
        "seam.py",
    }


def test_http_reader_import_seam_forces_the_real_fresh_import(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    events: list[str] = []
    imported = ModuleType(classifier._HTTP_READER_MODULE)

    def invalidate() -> None:
        events.append("invalidate")

    def import_module(name: str) -> ModuleType:
        assert name == classifier._HTTP_READER_MODULE
        assert "adapter" not in sys.modules
        assert classifier._HTTP_READER_MODULE not in sys.modules
        events.append(f"import:{name}")
        return imported

    monkeypatch.setattr(reader_seam.importlib, "invalidate_caches", invalidate)
    monkeypatch.setattr(reader_seam.importlib, "import_module", import_module)
    monkeypatch.setitem(sys.modules, "adapter", ModuleType("adapter"))
    monkeypatch.setitem(
        sys.modules,
        classifier._HTTP_READER_MODULE,
        ModuleType(classifier._HTTP_READER_MODULE),
    )

    assert reader_seam.import_http_reader_for_test() is imported
    assert events == [
        "invalidate",
        f"import:{classifier._HTTP_READER_MODULE}",
    ]
